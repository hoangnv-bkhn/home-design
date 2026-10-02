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
chrome=Path('C:/Program Files/Google/Chrome/Application/chrome.exe')
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
                call('Emulation.setDeviceMetricsOverride',{'width':1025,'height':980,'deviceScaleFactor':1,'mobile':False})
                call('Page.navigate',{'url':(OUT/f'option-{opt}-{view}.svg').as_uri()})
                for _ in range(50):
                    if js('document.documentElement.tagName.toLowerCase()==="svg" && document.readyState==="complete"'): break
                    time.sleep(.05)
                else: raise RuntimeError('Standalone SVG did not load')
                js('document.documentElement.setAttribute("width","1025");document.documentElement.setAttribute("height","980")')
                call('Runtime.evaluate',{'expression':'new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve)))','awaitPromise':True})
                shot=call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})
                (OUT/f'option-{opt}-{view}.png').write_bytes(base64.b64decode(shot['data']))
            finally:
                ws=main_ws
                try: call('Target.closeTarget',{'targetId':preview_id})
                finally: preview_ws.close()
    js('document.querySelector(\'[data-view="F1"]\').click();document.querySelector(\'[data-room-id="BR-01"]\').dispatchEvent(new MouseEvent("click"))')
    assert 'BR-01' in js("document.querySelector('#detail').textContent")
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
        js('document.querySelector(\'[data-view="F1"]\').click()')
        # Furniture was toggled off earlier; restore it for this assertion.
        js('document.querySelector("#furniture").checked=true;render()')
        assert js('document.querySelector(\'[data-furniture-name="TV stand"]\')!==null')
        assert js('document.querySelector(\'[data-door-id="ENTRY"]\').getAttribute("data-opening-width")')=='1.9'
    assert not errors, errors
    report = [f"# {MODEL['revision']} viewer review", "", "Headless Chrome local review completed.", "",
              f"- {len(MODEL['options'])} active option / all five views rendered without captured JavaScript exceptions.",
              "- Plot, F1 and F2 declare the 90° clockwise display transform; export metadata matches current revision.",
              "- BR-01 selection and each BAL-01 variant area/access note populated correctly.",
              "- F1 displayed TV stand and 1.90 m entrance opening in both options.",
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
