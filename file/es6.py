import random
# Apertura in scrittura
numeri = open("file/numeri.txt", "w")
# Scrivi
for numero in range(20):
    numero=random.randint(1, 100)
    numeri.write(str(numero) + "\n")
numeri.close()
# Apertura in lettura
numeri = open("file/numeri.txt", "r")
# Leggi
for numero in numeri:
    n=(int(numero.strip())/5)*6
    print(numero.strip(),"; ",round(n,2))
numeri.close()
