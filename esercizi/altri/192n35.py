conti_correnti = {
    '123456': 1500.50,
    '789012': 3000.75,
    '345678': 100.00
}

def visualizza_saldo(numero_conto):
    # Verifica se il numero del conto è presente nel dizionario
    if numero_conto in conti_correnti:
        saldo = conti_correnti[numero_conto]
        print(f"Il saldo del conto {numero_conto} è: {saldo} euro")
    else:
        print(f"Il conto {numero_conto} non è presente nella mappa.")

# Fornisci il numero di conto
numero_conto_input = input("Inserisci il numero del conto: ")

# Visualizza il saldo o un messaggio se il conto non è presente
visualizza_saldo(numero_conto_input)
