from collections import defaultdict
import statistics
from models import StudentRecord
from reports.base import Report


class MedianCoffeeReport(Report):
    def calculate(self, rows: list[StudentRecord]) -> dict[str, float]:
        students_spent: dict[str, list[float]] = defaultdict(list)
        for row in rows:
            students_spent[row["student"]].append(row["coffee_spent"])

        median_spent: dict[str, float] = {}
        for student, coffee_spent_list in students_spent.items():
            median_spent[student] = statistics.median(coffee_spent_list)

        return dict(sorted(median_spent.items(), key=lambda x: x[1], reverse=True))
