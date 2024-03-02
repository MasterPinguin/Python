import time #librerie

while(True):
    num1 = int(input("inserisci numero 1: "))
    segno = string(input("inserisci + per addizione : per la divisione x per la moltiplicazione e - per la sottrazione:"))
    num2 = int(input("inserisci numero 2: "))
    print("=")
    if segno == "+":
        addizione = num1+num2
        print(addizione)
    elif segno == ":":
        divisione = num1/num2
        print(divisione)
    elif segno == "x":
        moltiplicazione = num1*num2
        print(moltiplicazione)
    elif segno == "-":
        sottrazione = num1-num2
        print(sottrazione)