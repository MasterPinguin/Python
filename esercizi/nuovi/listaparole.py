elenco_parole=[]
parola=''
print("inserisci le parole da mettere nella lista se vuoi uscirne inserisci *:\n")
i=0
while(parola!='*'):
    i+=1
    parola=str(input(f"inserisci la {i}˚ parola:\n"))
    if(parola!='*'):
        elenco_parole.append(parola)

print(f"le parole memorizzate sono {len(elenco_parole)}:\n")

print(elenco_parole)

elenco_parole=[]

print(elenco_parole)