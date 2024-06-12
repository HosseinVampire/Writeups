import socket
import hashlib
host  = "temperance.hackmyvm.eu"
port = 9988
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s : 
    s.connect((host , port ))
    intro = s.recv(1024) #print intro
    print(intro.decode())
    s.send(b'levelx20')
    level = s.recv(1024)  
                                                            # importing the 50 first words of rockyou disctionary 
    rockyou = '''123456    
12345
123456789
password
iloveyou
princess
1234567
12345678
abc123
nicole
daniel
babygirl
monkey
lovely
jessica
654321
michael
ashley
qwerty
111111
iloveu
000000
michelle
tigger
sunshine
chocolate
password1
soccer
anthony
friends
butterfly
purple
angel
jordan
liverpool
justin
loveme
fuckyou
123123
football
secret
andrea
carlos
jennifer
joshua
bubbles
1234567890
superman
hannah
amanda'''
    rockyou = rockyou.split('\n')  #split the words by the new lines 
    def  brouteforce():
        check = lambda x : hashlib.md5(x.encode('utf-8')) #  lambda to get each word and convert them to md5 
        for i in  rockyou:
            if check(i).hexdigest()  == level.decode() : # check if the hashed word is same with mission string 
                print(f'found the answer : {i}')  # the if condition only works if we found the right answer
                answer = i
                s.send(answer.encode('utf-8'))
                flag = s.recv(1024) 
                print(flag)
            else:
                pass
    brouteforce()