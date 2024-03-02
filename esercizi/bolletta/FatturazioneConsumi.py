import calcoli

consumo=int(input("Consumo in mc: "))

tipo=None
while tipo != 'A' and tipo != 'P':
    print("Tipologia di utenza (A = azienda, P = privato)")
    tipo =input().upper()

if tipo == 'A':
    calcoli.calcolo_aziende(consumo)
else:
    calcoli.calcolo_privati(consumo)