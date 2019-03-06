class Supervisor:

    def __init__(self):
        """Constructor for Supervisor."""
        self.userName = "supervisor"
        self.ID = "0001"
        self.email = "sprvsr@uwm.edu"
        self.phone = "555-555-5555"
        self.address = "homeless"

    def __createCourse__(self, course):
        """returns a new course"""
        pass

    def __editCourse__(self, course):
        """no return, edits course data"""

    def __createAccount__(self, account):
        """returns a new account"""
        pass

    def __modifyAccount__(self, account):
        """No return, modifies an account"""
        pass

    def __editSelf__(self):
        """no return, edits own data"""
        pass

    def __publicInfo__(self, user):
        """no return, displays public data on user"""
        pass

    def __privateInfo__(self, user):
        """no return, displays private data on user"""

    def __assignTA__(self, section, user):
        """assigns the TA to the lab or course section"""
        pass

    def __assignInstructor__(self, course, user):
        """assigns the instructor to a course"""
        pass

    def __notifyAll__(self):
        """no return, sends an email to every user"""
        pass