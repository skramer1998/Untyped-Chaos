class TA:
    """
    A class representing a TA.
    """
    def __init__(self):
        """Constructor for TA."""
        self.userName = "none"
        self.accID = "none"
        self.email = "none"
        self.phone = "none"
        self.address = "none"
        self.courses = "none"
        self.labSection = "none"


    def __viewTAAssignments__(self):
        """View your TA assignment"""
        return self.labSection