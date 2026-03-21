import pytest
from contextlib import nullcontext as does_not_raise
from typing import ContextManager, Any

from csv_reader import read_csv


@pytest.mark.parametrize(
    "file_path, expectation",
    [
        ("data/math.csv", does_not_raise()),  # существующий файл
        ("data/physics.csv", does_not_raise()),  # существующий файл
        ("data/chemistry.csv", pytest.raises(FileNotFoundError)),  # несуществующий файл
        ("data/programming.csv", does_not_raise()),  # существующий файл
        (
            "data/bad_encoding.csv",
            pytest.raises(UnicodeDecodeError),
        ),  # неправильный формат файла
        ("data/empty.csv", pytest.raises(EOFError)),  # пустой файл
        (
            "data/not_csv.txt",
            pytest.raises(TypeError),
        ),  # неправильное расшширение файла
        ("data/folder", pytest.raises(IsADirectoryError)),  # не файл
        ("data/permission_error.csv", pytest.raises(PermissionError)),  # нет прав
    ],
)
def test_read_csv_errors(file_path: str, expectation: ContextManager[Any]) -> None:
    with expectation:
        read_csv(file_path)


@pytest.mark.parametrize(
    "file_path",
    [
        ("data/math.csv"),
        ("data/physics.csv"),
        ("data/programming.csv"),
    ],
)
def test_read_csv_correct(file_path: str) -> None:
    data = read_csv(file_path)

    assert isinstance(data, list)
    assert len(data) > 0


@pytest.mark.parametrize(
    "file_path, column_count",
    [
        ("data/math.csv", 46),
        ("data/physics.csv", 46),
        ("data/programming.csv", 46),
    ],
)
def test_read_csv_row_count(file_path: str, column_count: int) -> None:
    data = read_csv(file_path)

    assert len(data) == column_count
