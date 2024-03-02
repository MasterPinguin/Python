def calcolo(prodotti, aumentocosto):
    prodotti_aumentati=[]
    for a, costo in prodotti:
        aumentato=(costo/100*aumentocosto)+costo
        prodotti_aumentati.append((a, aumentato))
    return prodotti_aumentati 

def stampa(lista_prodotti):
    for desk, prez in lista_prodotti:
        print(f"il prodotto {desk} ha aumentato il prezzo a {prez}€")