import csv
from pathlib import Path

def read_csv(file_path):
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"File {file_path} not found")
    
    if not path.is_file():
        raise IsADirectoryError(f"Path {file_path} is not a file")
    
    if path.suffix.lower() != ".csv":
        raise TypeError(f"File {file_path} is not a CSV file")

    if path.stat().st_size == 0:
        raise EOFError(f"File {file_path} is empty")    
    
    with open(path, encoding='utf-8') as f:
        reader = csv.reader(f)
        return list(reader)