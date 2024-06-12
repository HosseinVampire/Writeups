import socket
from PIL import Image
import io
import base64
import pytesseract
host  = "temperance.hackmyvm.eu"
port = 9988
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s : 
    s.connect((host , port ))
    intro = s.recv(1024) #print intro
    print(intro.decode())
    s.send(b'levelx26')
    level = s.recv(1024)
    image = io.BytesIO(base64.b64decode(level.decode()))
    image = Image.open(image)
    nums = pytesseract.image_to_string(image)
    s.send(nums.encode('utf-8'))
    flag = s.recv(1024)
    print(flag)