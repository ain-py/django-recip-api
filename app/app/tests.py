"""
Sample test
all functions must start with test_*
"""
from django.test import SimpleTestCase
from app import calc

class CalcTest(SimpleTestCase):
    def test_add_num(self):
        res = calc.add(5,6)
        self.assertEqual(res,11)
    
    def test_sub_num(self):
        res = calc.sub(15,10)
        self.assertEqual(res,5)