parole = list()
print("Inserisci un elenco di parole e per terminare l'inserimento metti l'*")
parola = input("Inserisci una parola: ")

while parola != '*':
    parole.append(parola)
    parola = input("Inserisci una parola: ")

parole.sort() # Ordinata in modo crescente
paroleDecrescente = parole.copy() 
paroleDecrescente.sort(reverse=True)  # Ordina in modo decrescente

print("Sono state inserite", len(parole), "parole.")
print("Lista ordinata in ordine crescente:", parole)
print("Lista ordinata in ordine decrescente:", paroleDecrescente)
