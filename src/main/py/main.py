from typing import List

from Categories.Category import Category
from Categories.Element import Element
from Categories.FinancialTypes import FinancialType


class Main:
    def __init__(self):
        self._categories: List[Category] = []

    def start(self):
        income = Category()
        income.add_element(Element(1000, FinancialType.INCOME))
        living = Category()
        living.add_element(Element(350, FinancialType.COST))
        loans = Category()
        loans.add_element(Element(200, FinancialType.COST))
        savings = Category()
        savings.add_element(Element(150, FinancialType.SAVING))

        self._categories.append(income)
        self._categories.append(living)
        self._categories.append(loans)
        self._categories.append(savings)

        remaining_money = sum(category.get_sum() for category in self._categories)
        print("Remaining Money: " + str(remaining_money))


main = Main()
main.start()