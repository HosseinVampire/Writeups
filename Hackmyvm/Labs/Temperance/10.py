import socket  
host  = "temperance.hackmyvm.eu"
port = 9988
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s : 
    s.connect((host , port ))
    intro = s.recv(1024) #print intro
    print(intro.decode())
    s.send(b'levelx10')
    level = s.recv(1024)
    level = str(level)
    nums  = level.replace("b'",'') # removed extra chars
    nums=nums.removesuffix("'") # also remove the suffix 
    nums = nums.split(' ')
    final_list=[]
    for i in nums :
        final_list.append(i)
    final_list.sort()
    answer = ''.join(final_list) # join the numbers togheter 
    s.send(answer.encode('utf-8')) # encode it to utf-8 to be able to send it .
    flag =s.recv(1024)
    print(flag)