import random
incassi=[]
som_mesi=[0,0,0,0,0,0]
som_rep=[0,0,0]
som_tot=0
for i in range(3):
    incassi.append([])
    incassi[i].append(f"reparto {i+1}:")
    for j in range(6):
        inc=random.randint(0, 100000)
        incassi[i].append(inc)
        som_mesi[j]=som_mesi[j]+inc
        som_rep[i]=som_rep[i]+inc
        som_tot=som_tot+inc

for reparto in incassi:
    print(reparto)

print(f"\n")
for i in range(6):
    print(f"la somma degli incassi del {i+1}˚ mese è di {som_mesi[i]}€")
print(f"\n")
for i in range(3):
    print(f"la somma degli incassi del {i+1}˚ reparto è di {som_rep[i]}€")

print(f"\n mentre la somma totale degli incassi del magazzino è di {som_tot}€")