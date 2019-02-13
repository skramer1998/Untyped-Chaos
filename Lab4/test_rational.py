from unittest import TestCase
from rational import Rational


class TestRational(TestCase):

    def setUp(self):
        self.negDen = Rational(0, -2)
        self.good = Rational()
        self.badCon = Rational('hello', '34')
        self.rat1 = Rational(1, 2)
        self.rat2 = Rational(2, 3)
        self.rat3 = Rational(1, 4)
        self.rat4 = Rational(7, 4)
    
    def test_posDen(self):
        self.assertTrue(self.negDen.d > 0)

    """Test Case Ideas"""
    def test_badConstructor(self):
        self.assertRaises(SomeException, self.badCon)


    def test_add(self):
        self.assertEqual(self.rat1.__add__(0), self.rat1, "please stay the same value when adding zero")
        self.assertNotEqual(self.rat1.__add__(self.rat1), self.rat1, "please don't stay the same value when adding not zero")
        self.assertEqual(self.rat3.__add__(self.rat3), self.rat1, "1/4 + 1/4 should equal 1/2")
        self.assertRaises(SomeException(), self.rat1.__add__("cheese"), "if it doesn't raise an exception shit's not great")
