import socket

HOST = "<OMSI Server IP>"
PORT = <OMSI Server Port>

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send("OMSI0001\x00bigfile.txt\x00me@ucdavis.edu\x0010.0.0.1")
s.close()
