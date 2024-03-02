import modulo

def acquisisci_dati_prodotti():
    n = int(input("Quanti prodotti vuoi inserire? "))
    prodotti = []
    for i in range(n):
        descrizione = input(f"Inserisci la descrizione del prodotto {i + 1}: ")
        costo = int(input(f"Inserisci il costo del prodotto {i + 1}: "))
        prodotti.append((descrizione, costo))
    return prodotti

dati_prodotti = acquisisci_dati_prodotti()
aumento = int(input("inserisci di quanto viene aumentato il prezzo"))
dati_prodotti_aumentati = modulo.calcolo(dati_prodotti, aumento)
modulo.stampa(dati_prodotti_aumentati)
