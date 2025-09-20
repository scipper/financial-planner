from typing import List

from Categories.Category import Category
from Categories.Element import Element
from Categories.FinancialTypes import FinancialType


class Main:
    def __init__(self):
        self._categories: List[Category] = []

    def start(self):
        incomes = Category()
        incomes.add_element(Element("Salary", 1000, FinancialType.INCOME))
        livings = Category()
        livings.add_element(Element("Rent", 350, FinancialType.COST))
        loans = Category()
        loans.add_element(Element("Car", 200, FinancialType.COST))
        savings = Category()
        savings.add_element(Element("Vacation", 150, FinancialType.SAVING))

        self._categories.append(incomes)
        self._categories.append(livings)
        self._categories.append(loans)
        self._categories.append(savings)

        for category in self._categories:
            print(category.get_element_information())

        remaining_money = sum(category.get_sum() for category in self._categories)
        print("Remaining Money: " + str(remaining_money))


main = Main()
main.start()