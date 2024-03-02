import time
giri = 0

while(True):
	if giri < 2:
		giri = giri + 1
		num1 = int(input("inserisci numero 1: "))
		num2 = int(input("inserisci numero 2: "))
		segno = input("inserisci 1 per addizione 2 per la divisione 3 per la moltiplicazione e 4 per la sottrazione: ")
		print(giri)
		if segno == "1":
			addizione = num1+num2
			print(addizione)
		elif segno == "2":
			divisione = num1/num2
			print(divisione)
		elif segno == "3":
			moltiplicazione = num1*num2
			print(moltiplicazione)    
		elif segno == "4":
			sottrazione = num1-num2
			print(sottrazione)
	else:
           break