import socket 
host  = "temperance.hackmyvm.eu"
port = 9988
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s : 
    s.connect((host , port ))
    intro = s.recv(1024) #print intro
    s.send(b'levelx04')
    level = s.recv(1024)
    s.send(level[::-1]) #reversed 
    flag = s.recv(1024) # flag  
    print(flag)