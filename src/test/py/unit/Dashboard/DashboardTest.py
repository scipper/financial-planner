import unittest

from Categories.Category import Category
from Categories.Element import Element
from Categories.FinancialTypes import FinancialType
from Dashboard.Dashboard import Dashboard


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.dashboard = Dashboard()

    def test_shows_sum_of_one_category(self):
        category = Category()
        self.dashboard.add_category(category)
        self.dashboard.add_element_to_category(0, Element("name", 1))
        self.assertEqual(self.dashboard.get_sum_of_categories(), 1)

    def test_shows_sum_of_multiple_categories(self):
        salary = Category()
        loads = Category()
        loads.set_type(FinancialType.COST)
        savings = Category()
        savings.set_type(FinancialType.SAVING)
        self.dashboard.add_category(salary)
        self.dashboard.add_category(loads)
        self.dashboard.add_category(savings)
        self.dashboard.add_element_to_category(0, Element("Salary", 1000))
        self.dashboard.add_element_to_category(1, Element("Car", 200))
        self.dashboard.add_element_to_category(2, Element("Vacation", 150))
        self.assertEqual(self.dashboard.get_sum_of_categories(), 650)
