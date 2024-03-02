# Apertura in scrittura
with open("file/squadre_serie_a.txt", "w") as file:
    # Scrivi
    squadre_serie_a = ["Serie A","Juventus", "Inter", "Milan", "Roma", "Napoli", "Lazio", "Atalanta", "Fiorentina", "Sassuolo", "Sampdoria", "Udinese", "Genoa", "Bologna", "Cagliari", "Torino", "Spezia", "Empoli", "Venezia", "Salernitana", "Verona"]
    for squadra in squadre_serie_a:
        file.write(squadra + "\n")
# Apertura in append
with open("file/squadre_serie_a.txt", "a") as file:
    # append
    squadre_serie_b = ["Serie B","Monza", "Brescia", "Vicenza", "Reggina", "Cosenza", "Cremonese", "Lecce", "Pisa", "Como", "Pordenone", "Ascoli", "Reggiana", "Frosinone", "Virtus Entella", "Cittadella", "Benevento", "Perugia", "Ternana", "Pescara", "L.R. Vicenza"]
    for squadra in squadre_serie_b:
        file.write(squadra + "\n")
