def carica_parole():
    parole = list()
    parola = input("inserisci una parola (* = fine): ")
    while parola != '*':
        parole.append(parola)
        parola = input("inserisci una parola (* = fine): ")
    return parole

def main():
    print("INSERIMENTO PAROLE")
    testo = carica_parole()

    print("\nSono state inserite", len(testo), "parole")
    testo.clear()
    print(testo)

main()