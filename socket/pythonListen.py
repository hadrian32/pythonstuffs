import socket
import sys

host = ''
port = 31337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((host,port))
except socket.error as e:
    print (str(e))

s.listen(5) #max incoming connection

conn, addr = s.accept()

print('connected to: '+addr[0]+':'+str(addr[1]))
