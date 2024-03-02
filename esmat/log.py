import math
t=True
while t:
    try:
        numero = float(input("Inserisci un numero: "))
        t=False
    except (NameError, ValueError, TypeError, SyntaxError) as errore:
        print("Hai inserito dei caratteri al posto di un numero. L'errore potrebbe essere legato all'utilizzo della ',' al posto del '.'")

esponenziale = math.exp(numero)

log_naturale = math.log(numero)

log_base_10 = math.log10(numero)

print(f"L'esponenziale di {str(numero).rstrip('0').rstrip('.') if '.' in str(numero) else str(numero)} è {str(esponenziale).rstrip('0').rstrip('.') if '.' in str(esponenziale) else str(esponenziale)}")
print(f"Il logaritmo naturale (base e) di {str(numero).rstrip('0').rstrip('.') if '.' in str(numero) else str(numero)} è {str(log_naturale).rstrip('0').rstrip('.') if '.' in str(log_naturale) else str(log_naturale)}")
print(f"Il logaritmo in base 10 di {str(numero).rstrip('0').rstrip('.') if '.' in str(numero) else str(numero)} è {str(log_base_10).rstrip('0').rstrip('.') if '.' in str(log_base_10) else str(log_base_10)}")
