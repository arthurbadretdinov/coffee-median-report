import pytest
from contextlib import nullcontext as does_not_raise

from validations import validate_data, HEADER, NUMERIC_FIELD

valid_data1 = [
    HEADER,
    ['Алексей Смирнов', '2024-06-01', '450', '4.5', '12', 'норм', 'Математика']
]

valid_data2 = [
    HEADER,
    ['Алексей Смирнов', '2024-06-01', '450', '4.5', '12', 'норм', 'Математика'],
    ['Дарья Петрова', '2024-06-01', '200', '7.0', '6', 'отл', 'Математика']
]

invalid_header = [
    ['student',
    'date',
    'coffee_spent',
    'sleep_hours',
    'study_hours',
    'mood',
    'exam',
    'score'
    ],
    ['Алексей Смирнов', '2024-06-01', '450', '4.5', '12', 'норм', 'Математика']
]

only_header = [HEADER]

invalid_row_length1 = [
    HEADER,
    ['Алексей Смирнов', '2024-06-01', '450', '4.5', '12', 'норм']
]

invalid_row_length2 = [
    HEADER,
    ['Алексей Смирнов', '2024-06-01', '450', '4.5', '12', 'норм', 'Математика', '5']
]

invalid_type = [
    HEADER,
    ['Алексей Смирнов', '2024-06-01', '450', '4.5', 'A', 'норм', 'Математика']
]


@pytest.mark.parametrize(
    "data_list, expectation", 
    [
        (valid_data1, does_not_raise()), 
        (invalid_header, pytest.raises(ValueError, match='Invalid header')), # неправильный header
        (only_header, pytest.raises(ValueError, match='No data found')), # нет данных
        (invalid_row_length1, pytest.raises(ValueError, match='Invalid row length')), # неправильная длина строки (меньше нужного)
        (invalid_row_length2, pytest.raises(ValueError, match='Invalid row length')), # неправильная длина строки (больше нужного)
        (invalid_type, pytest.raises(ValueError, match='could not convert')), # неправильный тип данных
    ]
)
def test_validate_data_errors(data_list, expectation):
    with expectation:
        validate_data(data_list)
        
        
@pytest.mark.parametrize(
    "data_list", 
    [
        valid_data1, 
        valid_data2,
    ]
)
def test_validate_data_correct(data_list):
    result = validate_data(data_list)
    
    assert isinstance(result, list)
    assert len(result) > 0
    
    for row in result:
        assert isinstance(row, dict)
        assert len(row) == len(HEADER)
        
        for key in HEADER:
            assert key in row
            
        for col, col_type in NUMERIC_FIELD.items():
            assert isinstance(row[col], col_type)