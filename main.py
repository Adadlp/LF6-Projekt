from hashlib import sha256, md5, sha3_256, sha512
import os
import tkinter as tk
from tkinter.filedialog import askopenfilename
import tkcolorpicker

def wortliste():
    global wort_liste
    x = str(os.environ['USERPROFILE'] + "\Desktop")
    wort_liste = askopenfilename(initialdir=x,
                                 filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
                                 title="Wähle die Passwortliste aus.")
    label_pfad.configure(text=wort_liste)

def schrift():
    global schriftfarbe
    schriftfarben = tkcolorpicker.askcolor(color=schriftfarbe,
                                           parent=fenster)
    schriftfarbe = str(schriftfarben[1])
    label_pfadtext.configure(fg=schriftfarbe)
    label_pfad.configure(fg=schriftfarbe)
    label_einstellungen.configure(fg=schriftfarbe)
    label_Hash.configure(fg=schriftfarbe)
    label_ausgabe.configure(fg=schriftfarbe)
    label_ueberschrift.configure(fg=schriftfarbe)
    radiobutton_1_1.configure(fg=schriftfarbe)
    radiobutton_1_2.configure(fg=schriftfarbe)
    radiobutton_2_1.configure(fg=schriftfarbe)
    radiobutton_2_2.configure(fg=schriftfarbe)
    radiobutton_2_3.configure(fg=schriftfarbe)
    radiobutton_2_4.configure(fg=schriftfarbe)
    button_schriftfarbe.configure(fg=schriftfarbe)
    button_wortliste.configure(fg=schriftfarbe)
    button_de_hash_2.configure(fg=schriftfarbe)
    button_de_hash_1.configure(fg=schriftfarbe)
    button_hintergrund.configure(fg=schriftfarbe)
    button_buttonfarbe.configure(fg=schriftfarbe)
    entry_eingabefeld.configure(fg=schriftfarbe)

def buttonfarbe():
    global buttfarbe
    bfarben = tkcolorpicker.askcolor(color=buttfarbe,
                                     parent=fenster)
    buttfarbe = str(bfarben[1])
    button_schriftfarbe.configure(bg=buttfarbe)
    button_wortliste.configure(bg=buttfarbe)
    button_de_hash_2.configure(bg=buttfarbe)
    button_de_hash_1.configure(bg=buttfarbe)
    button_hintergrund.configure(bg=buttfarbe)
    button_buttonfarbe.configure(bg=buttfarbe)

def hintergrund():
    global farbe
    farbe2 = tkcolorpicker.askcolor(color=farbe,
                                    parent=fenster)
    farbe = str(farbe2[1])
    fenster.configure(bg=farbe)
    draw.configure(bg=farbe)
    label_pfadtext.configure(bg=farbe)
    label_pfad.configure(bg=farbe)
    label_einstellungen.configure(bg=farbe)
    label_Hash.configure(bg=farbe)
    label_ausgabe.configure(bg=farbe)
    label_ueberschrift.configure(bg=farbe)
    radiobutton_1_1.configure(bg=farbe)
    radiobutton_1_2.configure(bg=farbe)
    radiobutton_2_1.configure(bg=farbe)
    radiobutton_2_2.configure(bg=farbe)
    radiobutton_2_3.configure(bg=farbe)
    radiobutton_2_4.configure(bg=farbe)
    entry_eingabefeld.configure(bg=farbe)

def passwort_hex():
    test = int(passhex.get())
    if test == 1:
        button_de_hash_2.place_forget()
        button_de_hash_1.place(x=310,
                               y=620,
                               width=220,
                               height=60)
        entry_eingabefeld.configure(show="*")
    elif test == 2:
        button_de_hash_1.place_forget()
        button_de_hash_2.place(x=310,
                               y=620,
                               width=220,
                               height=60)
        entry_eingabefeld.configure(show="")



class Pw:

    def saltpw(eingabe):
        salt = os.urandom(32)
        ausgabe = eingabe + salt
        return ausgabe

    def hashpw_algorithm(eingabe):

        if hashalgowert == "sha256":
            ausgabe = sha256(str(eingabe).encode('utf-8'))
        elif hashalgowert == "md5":
            ausgabe = md5(str(eingabe).encode('utf-8'))
        elif hashalgowert == "sha3":
            ausgabe = sha3_256(str(eingabe).encode('utf-8'))
        elif hashalgowert == "sha512":
            ausgabe = sha512(str(eingabe).encode('utf-8'))

        ausgabe = ausgabe.hexdigest()
        return ausgabe

    def pw_compare(eingabe, wort_liste):
        None

# Mein Vorschlag
# Liste = open("wort_liste", "r")
# for paswort in Liste:
#     error = 1
# return error
# with open(wort_liste) as LISTE:
#     for passwort in LISTE:
#     error = 1
#
# return error

# Variablen
fenster = tk.Tk() #Fenster erstellung
wort_liste = "" #für den Pfad zur Wortliste
o = Pw() #die andere Klasse abgekürzt
farbe = '#FFFFFF' #Farbe des Hintergrunds
schriftfarbe = '#000000' #Farbe der Schrift
buttfarbe = '#D3D3D3' #Farbe der Buttons
hashalgowert = tk.StringVar() #Hier wird festgehalten welcher Hashalgoritmus verwendet wird.
passhex = tk.StringVar() #Wert legt fest, ob die eingabe ein Passwort oder ein Hashwert ist
eingabe = tk.StringVar() #Der Wert der eingeben wurde
ausgabe = tk.StringVar() #Der Wert der ausgabe

# Fenster
#icon = tk.PhotoImage(file='ICON.png') #Das ICON in der oberen linken Ecke
fenster.title("     Hasher / Dehasher")
fenster.geometry("1280x720")
#fenster.iconphoto(False, icon)
fenster.configure(bg=farbe)



# Linie
draw = tk.Canvas(master=fenster,bg=farbe,bd=0,relief="flat",highlightthickness=0)
draw.create_line(1,0,1,720,width=2,dash=(50, 50))
draw.place(x=799,y=0,width=4,height=720)



# Überschrift
label_ueberschrift = tk.Label(master=fenster,bg=farbe,text="Überschrift")
label_ueberschrift.config(font=("Arial", 18))
label_ueberschrift.place(x=60,y=20,width=700,height=40)



# Hash oder dehash
button_de_hash_1 = tk.Button(master=fenster,bg=buttfarbe,relief="groove",text="Hash",
                             command=o.hashpw_algorithm())

button_de_hash_1.place(x=310,y=620,width=220,height=60)

button_de_hash_2 = tk.Button(master=fenster,bg=buttfarbe,relief="groove",text="Dehash",command="")

button_de_hash_2.place(x=310,y=620,width=220,height=60)
button_de_hash_2.place_forget()



# Hash oder Passwort
radiobutton_1_1 = tk.Radiobutton(master=fenster,bg=farbe,anchor="nw",text="Passwort eingabe",
                                 variable=passhex,
                                 value=1,
                                 command=passwort_hex)

radiobutton_1_1.config(font=("Arial", 12))
radiobutton_1_1.place(x=60,y=280,width=200,height=40)

radiobutton_1_2 = tk.Radiobutton(master=fenster,bg=farbe,anchor="nw",text="Hexadezimal eingabe",
                                 variable=passhex,
                                 value=2,
                                 command=passwort_hex)

radiobutton_1_2.config(font=("Arial", 12))
radiobutton_1_2.place(x=270,y=280,width=200,height=40)
radiobutton_1_1.select()



# Passwort eingabe feld
entry_eingabefeld = tk.Entry(master=fenster,show="*",
                             textvariable=eingabe,
                             relief="groove",bg=farbe)
entry_eingabefeld.place(x=60,y=60,width=700,height=220)



# Ausgabe
label_ausgabe = tk.Label(master=fenster,bg=farbe,relief="groove",anchor="nw",justify="left",
                         textvariable=ausgabe)

label_ausgabe.config(font=("Arial", 12))
label_ausgabe.place(x=60,y=350,width=700,height=220)



# Einstellungen
label_einstellungen = tk.Label(master=fenster,bg=farbe,text="Einstellungen")
label_einstellungen.config(font=("Arial", 18))
label_einstellungen.place(x=840,y=20,width=400,height=40)



# Wortliste auswählen
button_wortliste = tk.Button(master=fenster,bg="light gray",relief="groove",text="Wortliste auswählen",
                             command=wortliste)

button_wortliste.place(x=840,y=70,width=400,height=40)



# Hintergrundfarbe auswählen
button_hintergrund = tk.Button(master=fenster,bg="light gray",relief="groove",text="Hintergrundfarbe auswählen",
                               command=hintergrund)

button_hintergrund.place(x=840,y=130,width=400,height=40)



# Schriftfarbe auswählen
button_schriftfarbe = tk.Button(master=fenster,bg="light gray",relief="groove",text="Schriftfarbe auswählen",
                                command=schrift)

button_schriftfarbe.place(x=840,y=190,width=400,height=40)



# Buttonfarbe auswählen
button_buttonfarbe = tk.Button(master=fenster,bg="light gray",relief="groove",text="Buttonfarbe auswählen",
                               command=buttonfarbe)

button_buttonfarbe.place(x=840,y=250,width=400,height=40)



# Hashalgoritmus auswählen
label_Hash = tk.Label(master=fenster,bg=farbe,text="Hashalgorithmen")
label_Hash.config(font=("Arial", 15))
label_Hash.place(x=840,y=310,width=400,height=40)

radiobutton_2_1 = tk.Radiobutton(master=fenster,bg=farbe,anchor="w",text="SHA 256",
                                 variable=hashalgowert,
                                 value="sha256")

radiobutton_2_1.config(font=("Arial", 12))
radiobutton_2_1.place(x=860,y=350,width=100,height=40)

radiobutton_2_2 = tk.Radiobutton(master=fenster,bg=farbe,anchor="w",text="SHA 512",
                                 variable=hashalgowert,
                                 value="sha512")

radiobutton_2_2.config(font=("Arial", 12))
radiobutton_2_2.place(x=1060,y=350,width=100,height=40)

radiobutton_2_3 = tk.Radiobutton(master=fenster,bg=farbe,anchor="w",text="MD5",
                                 variable=hashalgowert,
                                 value="md5")

radiobutton_2_3.config(font=("Arial", 12))
radiobutton_2_3.place(x=860,y=400,idth=100,height=40)

radiobutton_2_4 = tk.Radiobutton(master=fenster,bg=farbe,anchor="w",text="SHA3 256",
                                 variable=hashalgowert,
                                 value="sha3")

radiobutton_2_4.config(font=("Arial", 12))
radiobutton_2_4.place(x=1060,y=400,width=100,height=40)
radiobutton_2_1.select()



# Pfad zur Wortliste
label_pfadtext = tk.Label(master=fenster,bg=farbe,text="Pfad zur derzeit angewendeten Wortliste:")
label_pfadtext.config(font=('Arial', 15))
label_pfadtext.place(x=840,y=530,width=400,height=40)
label_pfad = tk.Label(master=fenster,bg=farbe)
label_pfad.config(font=('Arial', 12))
label_pfad.place(x=840,y=570,width=400,height=40)

fenster.mainloop()
