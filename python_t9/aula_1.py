import csv

with open('aula_1.csv', mode='r') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        print(f"NOME: {row['NOME']}, IDADE: {row['IDADE']}, CPF: {row['CPF']}, EMAIL: {row['EMAIL']}")