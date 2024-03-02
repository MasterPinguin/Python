import datetime
import locale

# Imposta la lingua locale in italiano
locale.setlocale(locale.LC_TIME, 'it_IT')

# Chiedi all'utente di inserire la data di immatricolazione nel formato 'AAAA-MM-GG'
data_immatricolazione = input("Inserisci la data di immatricolazione (AAAA-MM-GG): ")

# Converte la stringa di input in un oggetto datetime
data_immatricolazione = datetime.datetime.strptime(data_immatricolazione, "%Y-%m-%d").date()

# Calcola la data della prima revisione (4 anni dopo l'immatricolazione)
data_prima_revisione = data_immatricolazione + datetime.timedelta(days=4*365)

# Calcola e visualizza le date delle prime tre revisioni con nomi dei mesi in italiano
print("Data di immatricolazione:", data_immatricolazione.strftime("%d %B %Y"))

for i in range(1, 4):
    print(f"Scadenza revisione {i}:", data_prima_revisione.strftime("%d %B %Y"))
    data_prima_revisione += datetime.timedelta(days=2*365)
