from math import sqrt
a=int(input("inserisci i valori per l'equazione di secondo grado ax^2+bx+c=0\na:"))
b=int(input("b:"))
c=int(input("c:"))

d=(b^2)-4*a*c
if(d>0):
    x1=(-b+sqrt(d))/2*a
    x2=(-b-sqrt(d))/2*a
    print("x1=",x1,"x2=",x2)
elif(d==0):
    x=x2=-b/2*a
    print("x=",x)
else:
    print("impossibile l'equazione non si interseca mai con l'asse x")