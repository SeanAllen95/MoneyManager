import unittest

from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("Bob")

    def test_user_has_name(self):
        self.assertEqual("Bob", self.user.name)
        
