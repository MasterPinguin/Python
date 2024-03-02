# Apertura in lettura
squadre_serie_a = open("file/squadre_serie_a.txt", "r")
# Leggi
for squadra in squadre_serie_a:
    print(squadra.strip())
squadre_serie_a.close()
