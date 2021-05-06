from hashlib import sha256, md5, sha3_256, sha512
import os
import tkinter as tk
from tkinter.filedialog import askopenfilename

def wortliste():
    global wort_liste
    x = os.environ['USERPROFILE'] + "\Desktop"
    wort_liste = askopenfilename(initialdir= x, filetypes =(("Text File", "*.txt"),("All Files","*.*")), title = "Wähle die Passwortliste aus.")
    pflabel.configure(text = wort_liste)

def hintergrund():
    None

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
hintergd = '#FFFFFF'

#Fenster
fenster = tk.Tk()
icon = tk.PhotoImage(file = 'ICON.png')
fenster.title("     Hasher / Dehasher")
fenster.geometry("1280x720")
fenster.iconphoto(False, icon)
fenster.configure(bg = hintergd)
#wichtig 2

# Hash oder dehash
button1p1 = tk.Button(master = fenster, bg = "light grey", relief = "groove", text = "Wortliste \n auswählen", command = wortliste)
button1p1.place(x = 100, y = 620, width = 80, height = 80)
button1p1.pack

button1p2 = tk.Button(master = fenster, bg = "light grey", relief = "groove", text = "Wortliste \n auswählen", command = wortliste)
button1p2.place(x = 100, y = 620, width = 80, height = 80)
button1p2.pack
#Wortliste auswählen
button2 = tk.Button(master = fenster, bg = "light gray", relief = "groove", text = "Wortliste auswählen", command = wortliste)
button2.place(x = 840, y = 70, width = 400, height = 40)
button2.pack

#Passwort eingabe feld
eingabefeld = tk.Entry(master = fenster,show = "*")
eingabefeld.place(x = 100, y = 220, width = 200, height = 20)
eingabefeld.pack
#Ausgabe
ausgabelabel = tk.Label(master= fenster, )

#Einstellungen
einstelllabel = tk.Label(master = fenster, bg = hintergd, text = "Einstellungen")
einstelllabel.place(x = 840, y = 20, width = 400, height = 40)
einstelllabel.config(font = ("Arial", 18))
einstelllabel.pack
#Pfad zur Wortliste
plabel = tk.Label(master = fenster, bg = hintergd, text = "Pfad zur derzeit angewendeten Wortliste:")
plabel.place(x = 840, y = 530, width = 400, height = 40)
plabel.config(font = ('Arial', 15))
plabel.pack

pflabel = tk.Label(master = fenster, bg = hintergd)
pflabel.place(x = 840, y = 570, width = 400, height = 40)
pflabel.config(font = ('Arial', 12))
pflabel.pack

#Hintergrundfarbe auswählen
button3 = tk.Button(master = fenster, bg = "light gray", relief = "groove", text = "Hintergrundfarbe auswählen", command = hintergrund)
button3.place(x = 840, y = 130, width = 400, height = 40)
button3.pack
#Linie
#draw = tk.Canvas(master = fenster)
#draw.create_line(800, 0, 800, 180, width = 2)
#draw.pack()
fenster.mainloop()

