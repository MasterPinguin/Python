def aggiorna_numeri(file_sede, file_dipendente, file_contratto):
    # Aggiorna Numero_dipendenti_sede
    with open(file_sede, 'r') as f_sede:
        righe_sede = f_sede.readlines()

    # Trova l'indice dell'attributo "Codice_sede" nel file dipendente.txt
    indice_codice_sede = 13

    for riga_sede in righe_sede[1:]:
        codice_sede = riga_sede.strip().split(';')[0]
        with open(file_dipendente, 'r') as f_dipendente:
            righe_dipendente = f_dipendente.readlines()
        # Conta i dipendenti associati al codice_sede
        numero_dipendenti = 0
        for riga_dipendente in righe_dipendente[1:]:
            valori_riga = riga_dipendente.strip().split(';')
            if valori_riga[indice_codice_sede] == codice_sede:
                numero_dipendenti += 1
        # Aggiorna il valore di Numero_dipendenti_sede nel file_sede
        nuovi_valori_sede = riga_sede.strip().split(';')
        nuovi_valori_sede[-1] = str(numero_dipendenti)
        nuova_riga_sede = ';'.join(nuovi_valori_sede)

        indice_riga_sede = righe_sede.index(riga_sede)
        if riga_sede == righe_sede[(len(righe_sede)-1)]: righe_sede[indice_riga_sede] = nuova_riga_sede
        else: righe_sede[indice_riga_sede] = nuova_riga_sede + '\n'

    with open(file_sede, 'w') as f_sede:
        f_sede.writelines(righe_sede)

    # Aggiorna Numero_clienti_diretti
    with open(file_dipendente, 'r') as f_dipendente:
        righe_dipendente = f_dipendente.readlines()

    for riga_dipendente in righe_dipendente[1:]:
        codice_dipendente = riga_dipendente.strip().split(';')[0]
        # Conta i contratti associati al codice_dipendente
        codici_cliente = []
        with open(file_contratto, 'r') as f_contratti:
            righe_contratti = f_contratti.readlines()
            # Itera attraverso le righe a partire dalla seconda riga
            for riga in righe_contratti[1:]:
                valori_riga = riga.strip().split(';')
                if (valori_riga[2] == str(codice_dipendente)) and (valori_riga[1] not in codici_cliente):
                    codici_cliente.append(valori_riga[1])

        numero_clienti = len(codici_cliente)

        # Aggiorna il valore di Numero_clienti_diretti nel file_dipendente
        nuovi_valori_dipendente = riga_dipendente.strip().split(';')
        nuovi_valori_dipendente[-1] = str(numero_clienti)
        nuova_riga_dipendente = ';'.join(nuovi_valori_dipendente)

        indice_riga_dipendente = righe_dipendente.index(riga_dipendente)
        if riga_dipendente == righe_dipendente[(len(righe_dipendente)-1)]: righe_dipendente[indice_riga_dipendente] = nuova_riga_dipendente
        else: righe_dipendente[indice_riga_dipendente] = nuova_riga_dipendente + '\n'

    with open(file_dipendente, 'w') as f_dipendente:
        f_dipendente.writelines(righe_dipendente)

# Chiamata della funzione per aggiornare i numeri
aggiorna_numeri('sede.txt', 'dipendente.txt', 'contratto.txt')


def inserimento(file):
    
    visualizza(file)

    # Ottieni la prima riga
    attributi = leggi_attributi(file)

    # Chiedi in input i nuovi valori
    nuovi_valori = []
    for i, attributo in enumerate(attributi):
        if(i==0):
            # Il primo attributo è il codice primario, che verrà generato automaticamente
            continue
        elif(attributo=='Codice_dipendente'):
            codice = -1
            fcod = 'dipendente.txt' 
            while(not codice_esiste(fcod, codice)):
                try:
                    codice = int(input(f"Inserisci il nuovo valore numerico per {attributo}: "))
                except ValueError:
                    print("Devi inserire un numero!!!\n")
                if not codice_esiste(fcod, codice):
                    print(f"Errore: Il Codice {codice} non esiste nel file {fcod} non può essere inserito")
            nuovi_valori.append(codice)
        elif(attributo=='Codice_cliente'):
            codice = -1
            fcod = 'cliente.txt' 
            while(not codice_esiste(fcod, codice)):
                try:
                    codice = int(input(f"Inserisci il nuovo valore numerico per {attributo}: "))
                except ValueError:
                    print("Devi inserire un numero!!!\n")
                if not codice_esiste(fcod, codice):
                    print(f"Errore: Il Codice {codice} non esiste nel file {fcod} non può essere inserito")
            nuovi_valori.append(codice)
        elif(attributo=='Codice_sede'):
            codice = -1
            fcod = 'sede.txt' 
            while(not codice_esiste(fcod, codice)):
                try:
                    codice = int(input(f"Inserisci il nuovo valore numerico per {attributo}: "))
                except ValueError:
                    print("Devi inserire un numero!!!\n")
                if not codice_esiste(fcod, codice):
                    print(f"Errore: Il Codice {codice} non esiste nel file {fcod} non può essere inserito")
            nuovi_valori.append(codice)
        elif(attributo=='Numero_clienti_diretti'): nuovi_valori.append('-')
        elif(attributo=='Numero_dipendenti_sede'): nuovi_valori.append('-')
        else:
            nuovo_valore = input(f"Inserisci il nuovo valore per {attributo}: ")

            if attributo == "Data_di_nascita":
                # Controllo per la data nel formato aaaa-mm-gg
                while not(len(nuovo_valore) == 10 and nuovo_valore[4] == nuovo_valore[7] == "-" or nuovo_valore=='-'):
                    if len(nuovo_valore) == 10 and nuovo_valore[4] == nuovo_valore[7] == "-" or nuovo_valore=='-':
                        nuovi_valori.append(nuovo_valore)
                    else:
                        print("Formato data non valido. Inserisci nel formato aaaa-mm-gg.")
                        nuovo_valore = input(f"Inserisci il nuovo valore per {attributo}: ")
            elif attributo == "e-mail":
                # Controllo per la presenza della @
                while not("@" in nuovo_valore or nuovo_valore=='-'):
                    if "@" in nuovo_valore or nuovo_valore=='-':
                        nuovi_valori.append(nuovo_valore)
                    else:
                        print("Indirizzo e-mail non valido. Assicurati di includere '@' nell'indirizzo.")
                        nuovo_valore = input(f"Inserisci il nuovo valore per {attributo}: ")
            elif attributo == "Posizione_lavorativa":
                # Controllo per le posizioni lavorative valide
                validi = ["Programmatore", "Dipendente", "Analista", "Manager"]
                while not(nuovo_valore in validi or nuovo_valore=='-'):
                    if nuovo_valore in validi or nuovo_valore=='-':
                        nuovi_valori.append(nuovo_valore)
                    else:
                        print("Posizione lavorativa non valida. Le posizioni valide sono:", ", ".join(validi))
                        nuovo_valore = input(f"Inserisci il nuovo valore per {attributo}: ")
            elif attributo == "Stato_progetto":
                # Controllo per gli stati del progetto validi
                validi = ["In corso", "Approvato"]
                while not(nuovo_valore in validi or nuovo_valore=='-'):
                    if nuovo_valore in validi or nuovo_valore=='-':
                        nuovi_valori.append(nuovo_valore)
                    else:
                        print("Stato del progetto non valido. Gli stati validi sono:", ", ".join(validi))
                        nuovo_valore = input(f"Inserisci il nuovo valore per {attributo}: ")
            elif attributo == "Stato_civile":
                # Controllo per gli stati del progetto validi
                validi = ["Sposato", "Single"]
                while not(nuovo_valore in validi or nuovo_valore=='-'):
                    if nuovo_valore in validi or nuovo_valore=='-':
                        nuovi_valori.append(nuovo_valore)
                    else:
                        print("Stato del progetto non valido. Gli stati validi sono:", ", ".join(validi))
                        nuovo_valore = input(f"Inserisci il nuovo valore per {attributo}: ")
                
            nuovi_valori.append(nuovo_valore)

    # Genera un nuovo codice primario
    with open(file, 'r') as f:
        righe = f.readlines()

    # Estrai l'ultimo codice primario presente nel file
    if righe:
        ultimo_codice = righe[-1].split(';')[0]
        codice_primario = int(ultimo_codice) + 1
    else:
        codice_primario = 1

    # Costruisci la nuova riga del file
    valori_finali = [str(codice_primario)] + [str(valore) for valore in nuovi_valori]
    nuova_riga = ';'.join(valori_finali)

    # Aggiungi la nuova riga al file
    with open(file, 'a') as f:
        f.write('\n' + nuova_riga)

    print(f"Inserimento completato per il Codice {codice_primario} nel file {file}.")

    # Visualizza il file aggiornato
    visualizza(file)

def modifica(file):
    
    visualizza(file)

    codice_primario = -1
    
    while(not codice_esiste(file, codice_primario)):
        try:
            codice_primario = int(input("Inserisci il numero del Codice primario della riga che desideri modificare:\n "))
        except ValueError:
            print("ho detto un numero!!!\n")
        if not codice_esiste(file, codice_primario):
            print(f"Errore: Il Codice {codice_primario} non esiste nel file {file} non puo essere modificato")

    # Ottieni la prima riga
    attributi = leggi_attributi(file)

    # Chiedi in input i nuovi valori
    nuovi_valori = []
    for i, attributo in enumerate(attributi):
        if(i==0):
            nuovi_valori.append(codice_primario)
        elif(attributo=='Codice_dipendente'):
            codice = -1
            fcod = 'dipendente.txt' 
            while(not codice_esiste(fcod, codice)):
                try:
                    codice = int(input(f"Inserisci il nuovo valore numerico per {attributo} (o '-' per mantenere invariato): "))
                except ValueError:
                    print("ho detto un numero!!!\n")
                if not codice_esiste(fcod, codice):
                    print(f"Errore: Il Codice {codice} non esiste nel file {fcod} non puo essere inseito")
            nuovi_valori.append(codice)
        elif(attributo=='Codice_cliente'):
            codice = -1
            fcod = 'cliente.txt' 
            while(not codice_esiste(fcod, codice)):
                try:
                    codice = int(input(f"Inserisci il nuovo valore numerico per {attributo} (o '-' per mantenere invariato): "))
                except ValueError:
                    print("ho detto un numero!!!\n")
                if not codice_esiste(fcod, codice):
                    print(f"Errore: Il Codice {codice} non esiste nel file {fcod} non puo essere inseito")
            nuovi_valori.append(codice)
        elif(attributo=='Codice_sede'):
            codice = -1
            fcod = 'sede.txt' 
            while(not codice_esiste(fcod, codice)):
                try:
                    codice = int(input(f"Inserisci il nuovo valore numerico per {attributo} (o '-' per mantenere invariato): "))
                except ValueError:
                    print("ho detto un numero!!!\n")
                if not codice_esiste(fcod, codice):
                    print(f"Errore: Il Codice {codice} non esiste nel file {fcod} non puo essere inseito")
            nuovi_valori.append(codice)
        elif(attributo=='Numero_clienti_diretti'): nuovi_valori.append('-')
        elif(attributo=='Numero_dipendenti_sede'): nuovi_valori.append('-')
        else:
            nuovo_valore = input(f"Inserisci il nuovo valore per {attributo} (o '-' per mantenere invariato): ")

            if attributo == "Data_di_nascita":
                # Controllo per la data nel formato aaaa-mm-gg
                while not(len(nuovo_valore) == 10 and nuovo_valore[4] == nuovo_valore[7] == "-" or nuovo_valore=='-'):
                    if len(nuovo_valore) == 10 and nuovo_valore[4] == nuovo_valore[7] == "-" or nuovo_valore=='-':
                        nuovi_valori.append(nuovo_valore)
                    else:
                        print("Formato data non valido. Inserisci nel formato aaaa-mm-gg.")
                        nuovo_valore = input(f"Inserisci il nuovo valore per {attributo} (o '-' per mantenere invariato): ")
            elif attributo == "e-mail":
                # Controllo per la presenza della @
                while not("@" in nuovo_valore or nuovo_valore=='-'):
                    if "@" in nuovo_valore or nuovo_valore=='-':
                        nuovi_valori.append(nuovo_valore)
                    else:
                        print("Indirizzo e-mail non valido. Assicurati di includere '@' nell'indirizzo.")
                        nuovo_valore = input(f"Inserisci il nuovo valore per {attributo} (o '-' per mantenere invariato): ")
            elif attributo == "Posizione_lavorativa":
                # Controllo per le posizioni lavorative valide
                validi = ["Programmatore", "Dipendente", "Analista", "Manager"]
                while not(nuovo_valore in validi or nuovo_valore=='-'):
                    if nuovo_valore in validi or nuovo_valore=='-':
                        nuovi_valori.append(nuovo_valore)
                    else:
                        print("Posizione lavorativa non valida. Le posizioni valide sono:", ", ".join(validi))
                        nuovo_valore = input(f"Inserisci il nuovo valore per {attributo} (o '-' per mantenere invariato): ")
            elif attributo == "Stato_progetto":
                # Controllo per gli stati del progetto validi
                validi = ["In corso", "Approvato"]
                while not(nuovo_valore in validi or nuovo_valore=='-'):
                    if nuovo_valore in validi or nuovo_valore=='-':
                        nuovi_valori.append(nuovo_valore)
                    else:
                        print("Stato del progetto non valido. Gli stati validi sono:", ", ".join(validi))
                        nuovo_valore = input(f"Inserisci il nuovo valore per {attributo} (o '-' per mantenere invariato): ")
            elif attributo == "Stato_civile":
                # Controllo per gli stati del progetto validi
                validi = ["Sposato", "Single"]
                while not(nuovo_valore in validi or nuovo_valore=='-'):
                    if nuovo_valore in validi or nuovo_valore=='-':
                        nuovi_valori.append(nuovo_valore)
                    else:
                        print("Stato del progetto non valido. Gli stati validi sono:", ", ".join(validi))
                        nuovo_valore = input(f"Inserisci il nuovo valore per {attributo} (o '-' per mantenere invariato): ")
                
            nuovi_valori.append(nuovo_valore)


    # Leggi tutte le righe del file ed estrapola indice e vecchi valori
    with open(file, 'r') as f:
        righe = f.readlines()

    vecchi_valori = []
    indice_riga = -1
    for i, riga in enumerate(righe):
        if riga.startswith(str(codice_primario) + ';'):
            indice_riga = i
            vecchi_valori = riga.strip().split(';')
            break
    
    # Costruisci la nuova riga del file
    valori_finali = []
    for i, valore in enumerate(nuovi_valori):
        if(valore=='-'):
            valori_finali.append(str(vecchi_valori[i]))
        else:
            valori_finali.append(str(valore))

    nuova_riga = ';'.join(valori_finali)

    # Sostituisci la riga con i nuovi dati
    righe[indice_riga] = nuova_riga + '\n'

    # Scrivi le righe modificate nel file
    with open(file, 'w') as f:
        f.writelines(righe)

    print(f"Modifica completata per il Codice {codice_primario} nel file {file}.")

    visualizza(file)

def cancellazione(file):
    visualizza(file)
    scelta=4
    while not (scelta == '1' or scelta == '2' or scelta == '3'):
        scelta = input("Vuoi eliminare tutti i dati del file o solo una riga?\n1-Tutti i dati\n2-Una riga\n3-annulla\n: ")

        if scelta == '1':
            conferma = 'h'
            while not (conferma == 's' or conferma == 'n'):
                conferma = input(f"Sei sicuro di voler eliminare tutti i dati del file {file}? (s/n): ")
                if conferma == 's':
                    prima = ';'.join(leggi_attributi(file))
                    with open(file, 'w') as f:
                        f.write(prima)
                    print(f"Tutti i dati del file {file} sono stati eliminati ora il file è così:\n")
                    visualizza(file)
                    break
                else:
                    print("Operazione annullata.")
        elif scelta == '2':
            codice = -1
            while(not codice_esiste(file, codice)):
                try:
                    codice = input("Inserisci il numero del Codice numerico primario della riga che desideri eliminare: ")
                except ValueError:
                    print("ho detto un numero!!!\n")
                if codice_esiste(file, codice):
                    conferma = 'h'
                    while not (conferma == 's' or conferma == 'n'):
                        conferma = input(f"Sei sicuro di voler eliminare la riga con il Codice {codice}? (s/n):")
                        if conferma == 's':
                            # Leggi tutte le righe del file ed estrapola indice e vecchi valori
                            with open(file, 'r') as f:
                                righe = f.readlines()

                            nuove_righe = []
                            for riga in righe:
                                if riga.startswith(str(codice) + ';'):
                                    continue
                                else:
                                    nuove_righe.append(riga)

                            # Sovrascrivi il file con le nuove righe che escludono quella da eliminare
                            with open(file, 'w') as f:
                                f.writelines(nuove_righe)
                            
                            print(f"La riga con il Codice {codice} è stata eliminata dal file {file}:\n")
                            visualizza(file)
                            return
                        else:
                            print("Operazione annullata.")
                else:
                    print(f"Non esiste una riga con il Codice {codice} nel file {file}.")
        elif scelta == '3': break
        else: print("Scelta non valida.")

def numero(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        num_records = len(lines) - 1  # Sottrai 1 per escludere gli attributi
    print(f"Il numero di record nel file {file} è: {num_records}")

def clienti_per_dipendente(file):

    codice_dipendente = -1
    
    while(not codice_esiste(file, codice_dipendente)):
        try:
            codice_dipendente = int(input("Inserisci il numero del Codice_dipendente del dipendente del quale vuoi sapere il numero di clienti con cui ha stipulato un contratto:\n "))
        except ValueError:
            print("ho detto un numero!!!\n")
        if not codice_esiste(file, codice_dipendente):
            print(f"Errore: Il Codice {codice_dipendente} non esiste nel file {file}")

    codici_cliente = []
    with open('contratto.txt', 'r') as f_contratti:
        righe_contratti = f_contratti.readlines()
        # Itera attraverso le righe a partire dalla seconda riga
        for riga in righe_contratti[1:]:
            valori_riga = riga.strip().split(';')
            if (valori_riga[2] == str(codice_dipendente)) and (valori_riga[1] not in codici_cliente):
                codici_cliente.append(valori_riga[1])

    numero_clienti = len(codici_cliente)

    if numero_clienti > 0:
        print(f"Il dipendente con codice {codice_dipendente} ha stipulato contratti con {numero_clienti} clienti, ovvero i seguenti:")
        for codice_cliente in codici_cliente:
            print(f"- Codice cliente: {codice_cliente}")
            with open(file, 'r') as f:
                clienti = f.readlines()
            for cliente in clienti:
                if cliente.startswith(str(codice_cliente) + ';'):
                    print(cliente)
                    break
    else:
        print(f"Il dipendente con codice {codice_dipendente} non ha contratti con clienti.")


# di supporto
def leggi_attributi(file):
    with open(file, 'r') as f:
        prima_riga = f.readline()
    return prima_riga.strip().split(';')

def codice_esiste(file, codice):
    with open(file, 'r') as f:
        for line in f:
            if line.startswith(str(codice) + ';'): #se inizia con questo vero
                return True
    return False

def visualizza(file):
    if file == 'contratto.txt' :
        print(';'.join(leggi_attributi(file)))
        nuove_righe = []
        with open(file, 'r') as f:
            righe = f.readlines()
            for riga in righe[1:]:
                nuove_righe.append(riga.strip().split(';'))
        for riga in nuove_righe[1:]:
            riga[1]=Nome_e_Cognome(riga[1], 'cliente.txt')
            riga[2]=Nome_e_Cognome(riga[2], 'dipendente.txt')
            print(';'.join(riga))
    elif file == 'dipendente.txt':
        print(';'.join(leggi_attributi(file)))
        nuove_righe = []
        with open(file, 'r') as f:
            righe = f.readlines()
            for riga in righe[1:]:
                nuove_righe.append(riga.strip().split(';'))
        for riga in nuove_righe[1:]:
            riga[13]=Nome_e_Cognome(riga[13], 'sede.txt')
            print(';'.join(riga))
    else:
        with open(file, "r") as f: 
            for line in f: 
                print(line.strip()) 

def Nome_e_Cognome(codice, file):
    if file=='sede.txt':
        with open(file, 'r') as f:
            for line in f:
                if line.startswith(str(codice) + ';'): #se inizia con questo vero
                    riga=line.strip().split(';')
                    nominativo=riga[1]
                    break
    else:
        with open(file, 'r') as f:
            for line in f:
                if line.startswith(str(codice) + ';'): #se inizia con questo vero
                    riga=line.strip().split(';')
                    nominativo=riga[1]+' '+riga[2]
                    break
    return nominativo

o='el'
while(o=='el'):
    fileop=404
    while(fileop<1 or fileop>5):
        try:
            fileop=int(input("Inserisci il numero dell'file sul quale vuoi svolgere le operazioni:\n1-sede\n2-dipendente\n3-cliente\n4-contratto\n5-esci\n: "))
        except ValueError:
            print("ho detto un numero!!!\n")
        if(fileop<1 or fileop>5):
            print("non penso che sia un opzione\n")
        if(fileop==5):
            print('Addio!!!')
            exit()

    if(fileop==1): #inserimento, modifica, cancellazione
        file='sede.txt' 
        lim=6
    elif(fileop==2):#inserimento, modifica, cancellazione, numero dipendenti, clienti per dipendente
        file='dipendente.txt' 
        lim=8
    elif(fileop==3): #inserimento, modifica, cancellazione, numero clienti
        file='cliente.txt' 
        lim=7
    else: #inserimento, modifica
        file='contratto.txt' 
        lim=5

    op=404
    while(op<1 or op>lim):
        try:
            print(f"Inserisci il numero dell'operazione che si vuole fare sul file {file}:\n1-inserimento\n2-modifica")
            if(lim==6): print("3-cancellazione\n4-visualizza\n5-annulla\n6-esci ")
            elif(lim==7): print("3-cancellazione\n4-numero di clienti\n5-visualizza\n6-annulla\n7-esci")
            elif(lim==5): print("3-visualizza\n4-annulla\n5-esci")
            else: print("3-cancellazione\n4-numero dei dipendenti\n5-clienti per dipendente\n6-visualizza\n7-annulla\n8-esci")
            op=int(input(": "))
        except ValueError:
            print("ho detto un numero!!!\n")
        if(op<1 or op>lim):
            print("non penso che sia un opzione\n")

    if(op==lim-1): o='el'
    elif(op==lim-2): visualizza(file)
    elif(op==lim): exit()
    elif(op==1): inserimento(file)
    elif(op==2): modifica(file)
    elif(op==3): cancellazione(file)
    elif(op==4): numero(file)
    else: clienti_per_dipendente(file)

    # Chiamata della funzione per aggiornare i numeri
    aggiorna_numeri('sede.txt', 'dipendente.txt', 'contratto.txt')