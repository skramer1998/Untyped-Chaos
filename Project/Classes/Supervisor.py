class Supervisor:

    def _init_(self):
        """Constructor for Supervisor."""
        self.userName = "supervisor"
        self.ID = "0001"
        self.email = "sprvsr@uwm.edu"
        self.phone = "555-555-5555"
        self.address = "homeless"

    def createCourse(self, course):
        """returns a new course"""
        pass

    def editCourse(self, course):
        """no return, edits course data"""

    def createAccount(self, account):
        """returns a new account"""
        pass

    def modifyAccount(self, account):
        """No return, modifies an account"""
        pass

    def editSelf(self):
        """no return, edits own data"""
        pass

    def publicInfo(self, user):
        """no return, displays public data on user"""
        pass

    def privateInfo(self, user):
        """no return, displays private data on user"""

    def assignTA(self, section, user):
        """assigns the TA to the lab or course section"""
        pass

    def assignInstructor(self, course, user):
        """assigns the instructor to a course"""