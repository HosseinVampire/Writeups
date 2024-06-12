import socket
import requests
import bs4
host  = "temperance.hackmyvm.eu"
port = 9988
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s : 
    s.connect((host , port ))
    intro = s.recv(1024) #print intro
    print(intro.decode())
    s.send(b'levelx25')
    level = s.recv(1024) 
    header= requests.get(level).headers
    s.send(header['Hmv-Code'].encode('utf-8'))
    flag= s.recv(1024)
    print(flag)