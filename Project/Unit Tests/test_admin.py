from unittest import TestCase
from Project.Classes.Admin import Admin
from Project.Classes.Account import Account

class TestAdmin(TestCase):

    def setUp(self):
        self.a1 = Account("Jo", 34, "x@gmail.com", 1234567, "White House")
        self.firstAdmin = Admin(self.a1)

    def test_createCourse(self):
        self.assertEqual(self.firstAdmin.__createCourse__("courseName"), True)
        # returns true if course is successfully created
        # will ask for more parameters after method is called and course is named

    def test_createAccount(self):
        self.assertEqual(self.firstAdmin.__createAccount__("name", id, "email@email.email", 1234567, "Under the bridge"), True)
        # attempts to create an account, if successful return true

    def test_modifyAccount(self):
        self.assertEqual(self.firstAdmin.__modifyAccounts__(self.a1, "Tom", 21, "newEmail@gmail.com", 1234560, "address"), True)
        self.assertEqual(self.a1.userName, "Tom", "User name not set correctly.")
        self.assertEqual(self.a1.userID, 21, "User ID not set correctly.")
        self.assertEqual(self.a1.userEmail, "newEmail@gmail.com", "User Email not set correctly.")
        self.assertEqual(self.a1.userPhone, 1234560, "User's Phone Number not set correctly.")
        self.assertEqual(self.a1.userAddress, "address", "User Address not set correctly.")
        # modifys the account a1 and checks the updated info

    def test_sendAllNoti(self):
        self.assertTrue(self.firstAdmin.__sendAllNoti__("Greetings my inferiors."))
        # sends message, if successful method returns true

    def test_seePrivateInfo(self):
        self.assertTrue(self.firstAdmin.__seePrivateInfo__(self.a1))
        # checks the private info of account a1
