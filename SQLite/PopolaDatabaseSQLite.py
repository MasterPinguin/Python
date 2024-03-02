import sqlite3
from pyftpdlib.handlers import FTPHandler
import os

def generatePath(path):
    elementi_path = []
    elementi_path = path.strip().split('/')
    elementi_nuovo_path = []
    elementi_nuovo_path = elementi_path[3].strip().split('_')
    nuovo_path = "/webcam/" + elementi_nuovo_path[1] + "/" + elementi_nuovo_path[3][:4] + "-" + elementi_nuovo_path[3][4:6] + "-" + elementi_nuovo_path[3][6:8] + "/" + elementi_nuovo_path[3][8:10] + ":" + elementi_nuovo_path[3][10:12] + ":" + elementi_nuovo_path[3][12:14] + ".jpg"
    return nuovo_path

class MyHandler(FTPHandler):
    def on_file_received(self, file):#aggiorna il database creando nuove sedi e immagini
        # Creare una connessione al database
        conn = sqlite3.connect('nome_database.db')

        # Creare un cursore per eseguire comandi SQL
        cursor = conn.cursor()

        # estraggo il path giusto
        path = generatePath(file)

        # estraggo i dati dal path
        dati_utili = path.strip().split('/') 

        # estraggo il nome della sede dal path
        nome = dati_utili[2]

        # query per sapere se la sede gia esiste
        select_first_query = """
        select *
        from sede 
        whdere sede.nome = %s
        """
        cursor.execute(select_first_query, nome)
        exist = cursor.fetchall()

        if len(exist) == 0:
            # Inserire dati nella tabella sede se non esiste
            insert_query = "insert into sede(nome) values (%s)"
            cursor.execute(insert_query, nome)
        
        # query per estrarre l'id della sede
        select_query = """
        select id 
        from sede 
        whdere sede.nome = %s
        """
        cursor.execute(select_query, nome)
        idSede = cursor.fetchall()

        # estraggo la data dal path
        data = dati_utili[3]

        # estraggo l'orario dal path
        time = dati_utili[4]

        # Inserire dati nella tabella sede se non esiste
        insert_query = "insert into immagine(idSede, dataStamp, timeStamp, path) values (%s, %s, %s, %s)"
        values = (idSede, data, time, path)
        cursor.execute(insert_query, values)

        # Rinomina il file per spostarlo
        os.rename(file, path)

        # Confermare le modifiche
        conn.commit()
        pass