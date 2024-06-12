import socket

host = "temperance.hackmyvm.eu"
port = 9988

def rot13(sentence):
    rot13 = str.maketrans(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
        'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    )
    return sentence.translate(rot13)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    intro = s.recv(1024)
    print("Intro message:", intro.decode())
    
    s.send(b'levelx09')
    level = s.recv(1024).decode()
    answer = rot13(level)
    s.send(answer.encode('utf-8'))
    flag = s.recv(1024)
    print(flag)