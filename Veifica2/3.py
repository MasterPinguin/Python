import random

MAIUSCOLE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
MINUSCOLE = 'abcdefghijklmnopqrstuvwxyz'
NUMERICHE = '0123456789'

# Il primo carattere è alfabetico (maiuscolo o minuscolo)
numero_casuale = random.randint(0, 25)
min_mius = random.randint(1, 2)
if(min_mius==1):
    primo_carattere=MAIUSCOLE[numero_casuale]
else:
    primo_carattere=MINUSCOLE[numero_casuale]

# I rimanenti caratteri sono alfabetici o numerici
caratteri_rimasti = ""
for _ in range(9):
    x = random.randint(1, 3)
    if(x==1):
        numero_casuale = random.randint(0, 25)
        caratteri_rimasti=caratteri_rimasti+str(MAIUSCOLE[numero_casuale])
    elif(x==2):
        numero_casuale = random.randint(0, 25)
        caratteri_rimasti=caratteri_rimasti+str(MINUSCOLE[numero_casuale])
    else:
        numero_casuale = random.randint(0, 10)
        caratteri_rimasti=caratteri_rimasti+str(NUMERICHE[numero_casuale])

# Unisci i caratteri per formare la password
password = str(primo_carattere) + str(caratteri_rimasti)

print("Password generata:", password)
