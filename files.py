import base64 

def Encode(FilePath, Output):
    with open(FilePath, 'rb') as imagefile:
        byteform = base64.b64encode(imagefile.read())
    
    f = open(Output, 'wb')
    f.write(byteform)
    f.close()

def Decode(FilePath, Output):
    file = open(FilePath, 'rb')
    byte = file.read()

    fh = open(Output, 'wb')
    fh.write(base64.b64decode((byte)))
    fh.close()

