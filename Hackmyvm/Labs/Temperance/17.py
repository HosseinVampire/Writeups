import socket
import base64 
import PIL
from PIL import Image
import io
host  = "temperance.hackmyvm.eu"
port = 9988
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s : 
    s.connect((host , port ))
    intro = s.recv(1024) #print intro
    print(intro.decode())
    s.send(b'levelx17')
    level = s.recv(1024)
    png = base64.b64decode(level.decode())
    pic = Image.open(io.BytesIO(png))
    pixels =pic.getdata()
    answer = ''
    for i in pixels:
        answer = i
    #print(answer[-1]) 
    s.send(str(answer[-1]).encode('utf-8')) 
    flag = s.recv(1024)
    print(flag)