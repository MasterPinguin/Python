def acquisisci_materia():
    materia = input("Inserisci la materia da controllare: ")
    return materia

def acquisisci_dati_docenti():
    n = int(input("Quanti docenti vuoi inserire? "))
    docenti = []
    for i in range(n):
        cognome = input(f"Inserisci il cognome del docente {i + 1}: ")
        materia = input(f"Inserisci la materia di insegnamento del docente {i + 1}: ")
        docenti.append((cognome, materia))
    return docenti

def conta_docenti_per_materia(docenti, materia):
    count = 0
    for _, materia_insegnamento in docenti:
        if materia_insegnamento == materia:
            count += 1
    return count


materia_da_controllare = acquisisci_materia()
dati_docenti = acquisisci_dati_docenti()
count = conta_docenti_per_materia(dati_docenti, materia_da_controllare)

print(f"I docenti che insegnano {materia_da_controllare} sono {count}.")
