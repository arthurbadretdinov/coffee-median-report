import argparse

from csv_reader import read_csv
from calculations import calculate_median_coffee_spent_per_student


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs='+', type=str, required=True)
    args = parser.parse_args()
    
    all_rows = []
    for file_path in args.files:
        all_rows.extend(read_csv(file_path))
    
    result = calculate_median_coffee_spent_per_student(all_rows)
    print(result)
    

if __name__ == "__main__":
    main()