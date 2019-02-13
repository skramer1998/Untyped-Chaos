from unittest import TestCase
from rational import Rational


class TestRational(TestCase):
    def setUp(self):
        self.negDen = Rational(0, -2)
        self.good = Rational()
        self.badCon = Rational('hello', '34')
    
    def test_posDen(self):
        self.assertTrue(self.negDen.d < 0)

    """Test Case Ideas"""
    def test_badConstructor(self):
        self.assertRaises(SomeException, self.badCon)


    def test_add(self):
        self.assertEquals(self.add(0), self)
