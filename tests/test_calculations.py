import pytest

from models import StudentRecord
from reports.median_coffee import MedianCoffeeReport

data_empty: list[StudentRecord] = []

result_empty: dict[str, float] = {}

data1: list[StudentRecord] = [
    {"student": "Алексей Смирнов", "coffee_spent": 450.0},
]

result1: dict[str, float] = {"Алексей Смирнов": 450.0}

data2: list[StudentRecord] = [
    {"student": "Алексей Смирнов", "coffee_spent": 450.0},
    {"student": "Алексей Смирнов", "coffee_spent": 550.0},
    {"student": "Дарья Петрова", "coffee_spent": 200.0},
    {"student": "Дарья Петрова", "coffee_spent": 250.0},
    {"student": "Дарья Петрова", "coffee_spent": 350.0},
]

result2: dict[str, float] = {"Алексей Смирнов": 500.0, "Дарья Петрова": 250.0}

data3: list[StudentRecord] = [
    {"student": "Алексей Смирнов", "coffee_spent": 450.0},
    {"student": "Иван Кузнецов", "coffee_spent": 550.0},
    {"student": "Дарья Петрова", "coffee_spent": 200.0},
    {"student": "Елена Волкова", "coffee_spent": 250.0},
    {"student": "Сергей Козлов", "coffee_spent": 350.0},
]

result3: dict[str, float] = {
    "Иван Кузнецов": 550.0,
    "Алексей Смирнов": 450.0,
    "Сергей Козлов": 350.0,
    "Елена Волкова": 250.0,
    "Дарья Петрова": 200.0,
}


@pytest.mark.parametrize(
    "rows, result",
    [
        (data_empty, result_empty),
        (data1, result1),
        (data2, result2),
        (data3, result3),
    ],
)
def test_calculate_median_coffee(
    rows: list[StudentRecord], result: dict[str, float]
) -> None:
    report = MedianCoffeeReport()
    assert report.calculate(rows) == result
