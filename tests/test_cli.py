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
                "--report", 
                "median-coffee",
                "--files", 
                "data/math.csv", 
                "data/physics.csv", 
                "data/programming.csv"
            ], does_not_raise()
        ), # чтение трёх файлов
    ]
)
def test_parse_arguments_error(args_list, expectation):
    with expectation:
        parse_arguments(args_list)
        
        
@pytest.mark.parametrize(
    "args_list, files, report", 
    [
        (
            ["--files", "data/math.csv", "--report", "median-coffee"],
            ["data/math.csv"],
            "median-coffee"
        ), 
        (
            [
                "--files", 
                "data/math.csv", 
                "data/physics.csv", 
                "data/chemistry.csv", 
                "--report", 
                "median-coffee"
            ],
            ["data/math.csv", "data/physics.csv", "data/chemistry.csv"],
            "median-coffee"
        ),
        (
            [
                "--report", 
                "median-coffee",
                "--files", 
                "data/math.csv", 
                "data/physics.csv", 
                "data/programming.csv"
            ], 
            ["data/math.csv", "data/physics.csv", "data/programming.csv"],
            "median-coffee"
        ),
    ]
)
def test_parse_arguments_correct(args_list, files, report):
    args = parse_arguments(args_list)
    
    assert args.files == files
    assert args.report == report
