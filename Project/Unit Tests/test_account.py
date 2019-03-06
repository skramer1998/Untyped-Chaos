from unittest import TestCase
from Project.Classes.Account import Account

class TestAccount(TestCase):
    def setUp(self):
        self.a1 = Account("Rick Flair", 69, "ricky@gmail.com", 5555555, "1600 Pennyslvania Ave")

    def test_editSelf(self):
        self.a1.editSelf("Migos", 22, "durp@yahoo.com", 1234567, "15 Drury Lane")
        self.assertEqual(self.a1.userName, "Migos", "User name did not change.")
        self.assertFalse(self.a1.editSelf("Rick Flair", 69, "ricky@gmail.com", 5, "1600 Pennyslvania Ave"),
                         "Phone Number too short.")
        self.assertFalse(self.a1.editSelf("Rick Flair"), "Not enough parameters.")
        self.assertFalse(self.a1.editSelf("Rick Flair", 69, "lip", 5555555, "1600 Pennyslvania Ave"),
                         "Not a valid email.")
        self.assertFalse(self.a1.editSelf(1, 69, 3, 5, "1600 Pennyslvania Ave"),
                         "Invalid Parameters.")

    def test_publicInfo(self):
        self.assertTrue()
