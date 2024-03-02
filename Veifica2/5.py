occupati_anno = dict()

for anno in range(2013, 2023):
    occupati = int(input(f"Inserisci il numero degli occupati per l'anno {anno}: "))
    occupati_anno[anno] = occupati

# Calcolo della media dividendo la somma dei valori degli occupati per la lunghezza del'dizionario
media = sum(occupati_anno.values()) / len(occupati_anno)

print(f"\nIl valore medio degli occupati negli ultimi dieci anni è: {media}\n")

# invertendo chiavi e valori
inverso = dict()
for chiave, valore in occupati_anno.items():
    inverso[valore] = chiave

# ricerca
valore_cercato = int(input("Inserisci il valore degli occupati per trovare l'anno corrispondente: "))
anno_corrispondente = inverso.get(valore_cercato, "Valore non trovato")

print(f"\nL'anno corrispondente al valore degli occupati {valore_cercato} è: {anno_corrispondente}")