import unittest

class CoursesTest(unittest.TestCase):
    def setup(self):

        self.fsa.command("create_course softwareEngineering 361 lubarHall T-TR 10-10:50 SP19 rock apoorv 1")
        self.fsa.command("create_course algorithmDesign 535 EMS M-W 4-5:15 SP19 cheng")
        self.fsa.command("create_course security 469 EMS T-TR 10-10:50 SP19 bob")
        self.fsa.command("create_course operatingSystems 550 physics M-W-F 8-8:50 SP19 sorensen jimbo-allen 2")

        """
            self.fsa.command("create_course course_name course_number course_place course_days course_time course_semester course_professor course_tas course_labs")
        
            When the create course command is entered, it takes 11 arguments:
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
            - "Error creating account."
        """