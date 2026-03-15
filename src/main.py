import argparse
from tabulate import tabulate

from csv_reader import read_csv
from calculations import calculate_median_coffee

REPORTS = {
    "median-coffee": calculate_median_coffee
}


def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--files", nargs='+', type=str, required=True)
    parser.add_argument("--report", type=str, required=True, choices=REPORTS.keys())
    
    args = parser.parse_args()
    
    all_rows = []
    for file_path in args.files:
        all_rows.extend(read_csv(file_path))
    
    report_func = REPORTS[args.report]
    result = report_func(all_rows)
    
    print(tabulate(result.items(), headers=["student", "median_coffee"], tablefmt="grid"))


if __name__ == "__main__":
    main()