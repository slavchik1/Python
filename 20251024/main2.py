import csv


with open("scores.txt", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    with open("winners.txt", 'a', encoding='utf-8') as w:
        for row in reader:
            if float(row[1]) > 100.0:
                w.write(f"{row[0]}\n")
