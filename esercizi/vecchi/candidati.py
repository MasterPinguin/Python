from random import randrange

p1=randrange(1,100)
p2=100-p1
n1="Donald Trump"
n2="Mario Draghi"
if(p1>p2):
    win=n1
elif(p2>p1):
    win=n2
else:
    win="nessun'"

print(f"""/

Alla fine della giornata delle elezioni per il ballottaggio tra {n1} e {n1}
I risultati sono:
{n1:^30}{n2:^30}
{p1:>15}%{p2:>30}%
con {win} vincitore
      
""")