comuni=[]
n=int(input("inserisci il numero di studenti dei quali si vuole registrare il comune: "))
for i in range(n):
    alunno = str(input(f"Inserisci il nome del {i + 1}˚ alunno: "))
    comune = str(input(f"Inserisci il comune di provenienza del {i + 1}˚ alunno: "))
    comuni.append((alunno, comune))

comuni_distinti=[]
comuni_distinti.append(comuni[0][1])
i = 0
for _, comun in comuni:
    if comun != comuni_distinti[i]:
        comuni_distinti.append(comun)
        i += 1

print(f"i comuni distini sono {len(comuni_distinti)} e sono i deguenti:\n{comuni_distinti}")