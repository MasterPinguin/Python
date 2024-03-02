from math import sqrt
p1x=int(input("inserisci i valori x e y di tre punti per conoscere quale è piu distante\nP1 (x;y):\ninserisci la x:"))
p1y=int(input("inserisci la y:"))
p2x=int(input("P2 (x;y):\ninserisci la x:"))
p2y=int(input("inserisci la y:"))
p3x=int(input("P3 (x;y):\ninserisci la x:"))
p3y=int(input("inserisci la y:"))

print(f"     x  y\nP1 ({p1x};{p1y})\nP2 ({p2x};{p2y})\nP3 ({p3x};{p3y})")

dtraP1eP2=sqrt((p1x-p2x)**2+(p1y-p2y)**2)
dtraP2eP3=sqrt((p2x-p3x)**2+(p2y-p3y)**2)
dtraP1eP3=sqrt((p1x-p3x)**2+(p1y-p3y)**2)

if(dtraP1eP2>dtraP2eP3):
    if(dtraP1eP2>dtraP1eP3):
        print(f"\ni punti piu distanti sono il P1 e il P2 con una distanza pari a {dtraP1eP2:>4.3f}")
    else:
        print(f"\ni punti piu distanti sono il P1 e il P3 con una distanza pari a {dtraP1eP3:>4.3f}")
else:
    if(dtraP2eP3>dtraP1eP3):
        print(f"\ni punti piu distanti sono il P2 e il P3 con una distanza pari a {dtraP2eP3:>4.3f}")
    else:
        print(f"\ni punti piu distanti sono il P1 e il P3 con una distanza pari a {dtraP1eP3:>4.3f}")