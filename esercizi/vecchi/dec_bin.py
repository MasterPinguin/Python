b=[]
dec=int(input("inserisci il numero che vuoi trasformare in decimale:"))
bin = bin(dec)
while(dec>0):
    b.append(str(dec%2))
    dec=dec/2
bi=''
for i in reversed(b):
    bi+=i

print(bi+"   "+bin)