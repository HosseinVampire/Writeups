import socket
host  = "temperance.hackmyvm.eu"
port = 9988
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s : 
    s.connect((host , port ))
    intro = s.recv(1024) #print intro
    print(intro.decode())
    s.send(b'levelx22')
    level = s.recv(1024)
    asci=map(lambda x : chr(int(x)),level.decode().split())  
    s.send(''.join(list(asci)).encode())
    print(s.recv(1024))
    # i code this more compact ...