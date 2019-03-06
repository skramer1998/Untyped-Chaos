from unittest import TestCase
from Project.Classes.Admin import Admin

class TestAdmin(TestCase):

    def setUp(self):
        self.firstAdmin = Admin()

    def test_createCourse(self):
        self.assertEqual(self.firstAdmin.__createCourse__("courseName"), True)

    def test_createAccount(self):
        self.assertEqual(self.firstAdmin.__createAcount__("accountName"), True)

    def test_modifyAccount(self):
        self.assertEqual(self.firstAdmin.__modifyAccounts__("accountName"), True)

    def test_sendAllNoti(self):
        self.assertEqual(self.firstAdmin.__sendAllNoti__("all"), True)

    def test_seePrivateInfo(self):
        self.assertEqual(self.firstAdmin.__seePrivateInfo__("all"), True)