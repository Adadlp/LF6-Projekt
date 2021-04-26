from hashlib import sha256, md5, sha3_256, sha512
import os
import tkinter

wort_liste = ""
class Fenster:
    '''    def open_Fenster(self):
        Form = tkinter.Tk()
        Form.title = "Test"
        button1 = Form.Button(Form, text="QUIT", fg="red", command = Form.destroy())
        button1.pack
        Form.mainloop()

    def open_File(self):
        Form = tkinter.Tk()
'''

class Pw:
    def getpw(Self):
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

    def pw_compare(passwort, wort_liste):
        ''' Mein Vorschlag
        Liste = open("wort_liste", "r")
        for paswort in Liste:
            error = 1
        return error'''
        '''with open(wort_liste) as LISTE:
            for passwort in LISTE:
            error = 1
            
        return error
        '''

if __name__ == "__main__":
    Fenster.open_Fenster(0)