from typing import cast

from models import StudentRecord

HEADER = [
    "student",
    "date",
    "coffee_spent",
    "sleep_hours",
    "study_hours",
    "mood",
    "exam",
]

NUMERIC_FIELD = {"coffee_spent": float, "sleep_hours": float, "study_hours": float}


def validate_data(data_list: list[list[str]]) -> list[StudentRecord]:
    header = data_list[0]
    if header != HEADER:
        raise ValueError("Invalid header")

    rows = data_list[1:]
    if not rows:
        raise ValueError("No data found")

    data_result: list[StudentRecord] = []
    for row in rows:
        if len(row) != len(header):
            raise ValueError("Invalid row length")

        row_dict: dict[str, str | float] = {}
        for col_name, value in zip(header, row):
            if col_name in NUMERIC_FIELD:
                row_dict[col_name] = NUMERIC_FIELD[col_name](value)
            else:
                row_dict[col_name] = value
        data_result.append(cast(StudentRecord, row_dict))
    return data_result
