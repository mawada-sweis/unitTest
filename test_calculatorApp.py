import unittest
from unittest.mock import patch
from calculatorApp import *

class TestCalculate(unittest.TestCase):
    def setUp(self):
        print("Setup .. ")

    def test_AddPass(self):
        self.assertEqual(add(6,3), 9)# will execute the add
        self.assertEqual(calculate('1',6,3), 9) # will call the mock
        self.assertNotEqual(calculate('1',9,3), 9)

    def test_SubtractPass(self):
        self.assertEqual(subtract(6,3), 3)
        self.assertEqual(calculate('2',6,3), 3)

    def test_MultiplyPass(self):
        self.assertEqual(multiply(6,3), 18)
        result = (6, '*', 3, '=', 18)
        self.assertEqual(calculate('3',6,3), result)

    def test_DividePass(self):
        self.assertEqual(divide(6,3), 2)
        result = (6, '/', 3, '=', 2)
        self.assertEqual(calculate('4',6,3), result)
        with self.assertRaises(ZeroDivisionError):
            calculate('4', 5, '0')
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)
        self.assertEqual(divide(0, 3), 0)

    def test_invaliCalculate(self):
        with self.assertRaises(ValueError):
            calculate('1', "" ,3)
        with self.assertRaises(Exception):
            calculate('7', 5, 4)
    
    def test_isExit(self):
        self.assertEqual(isExit('no'), True)
        self.assertEqual(isExit('yes'), False)
        with self.assertRaises(ValueError):
            isExit('')
    
    def test_checkUserInput(self):
        with self.assertRaises(ValueError):
            check_user_input("")
        self.assertEqual(check_user_input('3.2'), 3.2)
        with self.assertRaises(ValueError):
            check_user_input("batekha")
    
    def tearDown(self):
        print("tearDown .. ")

if __name__ == '__main__':
	unittest.main()
