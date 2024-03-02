import calcolo

n=int(input("inserisci il numero di quanti prodotti vuoi inserire: "))
prodotti = []
quantit = []
prezz = []
for i in range(n):
    nome = str(input(f"Inserisci il nome del {i + 1}˚ prodotto: "))
    quantita = int(input(f"Inserisci la quantità di prodotti {nome} venduti: "))
    prezzo = float(input(f"Inserisci il prezzo di vendita di ognuno dei {quantita} {nome}: "))
    if(quantita>0):
        prodotti.append((nome,quantita,prezzo))
        quantit.append(quantita)
        prezz.append(prezzo)
print(prodotti)
print(f"la media di prodotti venduti per ogni prodotto è {calcolo.media(quantit)}")
print(f"il prezzo medio è {calcolo.media(prezz)}")
print(f"il valore totale delle vendite è {calcolo.valore_totale(prodotti)}")