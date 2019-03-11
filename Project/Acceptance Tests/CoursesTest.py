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
            
            A database entry should be created for the course, if course creation is a success:
            - "Course created successfully."
            If input parameters are invalid or entry creation fails, failure:
            - "Error: Invalid parameters or database error"
            If user trying to create a course does not have access to do so, failure:
            - "Error: Access Denied"
        """

    # Correct Course Creation Tests
    def test_course_creation_supervisor_correct(self):
        self.fsa.command("login Supervisor supervisorPassword")
        self.assertEqual(self.fsa.command("create_course testCourse 999 wonderLand M-T-W-TR-F 9-9 SP20 jackson"), "Course created successfully")

    """
        Supervisor should be able to create a course,
        Success: Course created successfully
        Failure: Course not created successfully
    """

    def test_course_creation_administrator_correct(self):
        self.fsa.command("login Administrator administratorPassword")
        self.assertEqual(self.fsa.command("create_course testCourse 999 wonderLand M-T-W-TR-F 9-9 SP20 jackson"), "Course created successfully")

    """
        Administrator should be able to create a course,
        Success: Course created successfully
        Failure: Course not created successfully
    """

    # Failed Course Creation Tests
    def test_course_creation_instructor(self):
        self.fsa.command("login Instructor instructorPassword")
        self.assertEqual(self.fsa.command("create_course testCourse 999 wonderLand M-T-W-TR-F 9-9 SP20 jackson"), "Error: Access Denied")

    """
        Instructor should not be able to create a course,
        Success: Course not created successfully
        Failure: Course created successfully
    """

    def test_course_creation_ta(self):
        self.fsa.command("login TA taPassword")
        self.assertEqual(self.fsa.command("create_course testCourse 999 wonderLand M-T-W-TR-F 9-9 SP20 jackson"), "Error: Access Denied")

    """
        TA should not be able to create a course,
        Success: Course not created successfully
        Failure: Course created successfully
    """

    def test_course_creation_invalid_params(self):
        self.fsa.command("login Supervisor supervisorPassword")
        self.assertEqual(self.fsa.command("create_course hello"), "Error: Invalid parameters or database error")

    """
        Trying to create a course with invalid parameters should not create a course,
        Success: Course not created successfully
        Failure: Course created successfully
    """

    #Correct Course Editing Tests
    def test_course_edit_correct(self):
        self.fsa.command("login Supervisor supervisorPassword")
        self.assertEqual(self.fsa.command("edit_course 361 name softwareSupplies"), "Course name updated.")
        self.assertEqual(self.fsa.command("edit_course 361 number 362"), "Course number updated.")
        self.assertEqual(self.fsa.command("edit_course 362 place laphamHall"), "Course place updated.")
        self.assertEqual(self.fsa.command("edit_course 362 days M-W-TR"), "Course days updated.")
        self.assertEqual(self.fsa.command("edit_course 362 times 10-11"), "course times updated.")
        self.assertEqual(self.fsa.command("edit_course 362 semester SP20"), "Course semester updated.")
        self.assertEqual(self.fsa.command("edit_course 362 professor james"), "Course professor updated.")
        self.assertEqual(self.fsa.command("edit_course 362 ta albany"), "Course ta updated.")
        self.assertEqual(self.fsa.command("edit_course 362 lab M-W"), "Course lab updated.")

    def test_course_view_supervisor(self):
        self.fsa.command("login Supervisor supervisorPassword")
        self.assertEqual(self.fsa.command("edit_course 361 name"), "softwareEngineering")
        self.assertEqual(self.fsa.command("edit_course 361 number"), "361")
        self.assertEqual(self.fsa.command("edit_course 361 place"), "lubarHall")
        self.assertEqual(self.fsa.command("edit_course 361 days"), "T-TR")
        self.assertEqual(self.fsa.command("edit_course 361 times"), "10-10:50")
        self.assertEqual(self.fsa.command("edit_course 361 semester"), "SP19")
        self.assertEqual(self.fsa.command("edit_course 361"), "rock")
        self.assertEqual(self.fsa.command("edit_course 361"), "apoorv")
        self.assertEqual(self.fsa.command("edit_course 361 lab"), "1")

    def test_course_view_administrator(self):
        self.fsa.command("login Administrator administratorPassword")
        self.assertEqual(self.fsa.command("edit_course 361 name"), "softwareEngineering")
        self.assertEqual(self.fsa.command("edit_course 361 number"), "361")
        self.assertEqual(self.fsa.command("edit_course 361 place"), "lubarHall")
        self.assertEqual(self.fsa.command("edit_course 361 days"), "T-TR")
        self.assertEqual(self.fsa.command("edit_course 361 times"), "10-10:50")
        self.assertEqual(self.fsa.command("edit_course 361 semester"), "SP19")
        self.assertEqual(self.fsa.command("edit_course 361"), "rock")
        self.assertEqual(self.fsa.command("edit_course 361"), "apoorv")
        self.assertEqual(self.fsa.command("edit_course 361 lab"), "1")

    def test_course_view_instructor(self):
        self.fsa.command("login Instructor instructorPassword")
        self.assertEqual(self.fsa.command("edit_course 361 name"), "softwareEngineering")
        self.assertEqual(self.fsa.command("edit_course 361 number"), "361")
        self.assertEqual(self.fsa.command("edit_course 361 place"), "lubarHall")
        self.assertEqual(self.fsa.command("edit_course 361 days"), "T-TR")
        self.assertEqual(self.fsa.command("edit_course 361 times"), "10-10:50")
        self.assertEqual(self.fsa.command("edit_course 361 semester"), "SP19")
        self.assertEqual(self.fsa.command("edit_course 361"), "rock")
        self.assertEqual(self.fsa.command("edit_course 361"), "apoorv")
        self.assertEqual(self.fsa.command("edit_course 361 lab"), "1")

    def test_course_view_TA(self):
        self.fsa.command("login TA taPassword")
        self.assertEqual(self.fsa.command("edit_course 361 name"), "softwareEngineering")
        self.assertEqual(self.fsa.command("edit_course 361 number"), "361")
        self.assertEqual(self.fsa.command("edit_course 361 place"), "lubarHall")
        self.assertEqual(self.fsa.command("edit_course 361 days"), "T-TR")
        self.assertEqual(self.fsa.command("edit_course 361 times"), "10-10:50")
        self.assertEqual(self.fsa.command("edit_course 361 semester"), "SP19")
        self.assertEqual(self.fsa.command("edit_course 361"), "rock")
        self.assertEqual(self.fsa.command("edit_course 361"), "apoorv")
        self.assertEqual(self.fsa.command("edit_course 361 lab"), "1")



