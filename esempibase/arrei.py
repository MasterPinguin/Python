vett = [2, 4, 7, 1, 3] #dichiarazione di un vettore
#print(vett[0])
trovato = False
i = 0

while( i <= 3 and trovato == False):
    if vett[i] == 1:
        trovato = True
    else:
        i = i + 1

print("trovato = " + str(trovato)) # stampa trovato = a falo o a vero 

for var in vett:
    var=var+1
    print(var)