def media(valori_media):
    media=0
    for i in valori_media:
        media=media+i
    media=media/len(valori_media)
    return media

def valore_totale(valori):
    valore_totale=0
    for i in valori:
        valore_totale=valore_totale+(i[1]*i[2])
    return valore_totale