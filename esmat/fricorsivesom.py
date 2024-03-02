def sommatoria(n):
    if n==0:
        n=0
    else:
        n=n+sommatoria(n-1)
    return n

n=int(input("inserisci il numero n della sommatoria da 1 a n:\nn:"))
print(f"la sommatoria da 1 a {n} è : {sommatoria(n)}")

