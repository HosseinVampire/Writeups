import socket
import jwt
import base64
host  = "temperance.hackmyvm.eu"
port = 9988
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s : 
    s.connect((host , port ))
    intro = s.recv(1024) #print intro
    print(intro.decode())
    s.send(b'levelx28')
    level = s.recv(1024)
    decode= jwt.decode(level , options={'verify_signature':False},algorithms='HS256')
    s.send(decode['HMVKey'].encode('utf-8'))
    flag = s.recv(1024)
    print(flag)