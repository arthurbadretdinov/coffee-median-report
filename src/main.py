from tabulate import tabulate

from cli import REPORTS, parse_arguments
from csv_reader import read_csv


def main():
    args = parse_arguments()
    
    all_rows = []
    for file_path in args.files:
        all_rows.extend(read_csv(file_path))
    
    report_func = REPORTS[args.report]
    result = report_func(all_rows)
    
    print(tabulate(result.items(), headers=["student", "median_coffee"], tablefmt="grid"))


if __name__ == "__main__":
    main()