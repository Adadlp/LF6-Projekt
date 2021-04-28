from hashlib import sha256, md5, sha3_256, sha512
import os
import tkinter as tk
from tkinter.filedialog import askopenfilename

def Wortliste():
    global wort_liste
    x = os.environ['USERPROFILE'] + "\Desktop"
    wort_liste = askopenfilename(initialdir= x, filetypes =(("Text File", "*.txt"),("All Files","*.*")), title = "Wähle die Passwortliste aus.")

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


#Wichtig
wort_liste = ""
o = Pw()
#Fenster
fenster = tk.Tk()
fenster.title("Test")
fenster.geometry("1280x720")
#Schliess-Button
button1 = tk.Button(master= fenster, bg = "light grey", relief = "groove", text = "Schließen", command = fenster.quit)
button1.place(x = 1160, y = 620, width = 80, height = 80)
button1.pack
#Wortliste auswählen
button2 = tk.Button(master= fenster, bg = "light grey", relief = "groove", text = "Wortliste \n auswählen", command = Wortliste)
button2.place(x = 100, y = 620, width = 80, height = 80)
button2.pack
#Passwort eingabe feld
entry_pass = tk.Entry(master=fenster,show = "*")
entry_pass.place(x = 100, y = 220, width = 200, height = 20)
entry_pass.pack
fenster.mainloop()

