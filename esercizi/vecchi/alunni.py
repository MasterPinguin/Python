studenti = []
distanze = []
studenti_lontani = []

for i in range(3):
    nome = input("Inserisci il nome dello studente {}: ".format(i+1))
    distanza = float(input("Inserisci la distanza in km da casa a scuola per {}: ".format(nome)))
    if distanza > 30:
        studenti_lontani.append(nome)
    studenti.append(nome)
    distanze.append(distanza)

if len(studenti_lontani) > 0:
    print("Gli studenti che abitano a più di 30 km dalla scuola sono:")
    for nome in studenti_lontani:
        print(nome)
else:
    print("Nessuno degli studenti abita a più di 30 km dalla scuola.")
