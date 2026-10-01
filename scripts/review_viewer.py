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
    call('Emulation.setDeviceMetricsOverride',{'width':1600,'height':1500,'deviceScaleFactor':1,'mobile':False})
    call('Page.navigate',{'url':(OUT/'house-concepts.html').as_uri()})
    for _ in range(50):
        if js("document.querySelector('#canvas svg')!==null"): break
        time.sleep(.1)
    else: raise RuntimeError('Viewer did not render')
    for opt in ['01','02']:
        js(f"document.querySelector('#options [data-id=\"{opt}\"]').click()")
        for view in ['site','F1','F2','section','massing']:
            js(f"document.querySelector('[data-view=\"{view}\"]').click()")
            svg=js("document.querySelector('#canvas svg').outerHTML")
            if 'xmlns=' not in svg: svg=svg.replace('<svg ','<svg xmlns="http://www.w3.org/2000/svg" ',1)
            (OUT/f'option-{opt}-{view}.svg').write_text(svg,encoding='utf-8')
            bounds=js("(()=>{const r=document.querySelector('#canvas').getBoundingClientRect();return {x:r.x+scrollX,y:r.y+scrollY,width:r.width,height:r.height,scale:1}})()")
            shot=call('Page.captureScreenshot',{'format':'png','clip':bounds,'captureBeyondViewport':True})
            (OUT/f'option-{opt}-{view}.png').write_bytes(base64.b64decode(shot['data']))
    js("document.querySelector('[data-view=\"F1\"]').click();document.querySelector('.room').dispatchEvent(new MouseEvent('click'))")
    assert 'BR-01' in js("document.querySelector('#detail').textContent")
    for control in ['grid','services','furniture','projection']:
        js(f"document.querySelector('#{control}').click()")
    assert js("document.querySelector('#canvas svg')!==null")
    call('Emulation.setDeviceMetricsOverride',{'width':390,'height':844,'deviceScaleFactor':1,'mobile':False})
    overflow=js('document.documentElement.scrollWidth > innerWidth')
    assert not overflow, 'Mobile layout overflows horizontally'
    assert not errors, errors
    (OUT/'viewer-review.md').write_text('# Viewer review\n\nHeadless Chrome local review completed.\n\n- Both options and all five views rendered without captured JavaScript exceptions.\n- Room selection populated the details panel.\n- Overlay controls responded without errors.\n- 390 px layout had no document-level horizontal overflow.\n- Standalone SVG and PNG previews exported for each option/view.\n\nThis checks the viewer, not architectural or engineering correctness.\n',encoding='utf-8')
    print('Viewer review passed; 10 SVG and 10 PNG views exported.')
finally:
    if ws:
        try: call('Browser.close')
        except Exception: pass
        ws.close()
    try: process.wait(timeout=5)
    except subprocess.TimeoutExpired: process.terminate()
