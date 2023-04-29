import unittest

from models.account import Account

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account("Penny", "Personal", 500)

    def test_account_has_user_id(self):
        self.assertEqual("Penny", self.account.user_id)

    def test_account_has_type(self):
        self.assertEqual("Personal", self.account.type)

    def test_account_has_balance(self):
        self.assertEqual(500, self.account.balance)

    def test_increase_balance(self):
        self.account.increase_balance(100)
        self.assertEqual(600, self.account.balance)

    def test_decrease_balance(self):
        self.account.decrease_balance(100)
        self.assertEqual(400, self.account.balance)
