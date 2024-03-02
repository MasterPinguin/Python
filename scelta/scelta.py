import numpy as np
from pandas import read_csv
from sklearn.tree import DecisionTreeClassifier

# prendo i dati per l'addestramento
giocatori = read_csv('/Users/newmac/Documents/PROG/Pythone/scelta/giocatori.csv')
X = giocatori.drop(columns=['videogame'])
y = giocatori['videogame']

# imposto l'albero decisionale
modello = DecisionTreeClassifier()
modello.fit(X.values, y.values)

# prendo i dati per l'output
n = int(input("inserisci il numero di persone di cui vuoi inserire i dati:  "))

matrice_nx2 = []

for i in range(n):
    sesso = 2
    while sesso not in (0, 1):
        sesso = int(input("Inserisci il sesso della persona {} per femmina 0 per maschio 1 :".format(i + 1)))
    età = 200
    while età <= 0 or età >= 100:
        età = int(input("Inserisci l'età della persona {}: ".format(i + 1)))

    matrice_nx2.append([sesso, età])

# Converti la lista di liste in un array NumPy
matrice_nx2 = np.array(matrice_nx2)

# Effettua la previsione
previsione = modello.predict(matrice_nx2)
print(previsione)