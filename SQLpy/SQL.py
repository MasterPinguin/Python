import mysql.connector

# Connessione al server MySQL senza password
conn = mysql.connector.connect(
    host="localhost",
    user="root"
)

# Creazione di un oggetto cursor per eseguire comandi SQL
cursor = conn.cursor()

# Creazione del database se non esiste
create_database_query = "CREATE DATABASE IF NOT EXISTS esercizi"
cursor.execute(create_database_query)

# Selezione del database appena creato
cursor.execute("USE esercizi")

# Creazione della tabella anagrafica se non esiste
create_table_query = """
CREATE TABLE IF NOT EXISTS anagrafica (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cognome VARCHAR(255),
    nome VARCHAR(255),
    ruolo VARCHAR(255)
)
"""
cursor.execute(create_table_query)

# Funzione per popolare la tabella anagrafica
def popola_anagrafica(cognome, nome, ruolo):
    insert_query = "INSERT INTO anagrafica (cognome, nome, ruolo) VALUES (%s, %s, %s)"
    values = (cognome, nome, ruolo)
    cursor.execute(insert_query, values)
    conn.commit()

# Funzione per estrarre dati di un dipendente per cognome e nome
def estrai_dipendente(cognome, nome):
    select_query = "SELECT * FROM anagrafica WHERE cognome = %s AND nome = %s"
    values = (cognome, nome)
    cursor.execute(select_query, values)
    result = cursor.fetchall()
    return result

# Funzione per estrarre dati di dipendenti per ruolo
def estrai_dipendenti_per_ruolo(ruolo):
    select_query = "SELECT * FROM anagrafica WHERE ruolo = %s"
    values = (ruolo,)
    cursor.execute(select_query, values)
    result = cursor.fetchall()
    return result

# Esempi di utilizzo
popola_anagrafica("Rossi", "Mario", "Impiegato")
popola_anagrafica("Verdi", "Luigi", "Manager")

print("Dati dipendente:")
dipendente = estrai_dipendente("Rossi", "Mario")
print(dipendente)

print("\nDati dipendenti per ruolo:")
dipendenti_manager = estrai_dipendenti_per_ruolo("Manager")
print(dipendenti_manager)


#Cancello il database per evitare conflitti nelle prossime esecuzioni
drop_database_query = "DROP DATABASE esercizi"
cursor.execute(drop_database_query)

# Chiusura del cursore e della connessione
cursor.close()
conn.close()
