import unittest

class CoursesTest(unittest.TestCase):
    def setup(self):

        self.fsa.command("create_course softwareEngineering 361 lubarHall T-TR 10-10:50 SP19 rock apoorv 1")
        self.fsa.command("create_course algorithmDesign 535 EMS M-W 4-5:15 SP19 cheng")
        self.fsa.command("create_course security 469 EMS T-TR 10-10:50 SP19 bob")
        self.fsa.command("create_course operatingSystems 550 physics M-W-F 8-8:50 SP19 sorensen jimbo-allen 2")

        """
            self.fsa.command("create_course course_name course_number course_place course_days course_time course_semester course_professor course_tas course_labs")
        
            When the create course command is entered, and the user has a valid ID, it takes 11 arguments:
            - Course Name
            - Course Number
            - Course Meeting Place
            - Course Meeting Days
            - Course Meeting Times
            - Course Semester
            - Course Professor
            - Course TAs (optional)
            - Course Labs (optional)
            
            A database entry should be created for the curse, if course creation is a success:
            - "Course created successfully."
            If input parameters are invalid or entry creation fails, failure:
            - "Error: Invalid parameters or database error"
            If user trying to create a course does not have access to do so, failure:
            - "Error: Access Denied"
        """

    # Correct Course Creation Tests
    def test_course_creation_supervisor_correct(self):
        fsa.command(login Supervisor supervisorPassword)
        self.assertEqual(self.fsa.command("create_course testCourse 999 wonderLand M-T-W-TR-F 9-9 SP20 jackson"), "Course created successfully")

    """
        Supervisor should be able to create a course,
        Success: Course created successfully
        Failure: Course not created successfully
    """

    def test_course_creation_administrator_correct(self):
        fsa.command(login Administrator administratorPassword)
        self.assertEqual(self.fsa.command("create_course testCourse 999 wonderLand M-T-W-TR-F 9-9 SP20 jackson"), "Course created successfully")

    """
        Administrator should be able to create a course,
        Success: Course created successfully
        Failure: Course not created successfully
    """