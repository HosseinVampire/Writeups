import socket 
host  = "temperance.hackmyvm.eu"
port = 9988
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s : 
    s.connect((host , port ))
    intro = s.recv(1024) #print intro
    s.send(b'levelx02')
    level = s.recv(1024)
    level =level.upper() # upper the string 
    s.send(level) # send to server
    flag  = s.recv(1024 ) # flag 
    print(flag)