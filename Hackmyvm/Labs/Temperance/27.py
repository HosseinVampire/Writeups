import socket
import requests
import bs4
host  = "temperance.hackmyvm.eu"
port = 9988
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s : 
    s.connect((host , port ))
    intro = s.recv(1024) #print intro
    print(intro.decode())
    s.send(b'levelx27')
    level = s.recv(1024)
    data = requests.get(level).content.decode()
    list_users_data= data.split('\n')
    for i in list_users_data :
        if  'proxy' in i :
            rightuser= i 
            uuid=rightuser.split(':')
            s.send(uuid[2].encode('utf-8'))
            flag=s.recv(1024)
            print(flag)
            break
        else :
            pass
