import socket
import binascii
host  = "temperance.hackmyvm.eu"
port = 9988
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s : 
    s.connect((host , port ))
    intro = s.recv(1024) #print intro
    print(intro.decode())
    s.send(b'levelx18')
    level = s.recv(1024)
    level = level.decode()  
    answer=''
    for i in level:
        i=bin(ord(i)) # iterate all the charaters in a loop to conver to inter then binary  ; cool way :)
        answer+=i
    answer =answer.replace('b','')  # remove extra b  from start and end of answer
    s.send(answer.encode('utf-8'))
    flag = s.recv(1024)
    print(flag)