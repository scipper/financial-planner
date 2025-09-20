from enum import Enum


class Element:
    """An element containing an amount of money; either income, saving or cost. """
    def __init__(self, value: float, financial_type: str = "income"):
        self._type = financial_type
        if self._type == "cost" or self._type == "saving":
            value = value * -1
        self._value = value

    def get_value(self) -> float:
        return self._value

    def get_type(self):
        return self._type

class FinancialType(Enum):
    INCOME = 1
    SAVING = 2
    COST = 3