from unittest import TestCase
from Project.Classes.Lab import Lab
from Project.Classes.TA import TA
from Project.Classes.Course import Course
from Project.Classes.Account import Account
from Project.Classes.Instructor import Instructor
from Project.Classes.Admin import Admin
from Project.Classes.Supervisor import Supervisor

class TestSupervisor(TestCase):

    def setUp(self):
        self.a1 = Account("Jo", 34, "x@gmail.com", 1234567, "White House")
        self.ad1 = Admin(self.a1)
        self.s1 = Supervisor(self.ad1)
        self.s2 = Supervisor()

        self.a2 = Account("Mandy", 18, "m@gmail.com", 0101010, "IHOP")
        self.in2 = Instructor(self.a2, [])

        self.a3 = Account("Tom", 21, "y@gmail.com", 1010101, "Dennys")
        self.t3 = TA(self.a3, [])

        self.course1 = Course("math", 301, "Lubar Hall", "MWF", "4 AM - 11 AM", "Winter 2019", "Prof. Swag Daddy",
                              ["foreign TA 1, foreign TA 2"], [401, 402, 403])
        self.lab1 = Lab(self.course1, self.course1.courseTA[0], self.course1.Lab[0], "1 AM - 1 PM")

    def test__assignInstructor__(self, course, user):
        self.assertEqual(self.s1.__assignInstructor__(self.course1, self.in2), True)
        # valid parameters

        self.assertEqual(self.s1.__assignInstructor__(self.lab1, self.in2), False)
        self.assertEqual(self.s1.__assignInstructor__(self.course1, self.t3), False)
        self.assertEqual(self.s1.__assignInstructor__(self.course1), False)
        self.assertEqual(self.s1.__assignInstructor__(self.in2), False)
        self.assertEqual(self.s1.__assignInstructor__(), False)
        self.assertEqual(self.s1.__assignInstructor__("Hello World"), False)
        # invalid parameters

        self.s1.__assignInstructor__(self.course1, self.in2)
        self.assertEqual(self.course1.courseProf, self.in2.userName)
        # checks if instructor was assigned

    def test__assignTA__(self):
        self.assertEqual(self.s1.__assignTA__(self.lab1, self.t3), True)
        # valid param

        self.assertEqual(self.s1.__assignInstructor__(self.course1, self.t3), False)
        self.assertEqual(self.s1.__assignInstructor__(self.lab1, self.in2), False)
        self.assertEqual(self.s1.__assignInstructor__(self.lab1), False)
        self.assertEqual(self.s1.__assignInstructor__(self.t3), False)
        self.assertEqual(self.s1.__assignInstructor__(), False)
        self.assertEqual(self.s1.__assignInstructor__("Hello World"), False)
        # invalid parameters

        self.s1.__assignTA__(self.lab1, self.t3)
        self.assertTrue(self.lab1.TAs.__contains__(self.t3.userName))
        # checks if TA was assigned

    def test__editCourse__(self):
        self.assertFalse(self.s1.__editCourse__(self.course1, "math"))
        self.assertFalse(self.s1.__editCourse__("math", 301, "Lubar Hall", "MWF", "4 AM - 11 AM", "Winter 2019", "Prof. Swag Daddy",
                              ["foreign TA 1, foreign TA 2"], [401, 402, 403]))
        self.assertFalse(self.s1.__editCourse__(self.course1, "math", 301, "Lubar Hall", "MWF", "4 AM - 11 AM", "Winter 2019",
                               "Prof. Swag Daddy", ["foreign TA 1, foreign TA 2"], [401, 402, 403], 12))
        # too few or too many params

        self.assertFalse(self.s1.__editCourse__(self.course1, "math", "301", "Lubar Hall", "MWF", "4 AM - 11 AM", "Winter 2019",
                                   "Prof. Swag Daddy", ["foreign TA 1, foreign TA 2"], [401, 402, 403]))
        self.assertFalse(self.s1.__editCourse__(self.course1, "math", 301, "Lubar Hall", "MWF", "4 AM - 11 AM", "Winter 2019",
                                   "Prof. Swag Daddy", ["foreign TA 1, foreign TA 2"], ["401", "402", "403"]))
        # invalid parameter type

        self.s1.__editCourse__(self.course1,"science", 400, "Physics Building", "TR", "1 AM - 1PM", "FALL 2019", "Prof. Strange",
                              ["foreign TA 3"], [800])
        self.assertEqual(self.course1.name, "science")
        self.assertEqual(self.course1.number, 400)
        self.assertEqual(self.course1.place, "Physics Building")
        self.assertEqual(self.course1.days, "TR")
        self.assertEqual(self.course1.time, "1 AM - 1PM")
        self.assertEqual(self.course1.semester, "FALL 2019")
        self.assertEqual(self.course1.courseProf, "Prof. Strange")
        self.assertEqual(self.course1.TAs, ["foreign TA 3"])
        self.assertEqual(self.course1.Labs, [800])
        # checks if course was successfully edited
