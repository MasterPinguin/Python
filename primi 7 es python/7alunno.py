from random import choice
name = input("alunno: ")
print("INSERIRE I VOTI DELL ALUNNO", name)
data = choice(["15/10/2023", "21/09/2023", "28/09/2023"])
v1 = float(input("VOTO DEL " + data + " :"))
data = choice(["18/12/2023", "23/10/2023", "08/11/2023"])
v2 = float(input("VOTO DEL " + data + " :"))
data = choice(["11/02/2023", "25/04/2023", "02/05/2023"])
v3 = float(input("VOTO DEL " + data + " :"))
media = (v1+v2+v3)/3
if(media>=6):
    x="promosso"
else:
    x="bocciato"
print("la media dell'alunno ",name," è ",media," l'alunno è ",x)