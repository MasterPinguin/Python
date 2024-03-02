# AttrezziMancanti.py: attrezzi mancanti per un lavoro

# funzione per il caricamento dei dati in un insieme 
def carica_insieme():
    insieme = set()
    attrezzo = input("Nome dell'attrezzo (* = fine): ")
    while attrezzo != '*':
        insieme.add(attrezzo)
        attrezzo = input("Nome dell'attrezzo (* = fine): ")
    return insieme
# funzione principale 
def main():
    # caricamento degli insiemi
    print("Attrezzi necessari")
    necessari = carica_insieme()
    print("\nForniti da Franco")
    da_franco = carica_insieme()
    print("\nForniti da Gianni")
    da_giovanni = carica_insieme()
    print("\nForniti da Matio")
    da_mario = carica_insieme()

    # attrezzi complessivamente procurati
    procurati = da_franco.union(da_giovanni)
    procurati = procurati.union(da_mario)

    #attrezzi mancanti e non richiesti
    mancano = necessari.difference(procurati)
    crescono = procurati.difference(necessari)

    # risultati
    print("\nMancano", len(mancano), "attrezzi")
    print("Attrezzi mancanti: ", mancano)
    print("Attrezzi inutili: ", crescono)

# esecuzione del programma
main()