import socket
import base64
from PIL import Image
host  = "temperance.hackmyvm.eu"
port = 9988
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s : 
    s.connect((host , port ))
    intro = s.recv(1024) #print intro
    print(intro.decode())
    s.send(b'levelx16')
    level = s.recv(1024)
    png =base64.b64decode(level.decode()) #  decode the string fro "base64" to PNG bytes
    png_file = open('16.png' , 'wb').write(png) # Save the raw image to our local machine 
    picture = Image.open('16.png')  #
    answer= f'{picture.width}x{picture.height}' # the answer 
    answer= answer.encode('utf-8')
    s.send(answer) # send it to server 
    flag = s.recv(1024)
    print(flag)