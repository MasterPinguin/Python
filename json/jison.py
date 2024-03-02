import json
# Leggi i dati JSON da un file
with open("dati.json", "r") as file:
    dati = json.load(file)
# Ora puoi accedere ai dati come chiavi nel dizionario
print(f"Nome: {dati['nome']}, Età: {dati['età']}, Città: {dati['città']}")
# Creo il valore dell'indirizzo
dati["indirizzo"] = "123 Main Street"
# Modifica il valore dell'età
dati["età"] = 31
# Scrivi i dati aggiornati nel file JSON
with open("dati.json", "w") as file:
    json.dump(dati, file, indent=4)
print(dati)
