import socket
host  = "temperance.hackmyvm.eu" # server 
port = 9988 # port 
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s : 
    s.connect((host , port ))
    intro = s.recv(1024) #print intro
    print(intro.decode())
    s.send(b'levelx20')
    level = s.recv(1024)
    #===================