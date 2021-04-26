
from hashlib import sha256, md5, sha3_256, sha512
import os

#class Pw:

def getpw():
    hashingpw=input("Tragen")
    return hashingpw

def saltpw(hashingpw):
    salt = os.urandom(32)
    hashingpw=hashingpw + salt
    return hashingpw

def hashpw_algorithm(hashingpw, input):
    hashingpw_algorithm=sha256(str(hashingpw).encode('utf-8'))
    if input == "sha256":
        hashingpw_algorithm = sha256(str(hashingpw).encode('utf-8'))
    elif input == "md5":
        hashingpw_algorithm = md5(str(hashingpw).encode('utf-8'))
    elif input == "sha3":
        hashingpw_algorithm = sha3_256(str(hashingpw).encode('utf-8'))
    elif input == "sha512":
        hashingpw_algorithm = sha512(str(hashingpw).encode('utf-8'))
    hashingpw_algorithm= hashingpw_algorithm.hexdigest()
    print(hashingpw_algorithm)
    return hashingpw_algorithm

one, two = getpw()
print(type(two))
hashpw_algorithm(one, two)