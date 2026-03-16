import pytest

from calculations import calculate_median_coffee

data_empty = []

result_empty = {}

data1 = [
    {'student': 'Алексей Смирнов', 'coffee_spent': 450.0},
]

result1 = {
    'Алексей Смирнов': 450.0
}

data2 = [
    {'student': 'Алексей Смирнов', 'coffee_spent': 450.0},
    {'student': 'Алексей Смирнов', 'coffee_spent': 550.0},
    {'student': 'Дарья Петрова', 'coffee_spent': 200.0},
    {'student': 'Дарья Петрова', 'coffee_spent': 250.0},
    {'student': 'Дарья Петрова', 'coffee_spent': 350.0},
]

result2 = {
    'Алексей Смирнов': 500.0,
    'Дарья Петрова': 250.0
}

data3 = [
    {'student': 'Алексей Смирнов', 'coffee_spent': 450.0},
    {'student': 'Иван Кузнецов', 'coffee_spent': 550.0},
    {'student': 'Дарья Петрова', 'coffee_spent': 200.0},
    {'student': 'Елена Волкова', 'coffee_spent': 250.0},
    {'student': 'Сергей Козлов', 'coffee_spent': 350.0},
]

result3 = {
    'Иван Кузнецов': 550.0,
    'Алексей Смирнов': 450.0,
    'Сергей Козлов': 350.0,
    'Елена Волкова': 250.0,
    'Дарья Петрова': 200.0
}


@pytest.mark.parametrize(
    "rows, result", 
    [
        (data_empty, result_empty), 
        (data1, result1),
        (data2, result2),
        (data3, result3),
    ]
)
def test_calculate_median_coffee(rows, result):
    assert calculate_median_coffee(rows) == result