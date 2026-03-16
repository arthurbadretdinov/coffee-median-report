import pytest
from contextlib import nullcontext as does_not_raise

from csv_reader import read_csv

@pytest.mark.parametrize(
    "file_path, expectation", 
    [
        ("data/math.csv", does_not_raise()), # существующий файл
        ("data/physics.csv", does_not_raise()), # существующий файл
        ("data/chemistry.csv", pytest.raises(FileNotFoundError)), # несуществующий файл
        ("data/programming.csv", does_not_raise()), # существующий файл
        ("data/bad_encoding.csv", pytest.raises(UnicodeDecodeError)), # неправильный формат файла
        ("data/empty.csv", pytest.raises(ValueError)), # пустой файл
        ('data/not_csv.txt', pytest.raises(ValueError)), # неправильное расшширение файла
        ("data/folder", pytest.raises(ValueError)), # не файл
        ("data/permission_error.csv", pytest.raises(PermissionError)), # нет прав
    ]
)
def test_read_csv_error(file_path, expectation):
    with expectation:
        read_csv(file_path)


@pytest.mark.parametrize(
    "file_path", 
    [
        ("data/math.csv"), 
        ("data/physics.csv"), 
        ("data/programming.csv"), 
    ]
)
def test_read_csv_correct(file_path):
    data = read_csv(file_path)
    
    assert isinstance(data, list)
    assert len(data) > 0


@pytest.mark.parametrize(
    "file_path, column_count", 
    [
        ("data/math.csv", 46), 
        ("data/physics.csv", 46), 
        ("data/programming.csv", 46), 
    ]
)
def test_read_csv_row_count(file_path, column_count):
    data = read_csv(file_path)
    
    assert len(data) == column_count
