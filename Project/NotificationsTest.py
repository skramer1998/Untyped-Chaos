import unittest

class NotificationsTest(unittest.TestCase):
    def setup(self):
        """
        self.fsa.command("new_notification toWhom subject")

        When the new notification command is used, it takes 2 arguments:
        -toWhom
        -subject

        An error will occur if the toWhom field is not a valid UWM email address, or one of the following:
        -all_users
        -all_tas
        -all_instructors
        -all_admins

        The use of these is restricted on an account-type basis.

        The subject field may be left blank.
        """

        self.fsa.command("new_notification jrock@uwm.edu Help")
        self.fsa.command("new_notification all_users Important")
        self.fsa.command("new_notification all_instructors test")