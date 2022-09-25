import base64 


def Encode(Text):
    return Text.encode("ascii")

def Decode(Base64):
    base64_bytes = base64.b64encode(Base64)
    return base64_bytes.decode("ascii")
