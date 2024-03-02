class MacchinaLavorazione:
    def __init__(self):
        self.coda_alta_priorita = []
        self.coda_bassa_priorita = []

    def aggiungi_lavorazione(self, codice, priorita):
        if priorita == 0:
            self.coda_alta_priorita.insert(0, codice)
        elif priorita == 1:
            self.coda_alta_priorita.append(codice)
        elif priorita == 2:
            self.coda_bassa_priorita.append(codice)
        else:
            print("Priorità non valida")

    def esegui_lavorazione(self):
        # con la funzione pop rimuovo l'elemento specificato dalla lista e ne prendo il valore in un unico passaggio
        if self.coda_alta_priorita:
            lavorazione = self.coda_alta_priorita.pop(0)
            print(f"Esecuzione della lavorazione {lavorazione}")
        elif self.coda_bassa_priorita:
            lavorazione = self.coda_bassa_priorita.pop(0)
            print(f"Esecuzione della lavorazione {lavorazione}")
        else:
            print("Nessuna lavorazione in coda.")

# Esempio di utilizzo
macchina = MacchinaLavorazione()
macchina.aggiungi_lavorazione("L1", 0)
macchina.aggiungi_lavorazione("L2", 1)
macchina.aggiungi_lavorazione("L3", 2)
macchina.aggiungi_lavorazione("L4", 0)
macchina.aggiungi_lavorazione("L5", 1)
macchina.aggiungi_lavorazione("L6", 2)
macchina.aggiungi_lavorazione("L7", 2)
macchina.aggiungi_lavorazione("L8", 1)
macchina.aggiungi_lavorazione("L9", 0)
macchina.aggiungi_lavorazione("L10", 1)

for i in range(15):
    macchina.esegui_lavorazione()

