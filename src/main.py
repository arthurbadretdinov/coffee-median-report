from tabulate import tabulate

from cli import REPORTS, parse_arguments
from csv_reader import read_csv
from models import StudentRecord
from validations import validate_data


def main():
    args = parse_arguments()

    all_rows: list[StudentRecord] = []
    for file_path in args.files:
        rows: list[list[str]] = read_csv(file_path)
        all_rows.extend(validate_data(rows))

    report_class = REPORTS[args.report]
    report = report_class()
    result = report.calculate(all_rows)

    print(
        tabulate(result.items(), headers=["student", "median_coffee"], tablefmt="grid")
    )


if __name__ == "__main__":
    main()
