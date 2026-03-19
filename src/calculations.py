from collections import defaultdict
import statistics


def calculate_median_coffee(rows):
    students_spent = defaultdict(list)
    for row in rows:
        students_spent[row["student"]].append(row["coffee_spent"])

    median_spent = {}
    for student, coffee_spent_list in students_spent.items():
        median_spent[student] = statistics.median(coffee_spent_list)

    return dict(sorted(median_spent.items(), key=lambda x: x[1], reverse=True))
