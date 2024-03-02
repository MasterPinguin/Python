import requests
import json
import time
with open('/Users/newmac/Documents/PROG/Pythone/investimento/info.json') as json_file: #per aprire all'interno del programma il file json
	info = json.load(json_file)
alerta = False

while(True):

    url = requests.get("https://api.pancakeswap.info/api/v2/tokens/0xb2f90ddc14d07bb42ad4d88266fde6e2afda9556")
    text = url.text
    dato = json.loads(text)
    dati = dato["data"]
    print(dati["price"]) #prezzo
    info["prezzo"] = (dati["price"]) #per il json
    soldi = float(dati["price"]) * float(16001604735) #secondo float aggiungere monete per 5 euro



    def truncate(n, decimals=2): #riduci in 2 cifre dopo virgola
        multiplier = 10 ** decimals
        return int(n * multiplier) / multiplier



    soldi2ciftre = truncate(soldi, 2) #culo in dolari a 2 cifre
    info["dai-5-euro"] = (soldi2ciftre) #per il json
    info["alerta"] = alerta #per il json
    with open('info.json', 'w') as outfile: # scrivi la variabile nel file json
        json.dump(info, outfile)

    print(soldi2ciftre)
    if float(dati["price"]) < float(0.000000000116186): #alerta del porco dio
        print("dio porco")
        alerta = True
    time.sleep(300)
