from django.test import TestCase
from app.calc import add, subtract


class CalcTests(TestCase):

    def test_add_number(self):
        """Tests that two numbers are added together"""
        self.assertEquals(add(8, 4), 12)

    def test_subtract_number(self):
        """Test that two numbers are subtracted properly"""
        self.assertEquals(subtract(8, 4), 4)
