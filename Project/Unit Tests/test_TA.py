from unittest import TestCase
from Project.Classes.TA import TA

class TestTA(TestCase):

    def setUp(self):
        self.default = TA()
        self.namedTom = TA()

    """
    Need to test editing each piece of information that TAs are allowed to edit (personal informaton)
    """
    def test__editSelf__(self):
        self.assertEqual(self.default.__editSelf__(self.default, "userName=tom"), self.namedTom)

    """
    Need to test which data gets returned and build object in setUp that replicate it
    """
    def test__publicInfo__(self):
        self.assertEqual(self.default.__publicInfo__(), self.default)

    """
    Need to test assignments for courses and lab sections
    """
    def test__viewTAAssignments__(self):
        self.assertEqual(self.default.__viewTAAssignments__(), "361")

    pass
