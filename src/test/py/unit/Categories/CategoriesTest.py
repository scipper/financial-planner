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
        self.category.add_element(Element(1))
        self.assertEqual(self.category.get_sum(), 1)

    def test_element_of_type_cost_has_negative_sum(self):
        self.category.add_element(Element(1, FinancialType.COST))
        self.assertEqual(self.category.get_sum(), -1)

    def test_element_of_type_saving_has_negative_sum(self):
        self.category.add_element(Element(1, FinancialType.SAVING))
        self.assertEqual(self.category.get_sum(), -1)

    def test_build_correct_sum_for_mixed_element_types(self):
        self.category.add_element(Element(10, FinancialType.INCOME))
        self.category.add_element(Element(3, FinancialType.SAVING))
        self.category.add_element(Element(4, FinancialType.COST))
        self.assertEqual(self.category.get_sum(), 3)

    def test_throws_on_unknown_financial_type(self):
        with pytest.raises(UnknownFinancialTypeError, match=r"Unknown financial type 'WRONG'"):
            self.category.add_element(Element(1, "WRONG"))
