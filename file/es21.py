def cerca(file_path, posizione):
    file = open(file_path, 'r')
    file.seek((posizione - 1) * 41)
    studente = file.read(40)
    nome = studente[20:].strip()
    cognome = studente[:20].strip()
    return nome, cognome

# Leggi il file originale
lista_studenti = []
studenti = open('file/studenti.txt', 'r')
lista_studenti = [line.strip() for line in studenti]
studenti.close()

# Ordina la lista degli studenti alfabeticamente
lista_studenti_ordinata = sorted(lista_studenti)

# Scrivi il nuovo file ordinato
studenti = open('file/studenti_ordinati.txt', 'w')
for studente in lista_studenti_ordinata:
    studenti.write(studente + '\n')
studenti.close()

# nome e cognome nella posizione pos
pos = int(input("inserisci la posizione della quale vuoi sapere che studente risiede: "))
nome, cognome = cerca('file/studenti_ordinati.txt', pos)

print(f"Lo studente alla posizione {pos} è: {nome} {cognome}")
