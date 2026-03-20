from typing import TypedDict


class StudentRecord(TypedDict):
    student: str
    date: str
    coffee_spent: float
    sleep_hours: float
    study_hours: float
    mood: str
    exam: str
