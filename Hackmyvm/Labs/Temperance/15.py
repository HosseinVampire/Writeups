import socket
host  = "temperance.hackmyvm.eu"
port = 9988
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s : 
    s.connect((host , port ))
    intro = s.recv(1024) #print intro
    print(intro.decode())
    s.send(b'levelx15')
    level = s.recv(1024)
    level = level.decode()
    list_num = level.split(' ')
    list_num =[int(x) for x in list_num]
    sub = list_num[2] - list_num[1] # Find the differece between numbers  
    answer = list_num[-1] + sub  # add the our  number to last index , this is our answer
    answer = str(answer).encode('utf-8')
    s.send(answer)  
    flag =s.recv(1024)  
    print(flag)