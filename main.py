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
    label_werbung.configure(fg=schriftfarbe)
    radiobutton_1_1.configure(fg=schriftfarbe)
    radiobutton_1_2.configure(fg=schriftfarbe)
    radiobutton_2_1.configure(fg=schriftfarbe)
    radiobutton_2_2.configure(fg=schriftfarbe)
    radiobutton_2_3.configure(fg=schriftfarbe)
    radiobutton_2_4.configure(fg=schriftfarbe)
    button_schriftfarbe.configure(fg=schriftfarbe)
    button_wortliste.configure(fg=schriftfarbe)
    button_hashen.configure(fg=schriftfarbe)
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
    button_hashen.configure(bg=buttfarbe)
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
    label_werbung.configure(bg=farbe)
    radiobutton_1_1.configure(bg=farbe)
    radiobutton_1_2.configure(bg=farbe)
    radiobutton_2_1.configure(bg=farbe)
    radiobutton_2_2.configure(bg=farbe)
    radiobutton_2_3.configure(bg=farbe)
    radiobutton_2_4.configure(bg=farbe)
    entry_eingabefeld.configure(bg=farbe)


def versteckt_klartext():
    wert = verklar.get()
    if wert == 1:
        entry_eingabefeld.configure(show="X")
    elif wert == 2:
        entry_eingabefeld.configure(show="")


def hashpw_algorithm():
    ausgabe.set("")
    if wort_liste != "":
        pw_compare(eingabe.get())
    if hashalgowert.get() == "sha256":
        ausgabe2 = sha256(str(eingabe.get()).encode('utf-8'))
        ausgabe.set(ausgabe2.hexdigest())
    elif hashalgowert.get() == "md5":
        ausgabe2 = md5(str(eingabe.get()).encode('utf-8'))
        ausgabe.set(ausgabe2.hexdigest())
    elif hashalgowert.get() == "sha3":
        ausgabe2 = sha3_256(str(eingabe.get()).encode('utf-8'))
        ausgabe.set(ausgabe2.hexdigest())
    elif hashalgowert.get() == "sha512":
        ausgabe2 = sha512(str(eingabe.get()).encode('utf-8'))
        ausgabe.set(ausgabe2.hexdigest())


def pw_compare(passwort):
    liste = open(wort_liste, "r", encoding="utf-8")
    for passwoerter in liste:
        passwoerter = passwoerter.replace("\n", "")
        if passwoerter == passwort:
            warnung = tk.Tk()
            warnung.title("     Info")
            warnung.geometry("280x120")
            warnung.configure(bg=farbe)
            ausgabe3 = "Ihr Passwort ist in Ihrer Rainbow-Table enthalten"
            label_info = tk.Label(master=warnung, text=ausgabe3, bg=farbe, fg=schriftfarbe)
            label_info.place(x=0, y=0, width=280, height=40)
            button_close = tk.Button(master=warnung, text="Schließen", bg=buttfarbe, fg=schriftfarbe,
                                     command=warnung.destroy)
            button_close.place(x=60, y=50, width=120, height=40)
            break
    liste.close()


# Variablen
fenster = tk.Tk()  # Fenster erstellung
wort_liste = ""  # für den Pfad zur Wortliste
farbe = '#FFFFFF'  # Farbe des Hintergrunds
schriftfarbe = '#000000'  # Farbe der Schrift
buttfarbe = '#D3D3D3'  # Farbe der Buttons
hashalgowert = tk.StringVar()  # Hier wird festgehalten welcher Hashalgoritmus verwendet wird.
verklar = tk.IntVar()  # Wert legt fest, ob das Passwort in Klartext angegeben wird oder nicht
eingabe = tk.StringVar()  # Der Wert der eingeben wurde
ausgabe = tk.StringVar()  # Der Wert der ausgabe

# Fenster
icon = tk.PhotoImage(file='ICON.png')  # Das ICON in der oberen linken Ecke
fenster.title("     Hasher")
fenster.geometry("1280x720")
fenster.iconphoto(False, icon)
fenster.configure(bg=farbe)

# Linie
draw = tk.Canvas(master=fenster, bg=farbe, bd=0, relief="flat", highlightthickness=0)
draw.create_line(1, 0, 1, 720, width=2, dash=(50, 50))
draw.place(x=799, y=0, width=4, height=720)

# Überschrift
label_ueberschrift = tk.Label(master=fenster, bg=farbe, text="Der Hashwert Berechner")
label_ueberschrift.config(font=("Arial", 18))
label_ueberschrift.place(x=60, y=20, width=700, height=40)

# Passwort eingabe feld
entry_eingabefeld = tk.Entry(master=fenster, show="X",
                             textvariable=eingabe,
                             relief="groove", bg=farbe)
entry_eingabefeld.config(font=("Arial", 12))
entry_eingabefeld.place(x=60, y=60, width=700, height=40)

# Passwort oder Klartext
radiobutton_1_1 = tk.Radiobutton(master=fenster, bg=farbe, anchor="nw", text="Versteckte eingabe",
                                 variable=verklar,
                                 value=1,
                                 command=versteckt_klartext)

radiobutton_1_1.config(font=("Arial", 12))
radiobutton_1_1.place(x=60, y=100, width=200, height=40)

radiobutton_1_2 = tk.Radiobutton(master=fenster, bg=farbe, anchor="nw", text="Klartext eingabe",
                                 variable=verklar,
                                 value=2,
                                 command=versteckt_klartext)
radiobutton_1_2.config(font=("Arial", 12))
radiobutton_1_2.place(x=270, y=100, width=200, height=40)

radiobutton_1_1.select()

# Werbung
label_werbung = tk.Label(master=fenster, bg=farbe, fg=schriftfarbe, text="Hier könnte ihre Werbung stehen",
                         relief="sunken")
label_werbung.config(font=("Arial", 24))
label_werbung.place(x=60, y=135, width=700, height=200)

# Ausgabe
label_ausgabe = tk.Label(master=fenster, bg=farbe, relief="groove", anchor="nw", justify="left",
                         textvariable=ausgabe)

label_ausgabe.config(font=("Arial", 12))
label_ausgabe.place(x=60, y=350, width=700, height=220)

# Hashen
button_hashen = tk.Button(master=fenster, bg=buttfarbe, relief="groove", text="Hashen",
                          command=hashpw_algorithm)
button_hashen.place(x=310, y=620, width=220, height=60)

# Einstellungen
label_einstellungen = tk.Label(master=fenster, bg=farbe, text="Einstellungen")
label_einstellungen.config(font=("Arial", 18))
label_einstellungen.place(x=840, y=20, width=400, height=40)

# Wortliste auswählen
button_wortliste = tk.Button(master=fenster, bg="light gray", relief="groove", text="Wortliste auswählen",
                             command=wortliste)

button_wortliste.place(x=840, y=70, width=400, height=40)

# Hintergrundfarbe auswählen
button_hintergrund = tk.Button(master=fenster, bg="light gray", relief="groove", text="Hintergrundfarbe auswählen",
                               command=hintergrund)

button_hintergrund.place(x=840, y=130, width=400, height=40)

# Schriftfarbe auswählen
button_schriftfarbe = tk.Button(master=fenster, bg="light gray", relief="groove", text="Schriftfarbe auswählen",
                                command=schrift)

button_schriftfarbe.place(x=840, y=190, width=400, height=40)

# Buttonfarbe auswählen
button_buttonfarbe = tk.Button(master=fenster, bg="light gray", relief="groove", text="Buttonfarbe auswählen",
                               command=buttonfarbe)

button_buttonfarbe.place(x=840, y=250, width=400, height=40)

# Hashalgoritmus auswählen
label_Hash = tk.Label(master=fenster, bg=farbe, text="Hashalgorithmen")
label_Hash.config(font=("Arial", 15))
label_Hash.place(x=840, y=310, width=400, height=40)

radiobutton_2_1 = tk.Radiobutton(master=fenster, bg=farbe, anchor="w", text="SHA 256",
                                 variable=hashalgowert,
                                 value="sha256")

radiobutton_2_1.config(font=("Arial", 12))
radiobutton_2_1.place(x=860, y=350, width=100, height=40)

radiobutton_2_2 = tk.Radiobutton(master=fenster, bg=farbe, anchor="w", text="SHA 512",
                                 variable=hashalgowert,
                                 value="sha512")

radiobutton_2_2.config(font=("Arial", 12))
radiobutton_2_2.place(x=1060, y=350, width=100, height=40)

radiobutton_2_3 = tk.Radiobutton(master=fenster, bg=farbe, anchor="w", text="MD5",
                                 variable=hashalgowert,
                                 value="md5")

radiobutton_2_3.config(font=("Arial", 12))
radiobutton_2_3.place(x=860, y=400, width=100, height=40)

radiobutton_2_4 = tk.Radiobutton(master=fenster, bg=farbe, anchor="w", text="SHA3 256",
                                 variable=hashalgowert,
                                 value="sha3")

radiobutton_2_4.config(font=("Arial", 12))
radiobutton_2_4.place(x=1060, y=400, width=100, height=40)
radiobutton_2_1.select()

# Pfad zur Wortliste
label_pfadtext = tk.Label(master=fenster, bg=farbe, text="Pfad zur derzeit angewendeten Wortliste:")
label_pfadtext.config(font=('Arial', 15))
label_pfadtext.place(x=840, y=530, width=400, height=40)
label_pfad = tk.Label(master=fenster, bg=farbe)
label_pfad.config(font=('Arial', 12))
label_pfad.place(x=840, y=570, width=400, height=40)

fenster.mainloop()
