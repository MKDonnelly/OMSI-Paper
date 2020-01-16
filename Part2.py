def receiveFile(self, pClientSocket, pFileName, pStudentEmail):
    
    # open new file on the server
    lNewFile = self.openNewFileServerSide(pFileName, pStudentEmail)
    #Code omitted for clarity...
