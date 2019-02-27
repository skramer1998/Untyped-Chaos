import unittest

class CoursesTest(unittest.TestCase):
    def setup(self):
        """
        self.fsa.command("create_course course_name course_number course_place course_days course_time course_semester course_professor course_tas course_labs")
        """

        self.fsa.command("create_course course_name course_number course_place course_days course_time course_semester course_professor course_tas course_labs")