def generatePath(path):
    elementi_path = []
    elementi_path = path.strip().split('/')
    elementi_nuovo_path = []
    elementi_nuovo_path = elementi_path[3].strip().split('_')
    nuovo_path = "/webcam/" + elementi_nuovo_path[1] + "/" + elementi_nuovo_path[3][:4] + elementi_nuovo_path[3][4:6] + elementi_nuovo_path[3][6:8] + "/" + elementi_nuovo_path[3][8:10] + elementi_nuovo_path[3][10:12] + elementi_nuovo_path[3][12:14] + ".jpg"
    return nuovo_path
    # Funzione che serve per cambiare il path e salvarlo nella cartella relativa. (esempio cartella /webcam/sanmenaio/GG/nome.jpg)
    # SALVARE TIMING PER PRIMO!!!
    # Path originario: /webcam/cache/Hikvision_NOMESEDE_F66728651_20230828141004030_TIMING.jpg
    # Path destinazione: /webcam/sanmenaio/YYYY_MM_GG/HH_MM_SS.jpg


print(generatePath("/webcam/cache/Hikvision_NOME SEDE_F66728651_20230828141004030_TIMING.jpg"))