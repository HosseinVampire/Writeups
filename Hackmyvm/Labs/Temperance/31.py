import socket
import base64
import io
from PIL import Image
from pyzbar.pyzbar import decode
host  = "temperance.hackmyvm.eu"
port = 9988
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s : 
    s.connect((host , port ))
    intro = s.recv(1024) #print intro
    print(intro.decode())
    s.send(b'levelx31')
    level = s.recv(1024)
    level = base64.b64decode(level.decode())
    image_qr = Image.open(io.BytesIO(level))
    data = decode(image_qr)  
    data = list(str(data).split(','))
    answer  = data[0][16:-1]
    s.send(str(answer).encode('utf-8'))
    flag = s.recv(1024)
    print(flag)