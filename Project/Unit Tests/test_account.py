from unittest import TestCase
from Project.Classes.Account import Account

class TestAccount(TestCase):
    def setUp(self):
        self.a1 = Account("Rick Flair", 69, "ricky@gmail.com", 5555555, "1600 Pennyslvania Ave")

    def test_editSelf(self):
        self.assertEqual(self.a1.userName, "Rick Flair", "User name not set correctly.")
        self.assertEqual(self.a1.userID, 69, "User ID not set correctly.")
        self.assertEqual(self.a1.userEmail, "ricky@gmail.com", "User Email not set correctly.")
        self.assertEqual(self.a1.userPhone, 5555555, "User's Phone Number not set correctly.")
        self.assertEqual(self.a1.userAddress, "1600 Pennyslvania Ave", "User Address not set correctly.")
        # tests that all parameters are set properly in __Init__

        self.a1.editSelf("Migos", 22, "durp@yahoo.com", 1234567, "15 Drury Lane")
        self.assertEqual(self.a1.userName, "Migos", "User name did not change.")
        self.assertEqual(self.a1.userID, 22, "User ID did not change.")
        self.assertEqual(self.a1.userEmail, "durp@yahoo.com", "User Email did not change.")
        self.assertEqual(self.a1.userPhone, 1234567, "User's Phone Number did not change.")
        self.assertEqual(self.a1.userAddress, "15 Drury Lane", "User Address did not change.")
        # tests that all parameters changed properly

        self.assertFalse(self.a1.editSelf("Rick Flair", 69, "ricky@gmail.com", 5, "1600 Pennyslvania Ave"),
                         "Phone Number too short.")
        self.assertFalse(self.a1.editSelf("Rick Flair"), "Not enough parameters.")
        self.assertFalse(self.a1.editSelf("Rick Flair", 69, "lip", 5555555, "1600 Pennyslvania Ave"),
                         "Not a valid email.")
        self.assertFalse(self.a1.editSelf(1, 69, 3, 5, "1600 Pennyslvania Ave"),
                         "Invalid Parameters.")
        # tests the outcome of putting bogus parameters into the method

    def test_publicInfo(self):
        self.assertTrue()
