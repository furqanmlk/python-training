import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOOD', f"{'foo'.upper()} is not equal to foo")

    def test_notUpper(self):
        self.assertGreater(20, 10, "10 is greater than 20")

    def addTwoNumber(self, a, b):
        if type(a) != int or type(b) != int:

            raise ValueError("Please pass only integers values")

        return a+b

    # addTwoNumber(2,3) = 5, addTwoNumber(-2,3) = 1, addTwoNumber(0,3) = 3, addTwoNumber(@,3) = ?, addTwoNumber("2",3) = ?

    def test_twoPositive(self):
        self.assertTrue(self.addTwoNumber(2, 3), 5)

    def test_OnePositive(self):
        self.assertTrue(self.addTwoNumber(-2, 3), 1)

    def test_OneSpecialChar(self):
        with self.assertRaises(ValueError) as context:
            self.addTwoNumber('', 3)

        self.assertTrue("Please pass only integers values" in context.exception.args[0])


