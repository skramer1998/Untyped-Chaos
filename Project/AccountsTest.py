import unittest

class AccountsTest(unittest.TestCase):
    def setup(self):
        """
        create account
        self.fsa.command("create_account AccountID FirstName LastName Email PhoneNumber Address")
        currently allowing same user to have different roles
        """
        self.fsa.command("create_account Supervisor Jane Doe doe@uwm.edu 1(234)567-8901 321_Example_Street_Milwukee_WI_12345")
        self.fsa.command("create_account Administrator Jane Doe doe@uwm.edu 1(234)567-8901 321_Example_Street_Milwukee_WI_12345")
        self.fsa.command("create_account Instructor Jane Doe doe@uwm.edu 1(234)567-8901 321_Example_Street_Milwukee_WI_12345")
        self.fsa.command("create_account TA Jane Doe doe@uwm.edu 1(234)567-8901 321_Example_Street_Milwukee_WI_12345")

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
        
        
        """