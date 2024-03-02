v=float(input("inserisci la velocità dell'autovettura: "))
y=0
while(y<1 or y>4):
    y=int(input("inserisci le condizioni stradali ( inserire solo una opsione tra le seguenti 1,2,3,4):\n1 asfalto ruvido\n2 asfalto liscio\n3 asfalto bagnato\n4 asfalto ghiacciato\n: "))
if(y==1):f=0.6
elif(y==2):f=0.5
elif(y==3):f=0.4
else:f=0.1
print(f"lo spazio di frenata a partire dalla velocità di {v}km/h e dalla condizione dell’asfalto è: ",(v**2)/(250*f)," m")