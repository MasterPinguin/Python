from math import sqrt 
print("le misure sono espresse in metri")
h = int(input("inserisci l'altezza del rettangolo: "))
b = int(input("inserisci la base del rettangolo: "))
d = sqrt((h**2)+(b**2))
print("l'area è",d,"m")