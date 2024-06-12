import socket
import requests
host  = "temperance.hackmyvm.eu"
port = 9988
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s : 
    s.connect((host , port ))
    intro = s.recv(1024) #print intro
    print(intro.decode())
    s.send(b'levelx24')
    level = s.recv(1024)
    #print(level)
    # i want to write this in one line .
    s.send(requests.get(level.decode()).content)
    print(s.recv(1024))