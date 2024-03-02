import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import csv

# Lista delle scelte possibili per le due colonne
colonna1_scelte = ["uomo", "donna", "bambino", "neonato", "no"]
colonna2_scelte = ["bianco", "di colore", "asiatico dell'ovest", "asiatico dell'est", "no"]

# Lista delle immagini mostrate in precedenza
immagini_mostrate = []

# Variabile globale per contenere il percorso dell'immagine corrente
nuova_immagine = ""

def mostra_immagine_casuale():
    global immagini_mostrate
    global nuova_immagine  # Aggiungi questa riga per rendere la variabile accessibile globalmente

    # Lista di tutte le immagini disponibili
    immagini_disponibili = [
        "/Users/newmac/Documents/PROG/Pythone/aimmagini/immagine1.png",
        "/Users/newmac/Documents/PROG/Pythone/aimmagini/immagine2.png",
        "/Users/newmac/Documents/PROG/Pythone/aimmagini/immagine3.png"
        # Aggiungi altre immagini se necessario
    ]

    # Rimuovi le immagini già mostrate dalla lista delle immagini disponibili
    immagini_disponibili = [img for img in immagini_disponibili if img not in immagini_mostrate]

    # Controlla se ci sono ancora immagini disponibili
    if len(immagini_disponibili) == 0:
        messagebox.showinfo("Fine", "Hai esaurito tutte le immagini disponibili!")
        return

    # Scegliere una nuova immagine casuale dalla lista delle immagini disponibili
    nuova_immagine = random.choice(immagini_disponibili)

    # Carica l'immagine e visualizzala nell'interfaccia
    image = Image.open(nuova_immagine)
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)  # Aggiorna questa riga per visualizzare l'immagine sul canvas
    canvas.image = photo

    # Aggiungi l'immagine mostrata alla lista delle immagini mostrate in precedenza
    immagini_mostrate.append(nuova_immagine)

    # Abilita i bottoni per le scelte
    for button in buttons_colonna1:
        button.config(state="normal")
    for button in buttons_colonna2:
        button.config(state="normal")

def salva_scelte():
    global nuova_immagine  # Aggiungi questa riga per rendere la variabile accessibile globalmente

    # Ottieni le scelte dell'utente
    tipo_scelto = colonna1.get()
    etnia_scelta = colonna2.get()

    # Salva i dati nel file CSV
    with open('/Users/newmac/Documents/PROG/Pythone/aimmagini/scelte.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nuova_immagine, tipo_scelto, etnia_scelta])

    # Mostra un messaggio di conferma
    messagebox.showinfo("Conferma", "Le tue scelte sono state salvate correttamente!")

    # Mostra una nuova immagine
    mostra_immagine_casuale()

def crea_interfaccia():
    global nuova_immagine  # Aggiungi questa riga per rendere la variabile accessibile globalmente

    # Creazione dei bottoni per la colonna 1
    for button in buttons_colonna1:
        button.destroy()
    buttons_colonna1.clear()
    for scelta in colonna1_scelte:
        button = tk.Radiobutton(canvas, text=scelta, variable=colonna1, value=scelta)
        buttons_colonna1.append(button)
        canvas.create_window(50, 50 + colonna1_scelte.index(scelta) * 30, anchor=tk.W, window=button)

    # Creazione dei bottoni per la colonna 2
    for button in buttons_colonna2:
        button.destroy()
    buttons_colonna2.clear()
    for scelta in colonna2_scelte:
        button = tk.Radiobutton(canvas, text=scelta, variable=colonna2, value=scelta)
        buttons_colonna2.append(button)
        canvas.create_window(200, 50 + colonna2_scelte.index(scelta) * 30, anchor=tk.W, window=button)

    # Bottone per salvare le scelte
    salva_button = tk.Button(canvas, text="Salva Scelte", command=salva_scelte)
    canvas.create_window(150, 50 + len(colonna1_scelte) * 30, anchor=tk.W, window=salva_button)

# Creazione dell'interfaccia grafica
root = tk.Tk()
root.title("Scelta Immagini")
root.geometry("500x400")

# Creazione del frame scorrevole per l'immagine e i bottoni
frame_scroller = tk.Frame(root)
frame_scroller.pack(expand=True, fill=tk.BOTH)

# Aggiunta della scrollbar verticale al frame scorrevole
scrollbar = tk.Scrollbar(frame_scroller, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Creazione di un Canvas all'interno del frame scorrevole per contenere l'immagine e i bottoni
canvas = tk.Canvas(frame_scroller, yscrollcommand=scrollbar.set)
canvas.pack(expand=True, fill=tk.BOTH)

# Inizializzazione delle variabili per le scelte
colonna1 = tk.StringVar()
colonna2 = tk.StringVar()

# Creazione dei bottoni e del pulsante di conferma iniziali
buttons_colonna1 = []
buttons_colonna2 = []
crea_interfaccia()

# Mostra la prima immagine all'avvio
mostra_immagine_casuale()

# Imposta la scrollbar per consentire lo scorrimento verticale
scrollbar.config(command=canvas.yview)

# Esegui la finestra
root.mainloop()