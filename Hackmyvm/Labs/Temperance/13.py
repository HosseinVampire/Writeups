import socket
host  = "temperance.hackmyvm.eu"
port = 9988
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s : 
    s.connect((host , port ))
    intro = s.recv(1024) #print intro
    print(intro.decode())
    s.send(b'levelx13')
    level = s.recv(1024)    
    level=level.decode()
    level=str(level)
    level =level[1:-1] # removing extra "[" "]" 
    list_strings= level.split(' ') 
    answer = sorted(list_strings)[-1] # Sorted func for sort alphabaticaly strings .  [-1] >>> for last index 
    answer=  answer.encode('utf-8') # encode it to be able to send 
    s.send(answer) # send answer to server 
    flag = s.recv(1024)   # This is flag 
    print(flag)