import unittest

from models.merchant import Merchant

class TestMerchant(unittest.TestCase):
    def setUp(self):
        self.merchant = Merchant("ASDA", "Food", 100)

    def test_merchant_has_name(self):
        self.assertEqual("ASDA", self.merchant.name)

    def test_merchant_has_category(self):
        self.assertEqual("Food", self.merchant.category)

    def test_merchant_has_amount(self):
        self.assertEqual(100, self.merchant.amount)

    def test_increase_amount(self):
        self.merchant.increase_amount(50)
        self.assertEqual(150, self.merchant.amount)

    def test_decrease_amount(self):
        self.merchant.decrease_amount(50)
        self.assertEqual(50, self.merchant.amount)
    