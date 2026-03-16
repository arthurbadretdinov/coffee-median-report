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

def test_parse_arguments(file_path, expectation):
    with expectation:
        read_csv(file_path)