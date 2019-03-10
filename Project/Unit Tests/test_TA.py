from unittest import TestCase
from Project.Classes.TA import TA
from Project.Classes.Account import Account
from Project.Classes.Course import Course
from Project.Classes.Lab import Lab

class TestTA(TestCase):

    def setUp(self):
        self.a1 = Account("Rick Flair", 69, "ricky@gmail.com", 5555555, "1600 Pennyslvania Ave")
        self.course1 = Course("math", "301", "Lubar Hall", "MWF", "4 AM - 11 AM", "Winter 2019", "Prof. Swag Daddy", ["foreign TA 1, foreign TA 2"], [401, 402, 403])
        self.labArr = [Lab(self.course1, self.course1.courseTA[0], self.course1.Lab[0], "1 AM - 1 PM")]

    def test__TA__(self):
        self.assertEqual(self.t1 = TA(), False)
        # empty constructor should return false

        self.assertEqual(self.t2 = TA(self.a1, self.labArr), True)
        # proper constructor returns true

    """
    Need to test assignments for courses and lab sections
    """
    def test__viewTAAssignments__(self):
        self.t2 = TA(self.a1, self.labArr)
        self.assertEqual(self.t2.__viewTAAssignments__(), self.labArr)
        #format for returning the TA's assignments

