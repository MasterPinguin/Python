import os
import json

# Definizione di una classe per rappresentare la "struct"
class MyStruct:
    def __init__(self, campo1, campo2, campo3):
        self.campo1 = campo1
        self.campo2 = campo2
        self.campo3 = campo3

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

# Esempio di utilizzo
# Carica i dati dal file JSON, se presenti, altrimenti inizializza come lista vuota
vettore_struct = carica_vettore_struct_da_file('/Users/newmac/Documents/PROG/Pythone/aimmagini/immagini/datii.json')

# Aggiungi una nuova struttura solo se il vettore è vuoto (nessun dato presente nel file JSON)
if not vettore_struct:
    vettore_struct = [
        MyStruct(1, "foo", True),
        MyStruct(2, "bar", False),
    ]

# Aggiungi una nuova struttura
vettore_struct.append(MyStruct(3, "baz", True))

# Ora puoi utilizzare il vettore di struct nel resto del codice
# ...
vettore_struct[0].campo1+=1
print(vettore_struct[0].campo1)
print(vettore_struct[0].campo2)
print(vettore_struct[0].campo3)

# Salva il vettore aggiornato nel file JSON
salva_vettore_struct_su_file(vettore_struct, '/Users/newmac/Documents/PROG/Pythone/aimmagini/immagini/datii.json')
