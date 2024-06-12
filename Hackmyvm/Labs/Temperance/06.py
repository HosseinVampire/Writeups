import socket 
import encodings
host  = "temperance.hackmyvm.eu"
port = 9988
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s : 
    s.connect((host , port ))
    intro = s.recv(1024) #print intro
    s.send(b'levelx06')
    level = s.recv(1024)
    length_str = str(len(level))
    length_byte= length_str.encode('utf-8') # convert out len to byte like for make it able to send
    s.send(length_byte) # send
    flag = s.recv(1024) # flag
    print(flag)