import socket
host  = "temperance.hackmyvm.eu"
port = 9988
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s : 
    s.connect((host , port ))
    intro = s.recv(1024) #print intro
    print(intro.decode())
    s.send(b'levelx12')
    level = s.recv(1024)
    level = str(level).split(' ')
    string , rep = level[0] , level[1]
    string = string.removeprefix("b'")
    rep = rep.removesuffix("'")
    rep = int(rep)
    answer = string*rep
    answer=answer.encode('utf-8')
    s.send(answer)
    flag = s.recv(1024)
    print(flag)