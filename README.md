# Coffee-median-report

Скрипт вычисляет медиану потребления кофе для каждого студента по данным из CSV-файлов.

## Пример запуска

```bash
python src/main.py --files data/math.csv data/physics.csv data/programming.csv --report median-coffee
```

### Параметры

--files — список CSV-файлов с данными (обязательный, минимум один файл).

--report — название отчета с результатом (обязательный).