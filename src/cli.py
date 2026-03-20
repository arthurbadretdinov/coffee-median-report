import argparse
from typing import Type

from reports.base import Report
from reports.median_coffee import MedianCoffeeReport

REPORTS: dict[str, Type[Report]] = {"median-coffee": MedianCoffeeReport}


def parse_arguments(args_list: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument("--files", nargs="+", type=str, required=True)
    parser.add_argument("--report", type=str, required=True, choices=REPORTS.keys())

    return parser.parse_args(args_list)
