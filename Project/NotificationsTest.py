import unittest

class NotificationsTest(unittest.TestCase):
    def setup(self):
        """
        self.fsa.command("new_notification toWhom subject")
        """

        self.fsa.command("new_notification jrock@uwm.edu Help")
        self.fsa.command("new_notification all_users Important")
        self.fsa.command("new_notification all_instructors test")