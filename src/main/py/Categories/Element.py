from Categories.FinancialTypes import FinancialType
from Categories.UnknownFinancialTypeError import UnknownFinancialTypeError


class Element:
    """An element containing an amount of money; either income, saving or cost. """
    def __init__(self, value: float, financial_type: FinancialType = FinancialType.INCOME):
        if financial_type != FinancialType.INCOME and financial_type != FinancialType.SAVING and financial_type != FinancialType.COST:
            raise UnknownFinancialTypeError(financial_type)

        self._type = financial_type
        if self._type == FinancialType.COST or self._type == FinancialType.SAVING:
            value = value * -1
        self._value = value

    def get_value(self) -> float:
        return self._value

    def get_type(self):
        return self._type