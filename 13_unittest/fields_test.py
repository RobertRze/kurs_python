import unittest
from fields import rectangle, triangle, trapeze


class FieldsTestCase(unittest.TestCase):
    def setUp(self):
        self.a = 10
        self.b = 5
        self.h = 5
    def test_rectangle_with_correct_values(self):
        result = rectangle(self.a, self.b)
        self.assertEqual(result, 50)

    def test_rectangle_with_incorrect_values(self):
#        self.assertRaises(ValueError, rectangle, True, 'string')
        with self.assertRaises(ValueError):
            rectangle(self.a, "błąd")

    def test_triangle_with_correct_values(self):
        result = triangle(self.a, self.b)
        self.assertEqual(result, 25)

    def test_triagle_with_incorrect_values(self):
        with self.assertRaises(ValueError):
            triangle(self.a, "błąd")

    def test_trapeze_with_correct_values(self):
        result = trapeze(self.a, self.b, self.h)
        expected_result = 37.5
        self.assertEqual(result, expected_result)

    def test_trapeze_with_incorect_value(self):
        with self.assertRaises(ValueError):
            trapeze(self.a, self.b, "błąd")

    def tearDown(self):
        del self.a
        del self.b
        del self.h

if __name__ == '__main__':
    unittest.main()
