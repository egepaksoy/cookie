import hashlib


def generate(token, serial):
    token = token.encode()
    token = hashlib.sha256(token).hexdigest()
    return token, serial