import socket 
import binascii # i used binascii module to 
host  = "temperance.hackmyvm.eu"
port = 9988
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s : 
    s.connect((host , port ))
    intro = s.recv(1024) #print intro
    s.send(b'levelx07')
    level = s.recv(1024)
    decoded=binascii.unhexlify(level)
    s.send(decoded) # send decoded hex to server
    flag =s.recv(1024) # recive the answer
    print(flag) # flag