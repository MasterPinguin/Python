def calcola_imposta(reddito):
    limiti = [15000, 28000, 55000, 75000, 1000000000000]
    aliquote = [23, 27, 38, 41, 43]

    imposta_totale = 0

    for i in range(len(limiti)):
        if(i==0):
            imposta_totale += (limiti[i]) * aliquote[i] / 100
        elif(reddito <= limiti[i]):
            imposta_totale += (reddito - limiti[i-1]) * aliquote[i] / 100
        else:
            imposta_totale += (limiti[i]-limiti[i-1]) * aliquote[i] / 100
        print(i)
        print(limiti[i])
        print(aliquote[i])
        print(imposta_totale)
        
        if reddito <= limiti[i]:
            break

    tassazione_media = (imposta_totale / reddito) * 100

    return imposta_totale, tassazione_media

reddito_input = float(input("Inserisci il reddito: "))

imposta, tassazione_media = calcola_imposta(reddito_input)

print(f"L'imposta sul reddito è: {imposta:.2f} €")
print(f"La tassazione media è: {tassazione_media:.2f}%")
