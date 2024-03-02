import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import csv
from io import BytesIO
from google_images_search import GoogleImagesSearch
from urllib.parse import quote
import os
import json

# Lista delle scelte possibili per le due colonne
colonna1_scelte = ["uomo", "donna", "bambino", "bambina", "neonato", "piú persone", "persona disegnata/anime", "persone disegnate/anime", "no"]
colonna2_scelte = ["bianco/a","albino","di colore", "asiatico/a dell'ovest", "asiatico/a dell'est", "varie etnie", "no"]

# Lista delle immagini mostrate in precedenza
immagini_mostrate = []

# Variabile globale per contenere l'oggetto immagine corrente
immagine_corrente = None


def scarica_immagine_da_google():
    global immagine_corrente
    global parole_chiave

    gis = GoogleImagesSearch('AIzaSyA9BtHP-lD-8CUAvzJLkGe1O61kPIk9dW4', 'b59099d4db868454c')
    
    # Cerca una parola chiave in modo casuale
    x = random.randint(0, len(parole_chiave) - 1)
    
    # Cerca immagini con i parametri di ricerca specificati
    search_params = {
        'q': parole_chiave[x].chiave,
        'num': 1,  # Scarica solo 1 immagine alla volta
        'fileType': 'jpg',
        'safe': 'medium',
        'start': parole_chiave[x].n,  # Utilizza l'indice aggiuntivo per ottenere le immagini in ordine di rilevanza
    }
    
    # Incrementa il contatore di parole chiave
    parole_chiave[x].n += 1
    # Salva il vettore aggiornato nel file JSON solo se ci sono stati risultati
    salva_vettore_struct_su_file(parole_chiave, '/Users/newmac/Documents/PROG/Pythone/aimmagini/immagini/dati.json')

    try:
        gis.search(search_params=search_params)
        risultati = gis.results()

        if risultati:
            immagine_corrente = risultati[0]
            nuova_immagine = f'/Users/newmac/Documents/PROG/Pythone/aimmagini/immagini/immagini' #immagine_{len(immagini_mostrate) + 1}.jpg
            immagine_corrente.download(nuova_immagine)
            return immagine_corrente
    except Exception as e:
        print(f"Errore durante il download dell'immagine: {e}")

    return None


# Definizione di una classe per rappresentare la "struct"
class MyStruct:
    def __init__(self, chiave, n):
        self.chiave = chiave
        self.n = n
   
         
def salva_vettore_struct_su_file(vettore_struct, nome_file):
    with open(nome_file, 'w') as file_json:
        json.dump([vars(item) for item in vettore_struct], file_json, indent=2)


def carica_vettore_struct_da_file(nome_file):
    if os.path.exists(nome_file) and os.path.getsize(nome_file) > 0:
        with open(nome_file, 'r') as file_json:
            data = json.load(file_json)
        return [MyStruct(**item) for item in data]
    else:
        return []
    
# Carica i dati dal file JSON, se presenti, altrimenti inizializza come lista vuota
parole_chiave = carica_vettore_struct_da_file('/Users/newmac/Documents/PROG/Pythone/aimmagini/immagini/dati.json')

# Aggiungi una nuova struttura solo se il vettore è vuoto (nessun dato presente nel file JSON)
if not parole_chiave:
    # Creazione del vettore di struct utilizzando la classe personalizzata
    parole_chiave = [
        MyStruct("persona", 1),
        MyStruct("uomo", 1),
    ]

  
def mostra_immagine_casuale():
    global immagine_corrente

    immagine_corrente = scarica_immagine_da_google()

    if immagine_corrente:
        # Converti l'immagine in un oggetto di tipo PIL.Image.Image
        image = Image.open(BytesIO(immagine_corrente.get_raw_data()))
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.image = photo

        for button in buttons_colonna1:
            button.config(state="normal")
        for button in buttons_colonna2:
            button.config(state="normal")


def salva_scelte():
    global immagine_corrente

    # Ottieni le scelte dell'utente
    tipo_scelto = colonna1.get()
    etnia_scelta = colonna2.get()

    # Salva i dati nel file CSV
    with open('/Users/newmac/Documents/PROG/Pythone/aimmagini/scelte.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        # Utilizza os.path.basename per ottenere il nome del file immagine senza il percorso completo
        nome_file_immagine = quote(os.path.basename(immagine_corrente.url))
        writer.writerow([nome_file_immagine, tipo_scelto, etnia_scelta])

    # Mostra un messaggio di conferma
    messagebox.showinfo("Conferma", "Le tue scelte sono state salvate correttamente!")

    # Mostra una nuova immagine
    mostra_immagine_casuale()


def crea_interfaccia():
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
