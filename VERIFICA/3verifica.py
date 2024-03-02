n=int(input("inserisci il numero dei numeri che vuoi inserire: "))
num = []
print("fare differire i valori ognuno dal precedente di un valore costante:")
for i in range(n):
    num_input = int(input(f"Inserisci il {i + 1}˚ valore: "))
    num.append(num_input)

rapp=num[1]-num[0]
costante=True
diffmax=rapp
diffmin=rapp
for i in range(1,n):
    diff=num[i]-num[i-1]
    if(diff!=rapp):
        costante=False
        if(diff>diffmax):
            diffmax=diff
        if(diff<diffmin):
            diffmin=diff

if costante: print(f"i valori della lista sono costanti con un rapporto di {rapp:>20d} tra un numero e l'altro ")
else: print(f"i valori della lista non sono costanti e il valore massimo della differenza è di {diffmax:>20d} mentre il minimo è di {diffmin:>20d} ")