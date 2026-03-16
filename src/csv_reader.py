import csv
from pathlib import Path

def read_csv(file_path):
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"File {file_path} not found")
    
    if not path.is_file():
        raise ValueError(f"Path {file_path} is not a file")
    
    if path.suffix.lower() != ".csv":
        raise ValueError(f"File {file_path} is not a CSV file")

    if path.stat().st_size == 0:
        raise ValueError(f"File {file_path} is empty")    
    
    try:
        with open(path, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)
    except PermissionError:
        raise
    except UnicodeDecodeError:
        raise