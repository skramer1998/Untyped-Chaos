from unittest import TestCase
from rational import Rational

class TestRational(TestCase):
    def setUp(self):
        self.negDen = Rational(0, -2)
    
    def test_posDen(self):
        self.assertTrue(self.negDen.d < 0)
