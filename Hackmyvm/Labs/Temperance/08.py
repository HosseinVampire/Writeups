import socket 
host  = "temperance.hackmyvm.eu"
port = 9988
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s : 
    s.connect((host , port ))
    intro = s.recv(1024) #print intro
    s.send(b'levelx08')
    level = s.recv(1024)
    level = level.split(b' ') # split the numbers and put them in a list as strings 
    sum = int(level[0]) + int(level[1]) # get sum of the numbers of each list index and conver the string to intgers 
    sum = str(sum) 
    sum = sum.encode('utf-8') # encode it to utf-8 to make able to send the server 
    s.send(sum)
    flag = s.recv(1024) # Flag 
    print(flag)