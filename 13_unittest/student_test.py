import unittest
from student import Student

class TestStudent(unittest.TestCase):
    def setUp(self) -> None:

    def test_email(self):
        anna = Student('anna', 'snow', 4.6)
        self.assertEqual(anna.email, 'anna.snow@uam.com')


    def test_full(self):
        anna = Student('anna', 'snow', 4.6)
        expected_result = 'Anna Snow'
        self.assertEqual(anna.fullname, expected_result)
        anna.last = 'SNOW'
        self.assertEqual(anna.fullname, expected_result)
        anna.name = 'ANNA'
        self.assertEqual(anna.fullname, expected_result)
        anna.name = 'aNNA'
        self.assertEqual(anna.fullname, expected_result)

    def test_scholarship(self):
        anna = Student('anna', 'snow', 4.6)
        adam = Student('adam', 'kowalski', 3.0)


        anna.grant_scholarship()
        self.assertTrue(anna.grant_scholarship)

        adam.grant_scholarship()
        self.assertTrue(adam.grant_scholarship)

