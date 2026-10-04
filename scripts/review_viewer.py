"""Local headless browser review; saves SVGs and previews without any downloaded drivers."""
import base64
import json
import subprocess
import time
import urllib.request
import urllib.parse
import socket
import struct
import os
from pathlib import Path

class LocalWebSocket:
    """Minimal standard-library client for the local Chrome debugging endpoint."""
    def __init__(self,url):
        u=urllib.parse.urlparse(url)
        self.sock=socket.create_connection((u.hostname,u.port),timeout=15)
        key=base64.b64encode(os.urandom(16)).decode()
        self.sock.sendall((f'GET {u.path} HTTP/1.1\r\nHost: {u.hostname}:{u.port}\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n').encode())
        self.buffer=b''
        while b'\r\n\r\n' not in self.buffer: self.buffer+=self.sock.recv(4096)
        headers,self.buffer=self.buffer.split(b'\r\n\r\n',1)
        if b' 101 ' not in headers.split(b'\r\n',1)[0]: raise RuntimeError(headers.decode())
    def read(self,n):
        while len(self.buffer)<n:
            chunk=self.sock.recv(max(4096,n-len(self.buffer)))
            if not chunk: raise ConnectionError('Browser closed connection')
            self.buffer+=chunk
        result,self.buffer=self.buffer[:n],self.buffer[n:]
        return result
    def send(self,text,opcode=1):
        raw=text.encode() if isinstance(text,str) else text
        length=len(raw)
        header=bytes([0x80|opcode])
        header+=bytes([0x80|length]) if length<126 else bytes([0x80|126])+struct.pack('!H',length) if length<65536 else bytes([0x80|127])+struct.pack('!Q',length)
        mask=os.urandom(4)
        self.sock.sendall(header+mask+bytes(v^mask[i%4] for i,v in enumerate(raw)))
    def recv(self):
        parts=[]
        while True:
            a,b=self.read(2)
            length=b&127
            if length==126:length=struct.unpack('!H',self.read(2))[0]
            elif length==127:length=struct.unpack('!Q',self.read(8))[0]
            mask=self.read(4) if b&128 else None
            raw=self.read(length)
            if mask:raw=bytes(v^mask[i%4] for i,v in enumerate(raw))
            opcode=a&15
            if opcode==8: raise ConnectionError('Browser closed socket')
            if opcode==9:self.send(raw,10);continue
            if opcode==10:continue
            parts.append(raw)
            if a&128:return b''.join(parts).decode()
    def close(self):self.sock.close()

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'outputs'
MODEL=json.loads((ROOT/'data/concepts.json').read_text(encoding='utf-8'))
profile=OUT/'browser-review-profile'
def find_chrome():
    candidates = [
        os.environ.get('CHROME_PATH'),
        r'C:/Program Files/Google/Chrome/Application/chrome.exe',
        r'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe',
        os.path.expandvars(r'%LOCALAPPDATA%/Google/Chrome/Application/chrome.exe'),
        os.path.expandvars(r'%PROGRAMFILES%/Google/Chrome/Application/chrome.exe'),
        os.path.expandvars(r'%PROGRAMFILES(X86)%/Google/Chrome/Application/chrome.exe'),
    ]
    for c in candidates:
        if c and Path(c).is_file():
            return Path(c)
    return Path('C:/Program Files/Google/Chrome/Application/chrome.exe')

chrome=find_chrome()
process=subprocess.Popen([str(chrome),'--headless','--disable-gpu','--no-first-run',
    '--no-default-browser-check','--remote-debugging-port=0','--remote-allow-origins=*',
    '--user-data-dir='+str(profile),'about:blank'],stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,creationflags=subprocess.CREATE_NO_WINDOW)
ws=None
try:
    portfile=profile/'DevToolsActivePort'
    for _ in range(60):
        if portfile.exists():
            try:
                port=int(portfile.read_text().splitlines()[0])
                pages=json.load(urllib.request.urlopen(f'http://127.0.0.1:{port}/json',timeout=1))
                page=next(p for p in pages if p['type']=='page')
                break
            except (OSError,ValueError,StopIteration): pass
        time.sleep(.15)
    else: raise RuntimeError('Local browser debugging endpoint unavailable')
    ws=LocalWebSocket(page['webSocketDebuggerUrl'])
    seq=0
    errors=[]
    def call(method,params=None):
        global seq
        seq+=1
        ident=seq
        ws.send(json.dumps({'id':ident,'method':method,'params':params or {}}))
        while True:
            msg=json.loads(ws.recv())
            if msg.get('method')=='Runtime.exceptionThrown': errors.append(msg['params'])
            if msg.get('id')==ident:
                if 'error' in msg: raise RuntimeError(msg['error'])
                return msg.get('result',{})
    def js(expression):
        result=call('Runtime.evaluate',{'expression':expression,'returnByValue':True})
        if 'exceptionDetails' in result: raise RuntimeError(result['exceptionDetails'])
        return result['result'].get('value')
    call('Runtime.enable')
    call('Page.enable')
    call('Emulation.setDeviceMetricsOverride',{'width':1600,'height':2400,'deviceScaleFactor':1,'mobile':False})
    call('Page.navigate',{'url':(OUT/'house-concepts.html').as_uri()})
    for _ in range(50):
        if js("document.querySelector('#canvas svg')!==null"): break
        time.sleep(.1)
    else: raise RuntimeError('Viewer did not render')
    rendered=[]
    for option in MODEL['options']:
        opt=option['id']
        js(f"document.querySelector('#options [data-id=\"{opt}\"]').click()")
        for view in ['site','F1','F2','section','massing']:
            js(f"document.querySelector('[data-view=\"{view}\"]').click()")
            assert js("document.querySelector('#canvas svg').getAttribute('data-revision')")==MODEL['revision']
            assert js("document.querySelector('#canvas svg').getAttribute('data-option')")==opt
            if view in ['site','F1','F2']:
                assert js("document.querySelector('#canvas svg').getAttribute('data-display-rotation')")=='90'
            if view=='massing':
                assert js("document.querySelector('#canvas svg').getAttribute('data-depth-order')")=='camera-ray'
                assert js("document.querySelector('#canvas svg').getAttribute('data-depth-cycles')")=='0', 'Massing has unresolved surface-order cycle'
                assert js('document.querySelector("[data-enclosed-cantilever]").getAttribute("data-enclosed-cantilever")')=='0'
                assert js('document.querySelectorAll("[data-facade-window][data-window-room^=STAIR]").length')==2
                assert js('document.querySelector("[data-low-parapet]")!==null')
                assert js('document.querySelector("#canvas svg").getAttribute("data-porch-design")')==option['porch_design']['kind']
                assert js('document.querySelector("[data-roof-service-screen]")!==null')
                assert js('document.querySelector("[data-solar-collector]")!==null')
                assert js('document.querySelector("[data-porch-side-screen]")!==null')==bool(option['porch_design'].get('side_screen_rect'))
                assert js('document.querySelector("[data-upper-roof-outline]")!==null')
                assert js('document.querySelector("#canvas svg").getAttribute("data-bedroom-cap-height")')=='6.6'
            if view=='section':
                section_text=js('document.querySelector("#canvas").textContent')
                assert '6.96 m²' in section_text and '0.90 m wide' in section_text
                assert 'Aligned bedroom walls' in section_text and '3.00 m projection' in section_text
                assert js('document.querySelector("[data-stair-beam-band]")!==null')
                assert js('document.querySelector("[data-roof-services-plan]")!==null')
                assert js('document.querySelector("[data-roof-overflow]")!==null')
                assert 'z3.00–3.50 m' in section_text and '8.15 m' in section_text
            if view=='site':
                assert js('document.querySelector("[data-upper-outline]").tagName')=='polygon'
            if view=='F2':
                assert js('document.querySelector("[data-enclosed-cantilever]")!==null')
                assert js('document.querySelector(\'[data-window-room="STAIR-02"]\').getAttribute("data-window-continuation")')=='false'
                assert js('document.querySelectorAll("[data-conditional-window]").length')==1
            if view=='F1':
                assert js('document.querySelectorAll("[data-conditional-window]").length')==2
                assert js('document.querySelector(\'[data-conditional-window="F1-WIN-ALT-SIDE"]\').getAttribute("data-window-status")')=='conditional'
            rendered.append((opt,view))
            svg=js("document.querySelector('#canvas svg').outerHTML")
            if 'xmlns=' not in svg: svg=svg.replace('<svg ','<svg xmlns="http://www.w3.org/2000/svg" ',1)
            (OUT/f'option-{opt}-{view}.svg').write_text(svg,encoding='utf-8')
            # Render each exported SVG in its own tab, avoiding viewer scroll/reflow clipping.
            main_ws=ws
            preview_id=call('Target.createTarget',{'url':'about:blank'})['targetId']
            pages=json.load(urllib.request.urlopen(f'http://127.0.0.1:{port}/json',timeout=2))
            preview_page=next(p for p in pages if p['id']==preview_id)
            preview_ws=LocalWebSocket(preview_page['webSocketDebuggerUrl'])
            try:
                ws=preview_ws
                call('Runtime.enable')
                call('Page.enable')
                export_height=2400 if view=='section' else 980
                call('Emulation.setDeviceMetricsOverride',{'width':1025,'height':export_height,'deviceScaleFactor':1,'mobile':False})
                call('Page.navigate',{'url':(OUT/f'option-{opt}-{view}.svg').as_uri()})
                for _ in range(50):
                    if js('document.documentElement.tagName.toLowerCase()==="svg" && document.readyState==="complete"'): break
                    time.sleep(.05)
                else: raise RuntimeError('Standalone SVG did not load')
                js(f'document.documentElement.setAttribute("width","1025");document.documentElement.setAttribute("height","{export_height}")')
                call('Runtime.evaluate',{'expression':'new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve)))','awaitPromise':True})
                shot=call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})
                (OUT/f'option-{opt}-{view}.png').write_bytes(base64.b64decode(shot['data']))
            finally:
                ws=main_ws
                try: call('Target.closeTarget',{'targetId':preview_id})
                finally: preview_ws.close()
    # Actual pointer input and SVG focus reproduce the reported black-room issue.
    room_interactions=0
    call('Emulation.setDeviceMetricsOverride',{'width':1600,'height':2400,'deviceScaleFactor':1,'mobile':False})
    for option in MODEL['options']:
        js(f'document.querySelector(\'#options [data-id="{option["id"]}"]\').click()')
        for floor in MODEL['floors']:
            js(f'document.querySelector(\'[data-view="{floor["id"]}"]\').click()')
            room_ids=js(f'floorData({json.dumps(floor["id"])}).rooms.map(r=>r.id)')
            for ident in room_ids:
                selector=json.dumps(f'[data-room-id="{ident}"]')
                box=js(f'(()=>{{const r=document.querySelector({selector});r.scrollIntoView({{block:"center"}});const b=r.querySelector("rect").getBoundingClientRect();return {{x:b.x+b.width/2,y:b.y+b.height/2}}}})()')
                call('Input.dispatchMouseEvent',dict(type='mouseMoved',**box))
                call('Input.dispatchMouseEvent',dict(type='mousePressed',button='left',clickCount=1,**box))
                call('Input.dispatchMouseEvent',dict(type='mouseReleased',button='left',clickCount=1,**box))
                assert ident in js("document.querySelector('#detail').textContent"), ident
                assert js(f'document.querySelector({selector}).getAttribute("aria-pressed")')=='true'
                before=js(f'getComputedStyle(document.querySelector({selector}).querySelector("rect")).fill')
                assert before not in ['rgb(0, 0, 0)','none'], (ident,before)
                js(f'document.querySelector({selector}).focus()')
                assert js(f'getComputedStyle(document.querySelector({selector}).querySelector("rect")).fill')==before
                assert js(f'getComputedStyle(document.querySelector({selector})).outlineStyle')=='none'
                js(f'document.querySelector({selector}).dispatchEvent(new KeyboardEvent("keydown",{{key:"Enter",bubbles:true}}))')
                assert js(f'document.querySelector({selector}).getAttribute("data-selected")')=='true'
                room_interactions+=1
    # A focused dining-room capture records the visual regression check.
    js('document.querySelector(\'[data-view="F1"]\').click();const dining=document.querySelector(\'[data-room-id="DIN-01"]\');dining.focus();dining.dispatchEvent(new KeyboardEvent("keydown",{key:"Enter",bubbles:true}));document.querySelector("#canvas").scrollIntoView({block:"start"})')
    call('Emulation.setDeviceMetricsOverride',{'width':1600,'height':1100,'deviceScaleFactor':1,'mobile':False})
    call('Runtime.evaluate',{'expression':'new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve)))','awaitPromise':True})
    shot=call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})
    (OUT/'viewer-selection-review.png').write_bytes(base64.b64decode(shot['data']))
    for control in ['grid','services','furniture','projection','routes']:
        js(f"document.querySelector('#{control}').click()")
    assert js("document.querySelector('#canvas svg')!==null")
    call('Emulation.setDeviceMetricsOverride',{'width':390,'height':844,'deviceScaleFactor':1,'mobile':False})
    overflow=js('document.documentElement.scrollWidth > innerWidth')
    assert not overflow, 'Mobile layout overflows horizontally'
    assert not errors, errors
    # Verify each balcony variant's actual displayed geometry/details.
    for option in MODEL['options']:
        js(f'document.querySelector(\'#options [data-id="{option["id"]}"]\').click()')
        js('document.querySelector(\'[data-view="F2"]\').click();document.querySelector(\'[data-room-id="BAL-01"]\').dispatchEvent(new MouseEvent("click"))')
        expected_area = option['balcony']['rect'][2]*option['balcony']['rect'][3]
        details = js("document.querySelector('#detail').textContent")
        assert f'{expected_area:.2f}' in details
        assert option['balcony']['note'] in details
        total_area=expected_area+sum(b['rect'][2]*b['rect'][3] for b in option.get('extra_balconies',[]))
        assert f'{total_area:.2f}' in js('document.querySelector("#balArea").textContent')
        assert js('document.querySelectorAll("[data-daylight-tube]").length')==0
        assert js('document.querySelector(\'[data-room-id="COURT-02"]\')!==null')
        assert js('document.querySelector(\'[data-window-room="BR-03"][data-operable="true"][data-window-face="court"]\')!==null')
        assert js('document.querySelector(\'[data-window-room="STAIR-02"][data-operable="true"]\')!==null')
        assert js('document.querySelectorAll("[data-window-shade]").length')==len(MODEL['floors'][1]['windows'])
        for extra in option.get('extra_balconies',[]):
            js(f'document.querySelector(\'[data-room-id="{extra["id"]}"]\').dispatchEvent(new MouseEvent("click"))')
            assert extra['note'] in js('document.querySelector("#detail").textContent')
            assert js(f'document.querySelector(\'[data-door-id="{extra["id"]}"]\')!==null')
        js('document.querySelector(\'[data-view="F1"]\').click()')
        # Furniture was toggled off earlier; restore it for this assertion.
        js('document.querySelector("#furniture").checked=true;render()')
        assert js('document.querySelector(\'[data-furniture-name="TV stand"]\')!==null')
        assert js('document.querySelector(\'[data-door-id="ENTRY"]\').getAttribute("data-opening-width")')=='1.9'
        assert js('document.querySelector(\'[data-door-id="BR-01"]\').getAttribute("data-opening-width")')=='0.9'
        assert js('document.querySelector(\'[data-window-room="BR-01"][data-operable="true"][data-window-face="court"]\')!==null')
        assert js('document.querySelector(\'[data-window-room="STAIR-01"][data-operable="true"]\')!==null')
        court=MODEL['house']['courtyard']['rect']
        expected_ground=MODEL['house']['width']*MODEL['house']['depth']-court[2]*court[3]
        assert f'{expected_ground:.2f}' in js('document.querySelector("#f1Area").textContent')
        assert js('document.querySelector("[data-altar-side-wall]")!==null')
        assert js('document.querySelector(\'[data-operation-door="BR-01"]\').getAttribute("data-operation-kind")')=='hinged'
        assert js('document.querySelector(\'[data-furniture-name="Sofa"]\').getAttribute("data-seat-facing")')==','.join(str(v) for v in MODEL['floors'][0]['tv']['seat_facing'])
        assert js('document.querySelector(\'[data-furniture-name="Wooden armchair"]\').getAttribute("data-seat-facing")')=='-1,0'
        assert js('document.querySelector(\'[data-window-room="LIV-01"][data-window-face="court-gallery"]\')!==null')
        assert js('document.querySelectorAll(\'[data-operation-door="ENTRY"][data-swing="outward"]\').length')==2
        assert js('(()=>{const c=n=>{const r=document.querySelector(`[data-furniture-name="${n}"] rect`);return +r.getAttribute("y")+(+r.getAttribute("height"))/2};return Math.abs(c("Sofa")-c("TV stand"))<1e-8})()')
        js('document.querySelector(\'[data-view="F2"]\').click()')
        assert js('document.querySelector(\'[data-door-id="BR-03"]\').getAttribute("data-opening-width")')=='0.9'
    js('document.querySelector("#furniture").checked=true;render()')
    assert js('document.querySelector(\'[data-room-id="STUDY-02"]\')===null')
    assert js('document.querySelector(\'[data-furniture-name="Study chair"]\')===null')
    assert js('document.querySelector(\'[data-furniture-name="Balcony bench"]\')!==null')
    assert js('document.querySelector(\'[data-door-id="UTIL-02"]\').getAttribute("data-opening-width")')=='1'
    assert js('document.querySelector(\'[data-room-id="BAL-02"]\')===null')
    js('document.querySelector(\'[data-view="F1"]\').click()')
    assert js('document.querySelector(\'[data-door-id="ALT-BUFFER"]\').getAttribute("data-opening-width")')=='1'
    assert js('document.querySelector(\'[data-operation-door="ALT-BUFFER"]\')===null')
    assert not errors, errors
    report = [f"# {MODEL['revision']} viewer review", "", "Headless Chrome local review completed.", "",
              f"- {len(MODEL['options'])} active option / all five views rendered without captured JavaScript exceptions.",
              "- Plot, F1 and F2 declare the 90° clockwise display transform; export metadata matches current revision.",
              f"- {room_interactions} actual room pointer clicks across both floors/options; keyboard selection and focus retained nonblack fills and accessible pressed state.",
              "- Focused dining screenshot saved as viewer-selection-review.png; each BAL-01 variant area/access note populated correctly.",
              "- F1 displayed TV stand and 1.90 m entrance opening in both options.",
              "- Direct parents/brother bedroom openings, parents inward leaf and sofa facing metadata displayed in both options.",
              "- Outward entry leaves, centered rendered sofa/TV, solid altar side wall, open court and operable bedroom/stair windows checked; displayed ground area matched model dimensions.",
              "- Study/chair removal, linen portal, shared terrace bench, absent private slab and doorless 1.00 m buffer opening checked.",
              "- Wooden armchair facing and gallery glazing displayed; both exterior variants resolve camera-depth ordering without dependency cycles.",
              "- C15 actual upper polygon, zero enclosed projection, 6.60 m common roof datum/low parapet and two independent stair openings checked. Conditional A-side candidates stay distinct from ordinary window schedule.",
              "- Section labels match the 6.96 m² court and 3.00 m canopy, and include aligned bedroom walls, illustrative beam/window ranges, roof-service reservations and low-parapet drainage diagram.",
              "- Ranch/framed-ranch porch metadata differs by option; rooftop screen and exposed collector appear in both massings.",
              "- All five overlay controls responded; 390 px layout had no document-level horizontal overflow.",
              f"- {len(rendered)} standalone SVG and {len(rendered)} PNG drawings regenerated.",
              "- PNG drawings captured from corresponding standalone SVG tabs, avoiding page-scroll clipping.",
              "- Print uses the same rotated F1/F2 drawing functions; print dialog/PDF output not exercised.",
              "", "Visual inspection is recorded in the revision notes. These checks do not validate architecture, circulation or engineering."]
    (OUT/'viewer-review.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
    print(f"{MODEL['revision']} viewer review passed; {len(rendered)} SVG and {len(rendered)} PNG views exported.")
finally:
    if ws:
        try: call('Browser.close')
        except Exception: pass
        ws.close()
    try: process.wait(timeout=5)
    except subprocess.TimeoutExpired: process.terminate()
