def esadecimale_a_decimale(cifra_esadecimale):
    esadecimale_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    return esadecimale_dict[cifra_esadecimale.upper()]

numero_esadecimale_1 = input("Inserisci il primo numero esadecimale a 1 cifra: ")
numero_esadecimale_2 = input("Inserisci il secondo numero esadecimale a 1 cifra: ")

decimale_1 = esadecimale_a_decimale(numero_esadecimale_1)
decimale_2 = esadecimale_a_decimale(numero_esadecimale_2)

somma_decimale = decimale_1 + decimale_2

print(f"La somma di {decimale_1} + {decimale_2} in decimale è: {somma_decimale}")
