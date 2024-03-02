import sqlite3

def create_database():
    #sede(id,nome)
    #immagine(id,idSede,dataStamp,timeStamp,path)
    
    # Creare una connessione al database (se non esiste, verrà creato)
    conn = sqlite3.connect('MeteoGargano.db')

    # Creare un cursore per eseguire comandi SQL
    cursor = conn.cursor()

    #creazione della tabella sede
    cursor.execute('''
        create table if not exists sede(
            id integer primary key autoincrement,
            nome varchar(50) not null
        )
    ''')

    # Confermare le modifiche
    conn.commit()

    #creazione della tabella immagine
    cursor.execute('''
        create table if not exists immagine(
            id integer primary key autoincrement,
            idSede integer not null,
            dataStamp date not null,
            timeStamp time not null,
            path varchar(255) not null,
            foreign key(idSede) references sede(id) on delete cascade
        )
    ''')

    # Confermare le modifiche
    conn.commit()

create_database()