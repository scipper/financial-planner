from typing import List

from Categories.Element import Element


class Category:
    def __init__(self):
        self.income_elements: List[Element] = []
        self.saving_elements: List[Element] = []
        self.cost_elements: List[Element] = []

    def get_sum(self) -> float:
        sum_income = sum(element.get_value() for element in self.income_elements)
        sum_savings = sum(element.get_value() for element in self.saving_elements)
        sum_costs = sum(element.get_value() for element in self.cost_elements)
        return sum_income + sum_savings + sum_costs

    def add_element(self, element: Element):
        if element.get_type() == "income":
            self.income_elements.append(element)
        elif element.get_type() == "saving":
            self.saving_elements.append(element)
        else :
            self.cost_elements.append(element)
