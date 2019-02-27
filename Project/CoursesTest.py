import unittest

class CoursesTest(unittest.TestCase):
    def setup(self):
        self.fsa.command("create_course Instructor InstructorPassword")