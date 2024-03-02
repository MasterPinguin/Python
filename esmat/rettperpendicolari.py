t = True
while t:
    try:
        m1 = float(input("Inserisci i dati della prima retta y=m1x+q1:\nAttenzione m1 deve essere diversa da 0 o ti verra chiesto di reinserire i dti!!!\nm1: "))
        q1 = float(input("q1: "))
        m2 = float(input("Inserisci i dati della seconda retta y=m2x+q2:\nAttenzione m2 deve essere diversa da 0 o ti verra chiesto di reinserire i dti!!!\nm2: "))
        q2 = float(input("q2: "))
        if m1!=0 or m2!=0: t=False 
    except (NameError, ValueError, TypeError, SyntaxError) as errore:
        print("Hai inserito dei caratteri al posto di un numero. L'errore potrebbe essere legato all'utilizzo della ',' al posto del '.'")

if m1*m2 == -1:
    print(f"le due rette y={str(m1).rstrip('0').rstrip('.') if '.' in str(m1) else str(m1)}x{'+'+str(q1).rstrip('0').rstrip('.') if '.' in str(q1) else str(q1) if q1 > 0 else '-'+str(q1).rstrip('0').rstrip('.') if '.' in str(q1) else str(q1) if q1 < 0 else ''} e y={str(m2).rstrip('0').rstrip('.') if '.' in str(m2) else str(m2)}x{'+'+str(q2).rstrip('0').rstrip('.') if '.' in str(q2) else str(q2) if q2 > 0 else '-'+str(q2).rstrip('0').rstrip('.') if '.' in str(q2) else str(q2) if q2 < 0 else ''} sono due rette perpendicolari l'una all'altra")
else:
    print(f"le due rette y={str(m1).rstrip('0').rstrip('.') if '.' in str(m1) else str(m1)}x{'+'+str(q1).rstrip('0').rstrip('.') if '.' in str(q1) else str(q1) if q1 > 0 else '-'+str(q1).rstrip('0').rstrip('.') if '.' in str(q1) else str(q1) if q1 < 0 else ''} e y={str(m2).rstrip('0').rstrip('.') if '.' in str(m2) else str(m2)}x{'+'+str(q2).rstrip('0').rstrip('.') if '.' in str(q2) else str(q2) if q2 > 0 else '-'+str(q2).rstrip('0').rstrip('.') if '.' in str(q2) else str(q2) if q2 < 0 else ''} non sono due rette perpendicolari l'una all'altra")