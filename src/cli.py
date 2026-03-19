import argparse

from calculations import calculate_median_coffee

REPORTS = {"median-coffee": calculate_median_coffee}


def parse_arguments(args_list=None):
    parser = argparse.ArgumentParser()

    parser.add_argument("--files", nargs="+", type=str, required=True)
    parser.add_argument("--report", type=str, required=True, choices=REPORTS.keys())

    return parser.parse_args(args_list)
