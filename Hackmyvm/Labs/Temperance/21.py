import socket
host  = "temperance.hackmyvm.eu"
port = 9988
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s : 
    s.connect((host , port ))
    intro = s.recv(1024) #print intro
    print(intro.decode())
    s.send(b'levelx21')
    level = s.recv(1024)
    level = level.decode()
    level=  int(level)/1024
    s.send(f'{level:.2f}KB'.encode())
    flag = s.recv(1024)
    print(flag)