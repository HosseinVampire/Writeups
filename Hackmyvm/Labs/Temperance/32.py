import socket
import hashlib
from itertools import permutations

host  = "temperance.hackmyvm.eu" # server 
port = 9988 # port 
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s : 
    s.connect((host , port ))
    intro = s.recv(1024) #print intro
    print(intro.decode())
    s.send(b'levelx32')
    level = s.recv(1024)
            
    def find_matching_permutation(md5_hash, input_string):
        # Generate all possible permutations of the input string
        for perm in permutations(input_string):
            perm_str = ''.join(perm)
            # Calculate the MD5 hash of the current permutation
            perm_md5 = hashlib.md5(perm_str.encode()).hexdigest()
            # Compare the calculated MD5 hash with the given MD5 hash
            if perm_md5 == md5_hash:
                return perm_str
        return None

    # Example usage:
    md5_hash = level.decode().split()[0]
    input_string = level.decode().split()[1]
    result = find_matching_permutation(md5_hash, input_string)
    s.send(result.encode('utf-8'))
    flag = s.recv(1024)
    print(flag)