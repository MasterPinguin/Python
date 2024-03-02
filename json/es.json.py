import json
import time

with open('data.json') as json_file: #per aprire all'interno del programma il file json
	data = json.load(json_file) #per aprire all'interno del programma il file json

data["tempo"] = 2 #creo la variabie tempo per il file json

with open('data.json', 'w') as outfile: # scrivi la variabile nel file json
	json.dump(data, outfile)  # scrivi la variabile nel file json

while(True): # while(True) per girare all'infinito
    time.sleep(5) #mette in per tempo che scegli

    with open('data.json') as json_file: #per aprire all'interno del programma il file json
        data = json.load(json_file) #per aprire all'interno del programma il file json

    data["temperatura"] = "6"
    data["umidita"] = "24"
    data["tempo"] = data["tempo"] + 2
    

    with open('data.json', 'w') as outfile: #scrivi la variabile nel file json
	    json.dump(data, outfile) #scrivi la variabile nel file json