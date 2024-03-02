def som(a,b):
    if b==0:
        a=0
    else:
        a=a+som(a,b-1)
    return a

a=int(input("inserisci i numeri dei quali vuoi il prodotto:\na:"))
b=int(input("b:"))
print(f"il prodotto di {a}x{b}={som(a,b)}")

