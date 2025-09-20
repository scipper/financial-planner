import unittest

import pytest

from Categories.Category import Category
from Categories.Element import Element
from Categories.FinancialTypes import FinancialType
from Categories.UnknownFinancialTypeError import UnknownFinancialTypeError


class CategoriesTest(unittest.TestCase):
    def setUp(self):
        self.category = Category()

    def test_empty_category_has_sum_of_0(self):
        self.assertEqual(self.category.get_sum(), 0)

    def test_category_with_one_element_has_sum_of_element_value(self):
        self.category.add_element(Element("", 1))
        self.assertEqual(self.category.get_sum(), 1)

    def test_category_of_type_cost_has_negative_sum(self):
        self.category.set_type(FinancialType.COST)
        self.category.add_element(Element("", 1))
        self.assertEqual(self.category.get_sum(), -1)

    def test_element_of_type_saving_has_negative_sum(self):
        self.category.set_type(FinancialType.SAVING)
        self.category.add_element(Element("", 1))
        self.assertEqual(self.category.get_sum(), -1)

    def test_build_correct_sum_for_multiple_element_types(self):
        self.category.add_element(Element("", 10))
        self.category.add_element(Element("", 3))
        self.category.add_element(Element("", 4))
        self.assertEqual(self.category.get_sum(), 17)

    def test_throws_on_unknown_financial_type(self):
        with pytest.raises(UnknownFinancialTypeError, match=r"Unknown financial type 'WRONG'"):
            self.category.set_type("WRONG")

    def test_returns_all_information_of_element(self):
        self.category.add_element(Element("Salary", 1))
        expected = [{"name": "Salary", "amount": 1}]
        self.assertEqual(self.category.get_element_information(), expected)

    def test_returns_all_information_for_multiple_elements(self):
        self.category.add_element(Element("Salary", 10))
        self.category.add_element(Element("Saving", 1))
        expected = [
            {"name": "Salary", "amount": 10},
            {"name": "Saving", "amount": 1}
        ]
        self.assertEqual(self.category.get_element_information(), expected)
