from abc import ABC, abstractmethod
from models import StudentRecord


class Report(ABC):

    @abstractmethod
    def calculate(self, rows: list[StudentRecord]) -> dict[str, float]:
        pass
