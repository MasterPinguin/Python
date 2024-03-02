import numpy as np
from pandas import read_csv
from sklearn.tree import DecisionTreeClassifier

# Carica i dati dal file CSV
giocatori = read_csv('numeri_primi/numeri_primi.csv')

# Caratteristiche (X) e target (y)
X = giocatori[['c']]  # Usa 'c' come caratteristica
y = giocatori['n']  # 'n' è il target

# Crea il modello di classificazione
modello = DecisionTreeClassifier()
modello.fit(X.values, y.values)

# Richiedi l'input all'utente
c = int(input("Inserisci il valore di c: "))

# Effettua la previsione
previsione = modello.predict([[c]])  # Passa un array di caratteristiche (matrice 2D)
print(f"La previsione per c = {c} è n ≈ {previsione[0]:.0f}")
