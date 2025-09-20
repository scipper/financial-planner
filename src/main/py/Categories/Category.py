from typing import List

from Categories.Element import Element
from Categories.FinancialTypes import FinancialType


class Category:
    """A category container 0 or more elements of financial types."""

    def __init__(self):
        self._income_elements: List[Element] = []
        self._saving_elements: List[Element] = []
        self._cost_elements: List[Element] = []

    def add_element(self, element: Element):
        if element.get_type() == FinancialType.INCOME:
            self._income_elements.append(element)
        elif element.get_type() == FinancialType.SAVING:
            self._saving_elements.append(element)
        else:
            self._cost_elements.append(element)

    def get_sum(self) -> float:
        sum_income = sum(element.get_value() for element in self._income_elements)
        sum_savings = sum(element.get_value() for element in self._saving_elements)
        sum_costs = sum(element.get_value() for element in self._cost_elements)
        return sum_income + sum_savings + sum_costs

    def get_element_information(self):
        information: List = []
        for element in self._income_elements:
            information.append({"name": element.get_name(), "amount": element.get_value(), "type": element.get_type()})
        for element in self._cost_elements:
            information.append({"name": element.get_name(), "amount": element.get_value(), "type": element.get_type()})
        for element in self._saving_elements:
            information.append({"name": element.get_name(), "amount": element.get_value(), "type": element.get_type()})
        return information
