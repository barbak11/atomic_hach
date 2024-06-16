import json

def decoder(bytestring : bytes):
    return json.loads(bytestring.decode('utf8'))