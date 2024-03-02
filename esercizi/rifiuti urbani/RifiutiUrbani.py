# Modulo con costanti
import costanti

# Modulo con funzioni di calcolo
import calcoli

# Input del numero di persone
numero_persone = int(input("Inserisci il numero di persone: "))

# Calcola l'imponibile
imponibile = calcoli.calcola_imponibile(numero_persone)

# Calcola l'IVA
iva = calcoli.calcola_iva(imponibile)

# Aggiungi le spese postali
spese_postali = costanti.SPESE_POSTALI

# Calcola il totale da pagare
totale_da_pagare = imponibile + iva + spese_postali

# Stampare la bolletta
print(f"Imponibile: {imponibile:.2f} €")
print(f"IVA: {iva:.2f} €")
print(f"Spese postali: {spese_postali:.2f} €")
print(f"Totale da pagare: {totale_da_pagare:.2f} €")
