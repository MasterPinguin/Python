coda_pazienti = list()
print("Inserisci l'elenco dei pazienti, per terminare l'inserimento metti l'*")
paziente = input("Inserisci una nuovo paziente: ")

while paziente != '*':
    coda_pazienti.append(paziente)
    print(f"{paziente} è stato registrato.")
    paziente = input("Inserisci una nuovo paziente: ")

if (len(coda_pazienti)>0):
    print(f"Il prossimo paziente in attesa è: {coda_pazienti[0]}")
else:
    print("La coda dei pazienti è vuota.")
