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

    def test_supervisor_privilege(self):
        self.fsa.command("login Supervisor supervisorPassword")
        self.assertEqual(self.fsa.command("new_notification all_users Important"), "New notification started")
        self.assertEqual(self.fsa.command("new_notification all_tas test"), "New notification started")
        self.assertEqual(self.fsa.command("new_notification all_instructors Hey"), "New notification started")
        self.assertEqual(self.fsa.command("new_notification all_admins Listen!"), "New notification started")
        self.assertEqual(self.fsa.command("new_notification jrock@uwm.edu HELP"), "New notification started")
        self.assertRaises(self.fsa.command("new_notification jrock@gmail.com HELP")) #should error, not UWM email
        self.assertRaises(self.fsa.command("new_notification all-admins HELP")) #should error, bad tag
        """
        The Supervisor should be able to send notifications to all emails and all groupings of emails.
        """

    def test_administrator_privelege(self):
        self.fsa.command("login Administrator adminPassword")
        self.assertEqual(self.fsa.command("new_notification all_users Important"), "New notification started")
        self.assertEqual(self.fsa.command("new_notification all_tas test"), "New notification started")
        self.assertEqual(self.fsa.command("new_notification all_instructors Hey"), "New notification started")
        self.assertEqual(self.fsa.command("new_notification all_admins Listen!"), "New notification started")
        self.assertEqual(self.fsa.command("new_notification jrock@uwm.edu HELP"), "New notification started")
        self.assertRaises(self.fsa.command("new_notification jrock@gmail.com HELP"))  # should error, not UWM email
        self.assertRaises(self.fsa.command("new_notification all-admins HELP"))  # should error, bad tag
        """
        The Administrator should be able to send notifications to all emails and all groupings of emails.
        """


    def test_instructor_privilege(self):
        self.fsa.command("login Instructor instructorPassword")
        self.assertEqual(self.fsa.command("new_notification all_users Important"), "Unauthorized to notify this group")
        self.assertEqual(self.fsa.command("new_notification all_tas test"), "New notification started")
        self.assertEqual(self.fsa.command("new_notification all_instructors Hey"), "Unauthorized to notify this group")
        self.assertEqual(self.fsa.command("new_notification all_admins Listen!"), "Unauthorized to notify this group")
        self.assertEqual(self.fsa.command("new_notification jrock@uwm.edu HELP"), "New notification started")
        self.assertRaises(self.fsa.command("new_notification jrock@gmail.com HELP"))  # should error, not UWM email
        self.assertRaises(self.fsa.command("new_notification all-admins HELP"))  # should error, bad tag
        """
        The Instructor should be able to send notifications to all emails but only the TAs list.
        """

    def test_TA_lackOfPrivilege(self):
        self.fsa.command("login TeacherAid taPassword")
        self.assertEqual(self.fsa.command("new_notification all_users Important"), "Unauthorized to notify this group")
        self.assertEqual(self.fsa.command("new_notification all_tas test"), "Unauthorized to notify this group")
        self.assertEqual(self.fsa.command("new_notification all_instructors Hey"), "Unauthorized to notify this group")
        self.assertEqual(self.fsa.command("new_notification all_admins Listen!"), "Unauthorized to notify this group")
        self.assertEqual(self.fsa.command("new_notification jrock@uwm.edu HELP"), "New notification started")
        self.assertRaises(self.fsa.command("new_notification jrock@gmail.com HELP"))  # should error, not UWM email
        self.assertRaises(self.fsa.command("new_notification all-admins HELP"))  # should error, bad tag
        """
        The TA should only be able to send notifications to email addresses.
        """