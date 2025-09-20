import unittest

from Categories.Category import Category
from Categories.Element import Element


class CategoriesTest(unittest.TestCase):
    def setUp(self):
        self.category = Category()

    def test_empty_category_has_sum_of_0(self):
        self.assertEqual(self.category.get_sum(), 0)

    def test_category_with_one_element_has_sum_of_element_value(self):
        self.category.add_element(Element(1))
        self.assertEqual(self.category.get_sum(), 1)

    def test_element_of_type_cost_has_negative_sum(self):
        self.category.add_element(Element(1, "cost"))
        self.assertEqual(self.category.get_sum(), -1)
