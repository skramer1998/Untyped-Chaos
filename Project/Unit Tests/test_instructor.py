from unittest import TestCase
from Project.Classes.TA import TA
from Project.Classes.Account import Account
from Project.Classes.Instructor import Instructor
from Project.Classes.Course import Course
from Project.Classes.Lab import Lab


class TestInstructor(TestCase):
    def setUp(self):
        self.a1 = Account("Rick Flair", 69, "ricky@gmail.com", 5555555, "1600 Pennyslvania Ave")
        self.course1 = Course("math", "301", "Lubar Hall", "MWF", "4 AM - 11 AM", "Winter 2019", "Prof. Swag Daddy", ["foreign TA 1, foreign TA 2"], [401, 402, 403])
        self.labArr = [Lab(self.course1, self.course1.courseTA[0], self.course1.Lab[0], "1 AM - 1 PM")]
        self.t1 = TA(self.a1, self.labArr)
        self.instruct1 = Instructor(self.t1, [self.course1])


    def test__viewCourseAssignments__(self):
        """View your course assignments"""
        self.assertEqual(self.instruct1.viewCourseAssignments(), self.instruct1.courses)

    def test__assignTAs__(self):
        """Assign TAs to lab sections"""
        # self.assertEqual(self.instruct1.assignTAs()

    def test__msgTAs__(self):
        """Message TAs in your courses"""
        self.assertEqual(self.instruct1.msgTAs("yo"), True)

