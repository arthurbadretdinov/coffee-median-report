import pytest
from contextlib import nullcontext as does_not_raise

from cli import parse_arguments

@pytest.mark.parametrize(
    "args_list, expectation", 
    [
        ([], pytest.raises(SystemExit)), # нет никаких аргументов
        (["--files", "data/math.csv"], pytest.raises(SystemExit)), # нет аргумента --report
        (["--report", "median-coffee"], pytest.raises(SystemExit)), # нет аргумента --files
        (["--files", "--report", "median-coffee"], pytest.raises(SystemExit)), # нет файлов
        (["--files", "data/math.csv", "--report"], pytest.raises(SystemExit)), # нет отчетов
        (["--files", "data/math.csv", "--report", "avg-coffee"], pytest.raises(SystemExit)), # неизвестный отчет
        (["--files", "data/math.csv", "--report", "median-coffee"], does_not_raise()), # чтение одного файла
        (
            [
                "--files", 
                "data/math.csv", 
                "data/physics.csv", 
                "data/chemistry.csv", 
                "--report", 
                "median-coffee"
            ], does_not_raise()
        ), # чтение трёх файлов
        (
            [
                "--files", 
                "data/math.csv", 
                "data/physics.csv", 
                "data/programming.csv", 
                "--report", 
                "median-coffee"
            ], does_not_raise()
        ), # чтение трёх файлов
    ]
)

def test_parse_arguments(args_list, expectation):
    with expectation:
        parse_arguments(args_list)