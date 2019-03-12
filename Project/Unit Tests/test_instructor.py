from unittest import TestCase
from Project.Classes.TA import TA
from Project.Classes.Account import Account
from Project.Classes.Instructor import Instructor
from Project.Classes.Course import Course
from Project.Classes.Lab import Lab


class TestInstructor(TestCase):
    def setUp(self):
        self.a1 = Account("Rick Flair", 69, "ricky@gmail.com", 5555555, "1600 Pennyslvania Ave")
        self.course1 = Course("math", 301, "Lubar Hall", "MWF", "4 AM - 11 AM", "Winter 2019", "Prof. Swag Daddy", ["foreign TA 1, foreign TA 2"], [401, 402, 403])
        self.lab1 = Lab(self.course1, self.course1.courseTA[0], self.course1.Lab[0], "1 AM - 1 PM")
        self.labArr = [self.lab1]
        self.t1 = TA(self.a1, self.labArr)
        self.in1 = Instructor(self.t1, [self.course1])


    def test__viewCourseAssignments__(self):
        """View your course assignments"""
        self.assertEqual(self.in1.viewCourseAssignments(), self.instruct1.courses)

    def test__assignTA__(self):
        self.assertEqual(self.in1.__assignTA__(self.lab1, self.t1), True)
        # valid param

        self.assertEqual(self.in1.__assignInstructor__(self.course1, self.t1), False)
        self.assertEqual(self.in1.__assignInstructor__(self.lab1), False)
        self.assertEqual(self.in1.__assignInstructor__(self.t1), False)
        self.assertEqual(self.in1.__assignInstructor__(), False)
        self.assertEqual(self.in1.__assignInstructor__("Hello World"), False)
        # invalid parameters

        self.in1.__assignTA__(self.lab1, self.t1)
        self.assertTrue(self.lab1.TAs.__contains__(self.t3.userName))
        # checks if TA was assigned

    def test__msgTAs__(self):
        """Message TAs in your courses"""
        self.assertEqual(self.in1.msgTAs("yo"), True)

