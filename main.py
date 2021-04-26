from hashlib import sha256, md5, sha3_256, sha512
import os

#class Pw:

wort_liste=X

def getpw():
    passwort=input("Tragen")
    return passwort

def saltpw(passwort):
    salt = os.urandom(32)
    passwort=passwort + salt
    return passwort

def hashpw_algorithm(passwort):

    if input == "sha256":
        hashingpw_algorithm = sha256(str(passwort).encode('utf-8'))
    elif input == "md5":
        hashingpw_algorithm = md5(str(passwort).encode('utf-8'))
    elif input == "sha3":
        hashingpw_algorithm = sha3_256(str(passwort).encode('utf-8'))
    elif input == "sha512":
        hashingpw_algorithm = sha512(str(passwort).encode('utf-8'))

    hashingpw_algorithm= hashingpw_algorithm.hexdigest()
    print(hashingpw_algorithm)
    return hashingpw_algorithm

def pw_compare(passwort):
    with open(wort_liste) as LISTE:
        error=1
    return error
