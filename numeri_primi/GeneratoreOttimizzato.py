import csv

np = "numeri_primi/numeri_primi2.csv"
n = 1
primi = []  # Lista per mantenere i numeri primi trovati

try:
    with open(np, "r") as file_csv:
        reader = csv.DictReader(file_csv)
        last_row = None
        for row in reader:
            last_row = row
        if last_row and 'c' in last_row:
            c = int(last_row['c'])
            n = int(last_row['n'])
            primi = [int(primo) for primo in last_row['n'].split(',')]  # Recupera la lista dei numeri primi
        else:
            c = 2
except FileNotFoundError:
    c = 2

while c <= 10000000:
    n += 1
    is_prime = True

    for primo in primi:
        if primo * primo > n:  # Crivello di Eratostene
            break
        if n % primo == 0:
            is_prime = False
            break

    if is_prime:
        primi.append(n)
        c += 1
        print(f"{c}, {n}")

        with open(np, "a", newline="") as file_csv:
            writer = csv.writer(file_csv)
            writer.writerow([c, n])
