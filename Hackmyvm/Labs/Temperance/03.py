import socket 
import base64
host  = "temperance.hackmyvm.eu"
port = 9988
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s : 
    s.connect((host , port ))
    intro = s.recv(1024) #print intro
    s.send(b'levelx03')
    level = s.recv(1024)
    dcode = base64.b64decode(level) # decrypt the base64 to ascii 
    s.send(dcode)
    flag = s.recv(1024) # flag
    print(flag)
