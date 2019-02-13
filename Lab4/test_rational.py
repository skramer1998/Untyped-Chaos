from unittest import TestCase
from rational import Rational

class TestRational(TestCase):
    def setUp(self):
       rat = Rational()
    
    def test_posDen(self):
        self.assertTrue(rat.d > 0);
    
    def 
