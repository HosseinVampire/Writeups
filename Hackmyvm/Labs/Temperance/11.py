# test FILE 
import socket
host  = "temperance.hackmyvm.eu"
port = 9988
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s : 
    s.connect((host , port ))
    intro = s.recv(1024) #print intro
    print(intro.decode())
    s.send(b'levelx11')
    level = s.recv(1024)
    level = str(level).removeprefix("b'")
    level = level.removesuffix("'").split(' ')
    temp_str='....'
    morse_dict={           # conver morse alphabet to ascii
        '.-':'A',
       '-...':'B',
        '-.-.':'C',
        '-..':'D',
        '.':'E',
        '..-.':'F',
        '--.':'G',
        '....':'H',
        '..':'I',
        '.---':'J',
        '-.-':'K',
        '.-..':'L',
        '--':'M',
        '-.':'N',
        '---':'O',
        '.--.':'P',
        '--.-':'Q',
        '.-.':'R',
        '...':'S',
        '-':'T',
        '..-':'U',
        '...-':'V',
        '.--':'W',
        '-..-':'X',
        '-.--':'Y',
        '--..':'Z',
        '.----':'1',
        '..---':'2',
        '...--':'3',
        '....-':'4',
        '.....':'5',
    }
    def decode(morse):
        text =morse_dict.get(morse)
        return text
    answer = ''
    for i in level :
        answer += decode(i)
    answer =answer.encode('utf-8')
    s.send(answer) # send the asnwer to server
    flag=s.recv(1024) # recive the flag
    print(flag) 