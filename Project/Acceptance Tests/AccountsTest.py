import unittest

class AccountsTest(unittest.TestCase):
    def setup(self):
        """
        create account
        self.fsa.command("create_account AccountID FirstName LastName Email PhoneNumber Address")
        currently allowing same user to have different roles
        """
        self.fsa.command("create_account Supervisor Jane Doe doe@uwm.edu 1(234)567-8901 321_Example_Street_Milwuakee_WI_12345")
        self.fsa.command("create_account Administrator Jane Doe doe@uwm.edu 1(234)567-8901 321_Example_Street_Milwuakee_WI_12345")
        self.fsa.command("create_account Instructor Jane Doe doe@uwm.edu 1(234)567-8901 321_Example_Street_Milwuakee_WI_12345")
        self.fsa.command("create_account TA Jane Doe doe@uwm.edu 1(234)567-8901 321_Example_Street_Milwuakee_WI_12345")

        """
            self.fsa.command("create_account AccountID FirstName MI LastName Email PhoneNumber Address")
        
            When the create account command is entered, and the user has a valid ID, it takes 7 arguments:
            - Account ID
            - First Name
            - Middle Name (optional)
            - Last Name
            - Email address (not limited to @uwm.edu)
            - Phone Number (style : #(###)###-####)
            - Address
        
            A database entry should be created for the account, if account creation is a success:
            - "Account created successfully."
            If input parameters are invalid or entry creation fails, failure:
            - "Error: Invalid parameters or database error"
            If user trying to create an account does not have access to do so, failure:
            - "Error: Access Denied"
        """

    """
         Supervisor should be able to create accounts,
         Success: Accounts created successfully
         Failure: Accounts not created successfully
     """
    def test_account_creation_supervisor_correct(self):
        self.fsa.command("login Supervisor supervisorPassword")
        self.assertEqual(self.fsa.command(
            "create_account Supervisor John Doe jdoe@uwm.edu 1(234)567-8900 123_Example_Street_Milwuakee_WI_12345"),
            "Account created successfully")
        self.assertEqual(self.fsa.command(
            "create_account Administrator Jane Doe doe@uwm.edu 1(234)567-8901 321_Example_Street_Milwuakee_WI_12345"),
            "Account created successfully")
        self.assertEqual(self.fsa.command(
            "create_account Administrator John Doe jdoe@uwm.edu 1(234)567-8900 123_Example_Street_Milwuakee_WI_12345"),
            "Account created successfully")
        self.assertEqual(self.fsa.command(
            "create_account Instructor Jane Doe doe@uwm.edu 1(234)567-8901 321_Example_Street_Milwuakee_WI_12345"),
            "Account created successfully")
        self.assertEqual(self.fsa.command(
            "create_account Instructor John Doe jdoe@uwm.edu 1(234)567-8900 123_Example_Street_Milwuakee_WI_12345"),
            "Account created successfully")
        self.assertEqual(self.fsa.command(
            "create_account TA Jane Doe doe@uwm.edu 1(234)567-8901 321_Example_Street_Milwuakee_WI_12345"),
            "Account created successfully")
        self.assertEqual(self.fsa.command(
            "create_account TA John Doe jdoe@uwm.edu 1(234)567-8901 123_Example_Street_Milwuakee_WI_12345"),
            "Account created successfully")

    """
         Administrator should be able to create accounts,
         Success: Account created successfully
         Failure: Account not created successfully
     """
    def test_account_creation_administrator_correct(self):
        self.fsa.command("login Administrator administratorPassword")
        self.assertEqual(self.fsa.command(
            "create_account Supervisor Jane Doe doe@uwm.edu 1(234)567-8901 321_Example_Street_Milwuakee_WI_12345"),
                "Account not created successfully")
        self.assertEqual(self.fsa.command(
            "create_account Supervisor John Doe jdoe@uwm.edu 1(234)567-8900 123_Example_Street_Milwuakee_WI_12345"),
            "Account not created successfully")
        self.assertEqual(self.fsa.command(
            "create_account Administrator Jane Doe doe@uwm.edu 1(234)567-8901 321_Example_Street_Milwuakee_WI_12345"),
            "Account not created successfully") ##why not? bc it already exists?
        self.assertEqual(self.fsa.command(
            "create_account Administrator John Doe jdoe@uwm.edu 1(234)567-8900 123_Example_Street_Milwuakee_WI_12345"),
            "Account created successfully")
        self.assertEqual(
            "create_account Instructor Jane Doe doe@uwm.edu 1(234)567-8901 321_Example_Street_Milwuakee_WI_12345",
                "Account created successfully")
        self.assertEqual(self.fsa.command(
            "create_account Instructor John Doe jdoe@uwm.edu 1(234)567-8900 123_Example_Street_Milwuakee_WI_12345"),
            "Account created successfully")
        self.assertEqual(self.fsa.command(
            "create_account TA Jane Doe doe@uwm.edu 1(234)567-8901 321_Example_Street_Milwuakee_WI_12345"),
                "Account created successfully")
        self.assertEqual(self.fsa.command(
            "create_account TA John Doe jdoe@uwm.edu 1(234)567-8900 123_Example_Street_Milwuakee_WI_12345"),
            "Account created successfully")

    """
        Instructors and TAs should not be able to create accounts, all such attempts should fail
        Failure: Account not created successfully
    """
    def test_account_creation_without_permissions(self):
        #without login should fail
        self.assertEqual(self.fsa.command(
            "create_account Supervisor Jane Doe doe@uwm.edu 1(234)567-8901 321_Example_Street_Milwuakee_WI_12345"),
            "Account not created successfully")
        self.assertEqual(self.fsa.command(
            "create_account Administrator Jane Doe doe@uwm.edu 1(234)567-8901 321_Example_Street_Milwuakee_WI_12345"),
            "Account not created successfully")
        self.assertEqual(self.fsa.command(
            "create_account Instructor Jane Doe doe@uwm.edu 1(234)567-8901 321_Example_Street_Milwuakee_WI_12345"),
            "Account not created successfully")
        self.assertEqual(self.fsa.command(
            "create_account TA Jane Doe doe@uwm.edu 1(234)567-8901 321_Example_Street_Milwuakee_WI_12345"),
            "Account not created successfully")

        #login as Instructor should not provide access
        self.fsa.command("login Instructor instructorPassword")
        self.assertEqual(self.fsa.command(
            "create_account Supervisor Jane Doe doe@uwm.edu 1(234)567-8901 321_Example_Street_Milwuakee_WI_12345"),
            "Account not created successfully")
        self.assertEqual(self.fsa.command(
            "create_account Administrator Jane Doe doe@uwm.edu 1(234)567-8901 321_Example_Street_Milwuakee_WI_12345"),
            "Account not created successfully")
        self.assertEqual(self.fsa.command(
            "create_account Instructor Jane Doe doe@uwm.edu 1(234)567-8901 321_Example_Street_Milwuakee_WI_12345"),
            "Account not created successfully")
        self.assertEqual(self.fsa.command(
            "create_account TA Jane Doe doe@uwm.edu 1(234)567-8901 321_Example_Street_Milwuakee_WI_12345"),
            "Account not created successfully")
        self.fsa.command("logout")

        #login as TA should not provide access
        self.fsa.command("login TA taPassword")
        self.assertEqual(self.fsa.command(
            "create_account Supervisor Jane Doe doe@uwm.edu 1(234)567-8901 321_Example_Street_Milwuakee_WI_12345"),
            "Account not created successfully")
        self.assertEqual(self.fsa.command(
            "create_account Administrator Jane Doe doe@uwm.edu 1(234)567-8901 321_Example_Street_Milwuakee_WI_12345"),
            "Account not created successfully")
        self.assertEqual(self.fsa.command(
            "create_account Instructor Jane Doe doe@uwm.edu 1(234)567-8901 321_Example_Street_Milwuakee_WI_12345"),
            "Account not created successfully")
        self.assertEqual(self.fsa.command(
            "create_account TA Jane Doe doe@uwm.edu 1(234)567-8901 321_Example_Street_Milwuakee_WI_12345"),
            "Account not created successfully")