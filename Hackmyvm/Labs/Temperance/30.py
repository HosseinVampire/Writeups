import socket
import xor_cipher
host  = "temperance.hackmyvm.eu"
port = 9988
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s : 
    s.connect((host , port ))
    intro = s.recv(1024) #print intro
    print(intro.decode())
    s.send(b'levelx30')
    level = s.recv(1024)
    def xor_encrypt(input_str, key):
        key_length = len(key)
        output = []
        
        for i, char in enumerate(input_str):
            xor_result = ord(char) ^ ord(key[i % key_length])
            output.append(chr(xor_result))
        return ''.join(output)
    input_str = level.decode() 
    key = "HMV"
    output_str = xor_encrypt(input_str, key)
    s.send(output_str.encode('utf-8'))
    flag = s.recv(1024)
    print(flag)