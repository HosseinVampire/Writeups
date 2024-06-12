import socket
import base64
import zipfile 
host  = "temperance.hackmyvm.eu"
port = 9988
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s : 
    s.connect((host , port ))
    intro = s.recv(1024) #print intro
    print(intro.decode())
    s.send(b'levelx19')
    level = s.recv(1024)
    zip_file = base64.b64decode(level.decode())
    zip_file  = open('19.zip' , 'wb').write(zip_file)  # save the zip file as 19.zip cuz of number of temperance misson
    zip1 =zipfile.ZipFile('19.zip') 
    zip1.extractall() # extract the zip file   (it contain the txt file called HMV.txt)
    answer = open('HMV.txt' , 'r').readline() # read the string  then we can send it to server to get FLAG .
    s.send(str(answer).encode('utf-8'))
    flag = s.recv(1024)
    print(flag)