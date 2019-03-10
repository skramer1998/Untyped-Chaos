from unittest import TestCase
from Project.Classes.Admin import Admin
from Project.Classes.Account import Account

class TestAdmin(TestCase):

    def setUp(self):
        self.firstAdmin = Admin()
        self.a1 = Account("Jo", 34, "x@gmail.com", 1234567, "White House")

    def test_createCourse(self):
        self.assertEqual(self.firstAdmin.__createCourse__("courseName"), True)
        # returns true if course is successfully created
        # will ask for more parameters after method is called and course is named


    def test_createAccount(self):
        self.assertEqual(self.firstAdmin.__createAccount__("name", id, "email@email.email", 1234567, "Under the bridge"), True)
        # attempts to create an account, if successful return true

    def test_modifyAccount(self):
        self.assertEqual(self.firstAdmin.__modifyAccounts__(a1, "newName", newID, "newEmail@gmail.com", 1234567, "adress"), True)
        self.assertEqual(self.a1.userName, "Jo", "User name not set correctly.")
        self.assertEqual(self.a1.userID, 34, "User ID not set correctly.")
        self.assertEqual(self.a1.userEmail, "x@gmail.com", "User Email not set correctly.")
        self.assertEqual(self.a1.userPhone, 1234567, "User's Phone Number not set correctly.")
        self.assertEqual(self.a1.userAddress, "White House", "User Address not set correctly.")
        # modifys the account a1 and checks the updated info

    def test_sendAllNoti(self):
        self.assertEqual(self.firstAdmin.__sendAllNoti__("Greetings my inferiors."), True)
        # sends message, if successful method returns true

    def test_seePrivateInfo(self):
        self.assertEqual(self.firstAdmin.__seePrivateInfo__(a1), True)
        # checks the private info of account a1
