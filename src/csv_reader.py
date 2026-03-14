import csv


def read_csv(file_path):
    with open(file_path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)