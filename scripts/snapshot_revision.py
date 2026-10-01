"""Archive a concept review baseline without overwriting existing revisions."""
import argparse
import hashlib
import json
import re
import uuid
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def revision_id(value):
    if not re.fullmatch(r'C[0-9]{2,}[a-z]?', value):
        raise argparse.ArgumentTypeError('Use C01, C02, or an erratum such as C01a')
    return value

def verify(revision):
    folder = ROOT / 'revisions' / revision
    manifest = json.loads((folder / 'manifest.json').read_text(encoding='utf-8'))
    archive = folder / 'snapshot.zip'
    if manifest['revision'] != revision or digest(archive.read_bytes()) != manifest['archive_sha256']:
        raise ValueError('Revision identity or archive checksum mismatch')
    with zipfile.ZipFile(archive) as z:
        if set(z.namelist()) != set(manifest['files']):
            raise ValueError('Archive member list differs from manifest')
        for name, expected in manifest['files'].items():
            if digest(z.read(name)) != expected['sha256']:
                raise ValueError('Checksum mismatch: ' + name)
    print(f'{revision}: verified {len(manifest["files"])} archived files; active workspace not compared.')

def snapshot(revision, note):
    model = json.loads((ROOT / 'data/concepts.json').read_text(encoding='utf-8'))
    if model['revision'] != revision:
        raise ValueError(f'Requested {revision}, but active data revision is {model["revision"]}')
    dest = ROOT / 'revisions' / revision
    if dest.exists():
        raise FileExistsError(f'{dest} already exists; choose a new revision, never overwrite')
    files = []
    for name in ['README.md','HOUSE_BUILDING_PLAN.md','AGENTS.md','PROJECT_STATE.md','plot_dimensions.jpg']:
        p = ROOT / name
        if p.is_file(): files.append(p)
    for directory, suffixes in [('data',{'.json','.yaml','.csv'}),('src',{'.html','.js','.css'}),
                                ('scripts',{'.py'}),('docs',{'.md'}),('.agents/skills',{'.md','.yaml'})]:
        base = ROOT / directory
        if base.exists():
            files.extend(p for p in base.rglob('*') if p.is_file() and p.suffix in suffixes)
    # Top-level deliverables only: never include Chrome profiles or nested archives.
    files.extend(p for p in (ROOT/'outputs').iterdir() if p.is_file() and p.suffix in {'.html','.md','.svg','.png','.pdf'})
    required = ['outputs/house-concepts.html','outputs/geometry-review.md',f'docs/concept-study-{revision}.md']
    for name in required:
        if not (ROOT/name).is_file(): raise FileNotFoundError('Required review artifact missing: '+name)
    payload = {p.relative_to(ROOT).as_posix():p.read_bytes() for p in sorted(set(files))}
    revision_root = ROOT/'revisions'
    revision_root.mkdir(exist_ok=True)
    stage = revision_root / f'.{revision}-{uuid.uuid4().hex}.partial'
    stage.mkdir()
    archive = stage/'snapshot.zip'
    with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED) as z:
        for name,raw in payload.items(): z.writestr(name,raw)
    manifest = {
        'revision':revision, 'created_utc':datetime.now(timezone.utc).isoformat(),
        'purpose':'Preserved concept review baseline; not owner or professional approval',
        'note':note, 'archive_sha256':digest(archive.read_bytes()),
        'files':{name:{'sha256':digest(raw),'bytes':len(raw)} for name,raw in payload.items()}
    }
    (stage/'manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    # Both paths are explicit descendants of this project's revisions directory.
    # Windows refuses rename onto an existing nonempty revision directory.
    if dest.exists(): raise FileExistsError('Destination appeared during snapshot; staging retained')
    stage.rename(dest)
    verify(revision)
    print(f'Created revisions/{revision}/snapshot.zip and manifest.json')

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--revision',type=revision_id)
    group.add_argument('--verify',type=revision_id)
    parser.add_argument('--note',default='Concept review baseline')
    args=parser.parse_args()
    try:
        verify(args.verify) if args.verify else snapshot(args.revision,args.note)
    except (OSError,ValueError,KeyError,zipfile.BadZipFile) as exc:
        parser.exit(1,str(exc)+'\n')
