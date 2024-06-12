import socket  
import re

from geopy.distance import geodesic

HOST = "temperance.hackmyvm.eu"  
PORT = 9988  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  
    s.connect((HOST, PORT))  
  
    print('Receiving Intro')  
    data = s.recv(1024)  
    print(data.decode() if data else "No data received")  
  
    s.sendall(b'levelx29')  
    
    print('Receiving challenge.')  
    data2 = s.recv(1024)  
    print(data2.decode() if data2 else "No challenge received")  

    a = data2.decode()
    b = re.findall('[0-9]+',a)
    lat1 = int(b[0])
    lon1 = int(b[1])
    lat2 = int(b[2])
    lon2 = int(b[3])

    distance = geodesic((lat1,lon1), (lat2,lon2)).kilometers
    solution =  "{:.3f}".format(distance)
    s.sendall(solution.encode())  
  
    print('Receiving flag.')  
    data3 = s.recv(1024)  
    print(data3.decode() if data3 else "No flag received")
    #HMV{wh3r314ml0st}
    