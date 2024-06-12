import socket
host  = "temperance.hackmyvm.eu"
port = 9988
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s : 
    s.connect((host , port ))
    intro = s.recv(1024) #print intro
    print(intro.decode())
    s.send(b'levelx14')
    level = s.recv(1024)
    list_level= level.decode().split(' ')
    string , charachter = list_level[0] , list_level[1]
    answer = string.count(charachter)
    answer = str(answer).encode('utf-8')
    s.send(answer)
    flag = s.recv(1024)
    print(flag)