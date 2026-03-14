import argparse

from csv_reader import read_csv


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs='+', type=str, required=True)
    args = parser.parse_args()
    
    all_rows = []
    for file_path in args.files:
        all_rows.extend(read_csv(file_path))
    print(all_rows)
    

if __name__ == "__main__":
    main()