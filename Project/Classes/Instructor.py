class Instructor:
    """
    A class representing an Instructor.
    """
    def __init__(self):
        """Constructor for Instructor."""
        self.userName = "none"
        self.accID = "none"
        self.email = "none"
        self.phone = "none"
        self.address = "none"
        self.courses = "none"
        self.labSection = "none"

    def __editSelf__(self, other):
        """Edit personal information"""
        return Instructor()

    def __publicInfo__(self):
        """View public info"""
        #return data
        pass

    def __viewTAAssignments__(self):
        """View your TA assignments"""
        return self.labSection

    def __viewCourseAssignments__(self):
        """View your course assignments"""
        return self.courses

    def __assignTAs__(self, other, other2):
        """Assign TAs to lab sections"""
        #return data
        pass

    def __msgTAs__(self):
        """Message TAs in your courses"""
        return