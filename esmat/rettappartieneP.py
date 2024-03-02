t = True
while t:
    try:
        m = float(input("Inserisci i dati della prima retta y=mx+q:\nAttenzione m deve essere diversa da 0 o ti verra chiesto di reinserire i dti!!!\nm: "))
        q = float(input("q: "))
        xp = float(input("Inserisci il punto P di coordinate (xp, yp):\nxp: "))
        yp = float(input("yp: "))
        if m!=0: t=False
    except (NameError, ValueError, TypeError, SyntaxError) as errore:
        print("Hai inserito dei caratteri al posto di un numero. L'errore potrebbe essere legato all'utilizzo della ',' al posto del '.'")

if (m*xp)+q == yp:
    print(f"il punto P di coordinate ({str(xp).rstrip('0').rstrip('.') if '.' in str(xp) else str(xp)};{str(yp).rstrip('0').rstrip('.') if '.' in str(yp) else str(yp)}) è coincidente alla retta y={str(m).rstrip('0').rstrip('.') if '.' in str(m) else str(m)}x{'+'+str(q).rstrip('0').rstrip('.') if '.' in str(q) else str(q) if q > 0 else '-'+str(q).rstrip('0').rstrip('.') if '.' in str(q) else str(q) if q < 0 else ''}")
else:
    print(f"il punto P di coordinate ({str(xp).rstrip('0').rstrip('.') if '.' in str(xp) else str(xp)};{str(yp).rstrip('0').rstrip('.') if '.' in str(yp) else str(yp)}) non è coincidente alla retta y={str(m).rstrip('0').rstrip('.') if '.' in str(m) else str(m)}x{'+'+str(q).rstrip('0').rstrip('.') if '.' in str(q) else str(q) if q > 0 else '-'+str(q).rstrip('0').rstrip('.') if '.' in str(q) else str(q) if q < 0 else ''}")