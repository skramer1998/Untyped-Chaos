from django.test import TestCase
from untitled1.AppName.models import LoginModel

# remember, fsa stands for functional school app


class LoginTests(TestCase):
    def setup(self):

        LoginModel.object.create(userName = "Instructor", password = "InstructorPassword")
        LoginModel.object.create(userName = "TA", password = "TAPassword")
        #^^ Need model for this

        #self.fsa.command("create_user Instructor InstructorPassword")
        #self.fsa.command("create_user TA TAPassword")

    """
        When the login command is entered, it takes two arguments:
        - Username
        - Password
        If the username and password match a database entry, login is a success:
        - "Logged in successfully."
        If they do not match or are omitted, failure:
        - "Error logging in."
    """
    def test_command_login_correct(self):
        self.assertEqual(self.fsa.command("login Instructor InstructorPassword"), "Logged in successfully.")

    def test_command_login_bad_pass(self):
        self.assertEqual(self.fsa.command("login Instructor Notinstructorpassword"), "Error logging in.")

    def test_command_login_bad_case_pass(self):
        self.assertEqual(self.fsa.command("login Instructor instructorpassword"), "Error logging in.")

    def test_command_login_wrong_user_pass(self):
        self.assertEqual(self.fsa.command("login Instructor TAPassword"), "Error logging in.")

    def test_command_login_no_pass(self):
        self.assertEqual(self.fsa.command("login Instructor"), "Error logging in.")

    def test_command_login_no_args(self):
        self.assertEqual(self.fsa.command("login"), "Error logging in.")

    def test_command_login_self_already_logged_in(self):
        self.ui.command("login Instructor InstructorPassword")
        self.assertEqual(self.fsa.command("login Instructor InstructorPassword"), "Error logging in.")

    def test_command_login_other_already_logged_in(self):
        self.ui.command("login Instructor Instructor Password")
        self.assertEqual(self.fsa.command("login TA TAPassword"), "Error logging in.")

    """ 
        When logout command is entered, it takes no arguments.
        It logs a user out only if there is one logged in.
        - Success: "Logged out successfully."
        - Failure: "Error logging out."
    """
    def test_command_logout_correct(self):
        self.ui.command("login Instructor InstructorPassword")
        self.assertEqual(self.fsa.command("logout"), "Logged out successfully.")

    def test_command_logout_allows_relogin(self):
        self.ui.command("login Instructor InstructorPassword")
        self.assertEqual(self.fsa.command("logout"), "Logged out successfully")
        self.assertEqual(self.fsa.command("login Instructor InstructorPassword"), "Logged in successfully")

    def test_command_logout_not_logged_in(self):
        self.assertEqual(self.fsa.command("logout"), "Error logging out.")