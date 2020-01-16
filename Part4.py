def receiveFile(self, pClientSocket, pFileName, pStudentEmail):

   #Code omitted for clarity...

   # receive the file
   tmpFile = ''
   while 1:
    # set a timeout for this
    ready = select.select([pClientSocket], [], [], 2)
    if ready[0]:
        lChunkOfFile = pClientSocket.recv(1024)
        tmpFile += lChunkOfFile
            

