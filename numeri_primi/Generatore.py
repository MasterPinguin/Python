import csv

np = "numeri_primi/numeri_primi2.csv"
n = 1

try:
    with open(np, "r") as file_csv:
        reader = csv.DictReader(file_csv)
        last_row = None
        for row in reader:
            last_row = row
        if last_row and 'c' in last_row:
            c = int(last_row['c'])
            n = int(last_row['n'])
        else:
            c = 2
except FileNotFoundError:
    c = 2

while True:
    while True:
        n += 1
        x = 1
        while True:
            x += 1
            r = n % x
            kyr = n / 2
            if not (r != 0 and x < kyr):
                break
        if r != 0:
            break
    
    c += 1
    print(f"{c}, {n}")

    with open(np, "a", newline="") as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow([c, n])

    
    if c >= 100000:
        break
