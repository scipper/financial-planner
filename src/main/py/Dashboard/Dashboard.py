from typing import List

from Categories.Category import Category
from Categories.Element import Element


class Dashboard:
    def __init__(self):
        self._categories: List[Category] = []

    def add_category(self, category: Category):
        self._categories.append(category)

    def add_element_to_category(self, index: int, element: Element):
        self._categories[index].add_element(element)

    def get_sum_of_categories(self):
        return sum(category.get_sum() for category in self._categories)
