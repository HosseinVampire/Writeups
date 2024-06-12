import socket
import base64
import io 
from PIL import Image
host  = "temperance.hackmyvm.eu"
port = 9988
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s : 
    s.connect((host , port ))
    intro = s.recv(1024) #print intro
    print(intro.decode())
    s.send(b'levelx23')
    level = s.recv(1024)
    image = base64.b64decode(level.decode())
    pixels=  list(Image.open(io.BytesIO(image)).getdata())
    # print the pixels then show u the pixels  , we need last index of each tuple 
    lastpixels= map(lambda x : chr(x[-1]),pixels)
    s.send(''.join(lastpixels).encode('utf-8')) 
    flag = s.recv(1024)
    print(flag ) # FLAG