# importazione delle tariffe
from tariffe import *

# calcolo della bolletta con le tariffe per le aziende 
def calcolo_aziende(c):
    qv = c*TARIFFA_A
    qf = QF_AZIENDE
    iva = (qv + qf)*PERC_IVA/100
    totale = qv+qf+iva
    risultati(qv,qf,iva,totale)

# calcolo della bolletta con le tariffe per i privati
def calcolo_privati(c):
    # quota variabile
    if c <= T1_FINOA:
        qv=c*T1
    elif c <= T2_FINOA:
        qv =(T1_FINOA * T1)+\
            (c-T1_FINOA)*T2
    else:
        qv =(T1_FINOA * T1)+\
            (T2_FINOA * T1_FINOA)*T2+\
            (c-T2_FINOA)*T3
    qf=QF_PRIVATI
    iva=(qv+qf)*PERC_IVA/100
    totale=qv+qf+iva
    risultati(qv,qf,iva,totale)

# output dei risultati 
def risultati(qv,qf,iva,totale):
    print("Quota variabile: {:10.2f}".format(qv))
    print("Quota fissa:     {:10.2f}".format(qf))
    print("IVA:             {:10.2f}".format(iva))
    print("Totale:          {:10.2f}".format(totale))
