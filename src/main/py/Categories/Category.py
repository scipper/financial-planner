from typing import List

from Categories.Element import Element
from Categories.FinancialTypes import FinancialType
from Categories.UnknownFinancialTypeError import UnknownFinancialTypeError


class Category:
    """A category container 0 or more elements of financial types."""

    def __init__(self):
        self._type = FinancialType.INCOME
        self._elements: List[Element] = []

    def set_type(self, financial_type: FinancialType):
        if financial_type != FinancialType.INCOME and financial_type != FinancialType.SAVING and financial_type != FinancialType.COST:
            raise UnknownFinancialTypeError(financial_type)

        self._type = financial_type

    def add_element(self, element: Element):
        self._elements.append(element)

    def get_sum(self) -> float:
        xxx = -1 if self._type != FinancialType.INCOME else 1
        sum_of_element_values = sum(element.get_value() * xxx for element in self._elements)
        return sum_of_element_values

    def get_element_information(self):
        information: List = []
        for element in self._elements:
            information.append({"name": element.get_name(), "amount": element.get_value()})
        return information
