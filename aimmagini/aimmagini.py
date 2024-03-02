import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import csv

# Lista delle scelte possibili per le due colonne
colonna1_scelte = ["uomo", "donna", "bambino", "neonato", "no"]
colonna2_scelte = ["bianco", "di colore", "asiatico dell'ovest", "asiatico dell'est", "no"]

def mostra_immagine_casuale():
    # Scegliere una nuova immagine in modo casuale (sostituire con il tuo metodo per ottenere le immagini)
    # Esempio: immagini_casuali = ["immagine1.jpg", "immagine2.jpg", ...]
    immagini_casuali = ["/Users/newmac/Documents/PROG/Pythone/aimmagini/immagini/images(1).png", "/Users/newmac/Documents/PROG/Pythone/aimmagini/immagini/images(1).png", "/Users/newmac/Documents/PROG/Pythone/aimmagini/immagini/images(1).png"]
    nuova_immagine = random.choice(immagini_casuali)

    # Carica l'immagine e visualizzala nell'interfaccia
    image = Image.open(nuova_immagine)
    photo = ImageTk.PhotoImage(image)
    canvas.config(image=photo)
    canvas.image = photo

    # Abilita i bottoni per le scelte
    for button in buttons_colonna1:
        button.config(state="normal")
    for button in buttons_colonna2:
        button.config(state="normal")

def salva_scelte():
    # Ottieni le scelte dell'utente
    tipo_scelto = colonna1.get()
    etnia_scelta = colonna2.get()

    # Salva i dati nel file CSV
    with open('/Users/newmac/Documents/PROG/Pythone/aimmagini/scelte.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([immagine_corrente, tipo_scelto, etnia_scelta])

    # Mostra un messaggio di conferma
    messagebox.showinfo("Conferma", "Le tue scelte sono state salvate correttamente!")

    # Mostra una nuova immagine
    mostra_immagine_casuale()

# Creazione dell'interfaccia grafica
root = tk.Tk()
root.title("Scelta Immagini")
root.geometry("500x400")

# Caricamento dell'immagine iniziale (sostituire con il percorso dell'immagine desiderata)
image = Image.open("/Users/newmac/Documents/PROG/Pythone/aimmagini/immagini/images(1).png")
photo = ImageTk.PhotoImage(image)
canvas = tk.Label(root, image=photo)
canvas.pack()

# Inizializzazione delle variabili per le scelte
immagine_corrente = "/Users/newmac/Documents/PROG/Pythone/aimmagini/immagini/images(1).png"
colonna1 = tk.StringVar()
colonna2 = tk.StringVar()

# Creazione dei bottoni per la colonna 1
buttons_colonna1 = []
for scelta in colonna1_scelte:
    button = tk.Radiobutton(root, text=scelta, variable=colonna1, value=scelta)
    buttons_colonna1.append(button)
    button.pack()

# Creazione dei bottoni per la colonna 2
buttons_colonna2 = []
for scelta in colonna2_scelte:
    button = tk.Radiobutton(root, text=scelta, variable=colonna2, value=scelta)
    buttons_colonna2.append(button)
    button.pack()

# Bottone per salvare le scelte
salva_button = tk.Button(root, text="Salva Scelte", command=salva_scelte)
salva_button.pack()

# Mostra la prima immagine all'avvio
mostra_immagine_casuale()

# Esegui la finestra
root.mainloop()