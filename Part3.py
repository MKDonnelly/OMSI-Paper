def openNewFileServerSide(self, pNameOfNewFile, pStudentEmail):

    try:
        #Code omitted for clarity...
        lFilePath = os.path.join(lDirectoryPath, pNameOfNewFile)
        lNewFile = open(lFilePath, 'wb')
