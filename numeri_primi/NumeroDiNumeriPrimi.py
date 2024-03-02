import csv

m = int(input("inserisci il numero dei numeri primi che vuoi visualizzare: ")) 
primi = []  # Lista per mantenere i numeri primi trovati
n = 1
c = 2
print("1, 1\n2, 2")
while c != m :
    n += 1
    is_prime = True

    for primo in primi:
        if primo * primo > n:  # Crivello di Eratostene
            break
        if n % primo == 0:
            is_prime = False
            break

    if is_prime:
        primi.append(n)
        c += 1
        print(f"{c}, {n}")
