from typing import List

from Categories.Category import Category
from Categories.Element import Element
from Categories.FinancialTypes import FinancialType
from Dashboard.Dashboard import Dashboard


class Main:
    def __init__(self):
        self._dashboard = Dashboard()
        self._categories: List[Category] = []

    def start(self):
        incomes = Category()
        incomes.set_type(FinancialType.INCOME)
        self._dashboard.add_category(incomes)
        self._dashboard.add_element_to_category(0, Element("Salary", 1000))
        livings = Category()
        livings.set_type(FinancialType.COST)
        self._dashboard.add_category(livings)
        self._dashboard.add_element_to_category(1, Element("Rent", 350))
        loans = Category()
        loans.set_type(FinancialType.COST)
        self._dashboard.add_category(loans)
        self._dashboard.add_element_to_category(2, Element("Car", 200))
        savings = Category()
        savings.set_type(FinancialType.SAVING)
        self._dashboard.add_category(savings)
        self._dashboard.add_element_to_category(3, Element("Vacation", 150))

        for category in self._categories:
            print(category.get_element_information())

        remaining_money = sum(category.get_sum() for category in self._categories)
        print("Remaining Money: " + str(remaining_money))


main = Main()
main.start()