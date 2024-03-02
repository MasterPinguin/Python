def aggiungi_canzone(coda, titolo):
    coda.insert(0, titolo)
    print(f"La canzone '{titolo}' è stata aggiunta alla coda.")

def riproduci_canzone(coda):
    if coda:
        canzone_in_riproduzione = coda.pop(0)
        print(f"Riproduzione in corso: '{canzone_in_riproduzione}'")
    else:
        print("La coda è vuota. Aggiungi delle canzoni.")

def elenca_canzoni_in_attesa(coda):
    if coda:
        print("Canzoni in attesa:")
        for canzone in coda:
            print(f"- {canzone}")
    else:
        print("La coda è vuota. Aggiungi delle canzoni.")

coda_musicale = []

while True:
    print("\nMenu:")
    print("1. Aggiungi canzone")
    print("2. Riproduci canzone in testa")
    print("3. Lista completa delle canzoni in attesa")
    print("4. Esci")

    scelta = input("Seleziona un'opzione: ")

    if scelta == '1':
        titolo_canzone = input("Inserisci il titolo della canzone: ")
        aggiungi_canzone(coda_musicale, titolo_canzone)
    elif scelta == '2':
        riproduci_canzone(coda_musicale)
    elif scelta == '3':
        elenca_canzoni_in_attesa(coda_musicale)
    elif scelta == '4':
        print("Programma terminato.")
        break
    else:
        print("Opzione non valida. Riprova.")
