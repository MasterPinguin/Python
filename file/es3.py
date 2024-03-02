# Apertura in scrittura
squadre_serie_a = open("file/squadre_serie_a.txt", "w")
# Scrivi
serie_a = ["Serie A","Juventus", "Inter", "Milan", "Roma", "Napoli", "Lazio", "Atalanta", "Fiorentina", "Sassuolo", "Sampdoria", "Udinese", "Genoa", "Bologna", "Cagliari", "Torino", "Spezia", "Empoli", "Venezia", "Salernitana", "Verona"]
for squadra in serie_a:
    squadre_serie_a.write(squadra + "\n")
squadre_serie_a.close()
# Apertura in append
squadre_serie_a = open("file/squadre_serie_a.txt", "a")
# append
serie_b = ["Serie B","Monza", "Brescia", "Vicenza", "Reggina", "Cosenza", "Cremonese", "Lecce", "Pisa", "Como", "Pordenone", "Ascoli", "Reggiana", "Frosinone", "Virtus Entella", "Cittadella", "Benevento", "Perugia", "Ternana", "Pescara", "L.R. Vicenza"]
for squadra in serie_b:
    squadre_serie_a.write(squadra + "\n")
squadre_serie_a.close()
