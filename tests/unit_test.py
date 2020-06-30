import unittest
from app.utilities.utils import print_test_time_elapsed


class UnitTests(unittest.TestCase):
    def setUp(self):
        print('\n starting...')

    def tearDown(self):
        print('\n completed!!!')

    @print_test_time_elapsed
    def test_case_1(self):
        pass

    @print_test_time_elapsed
    def test_case_2(self):
        pass


if __name__ == '__main__':
    unittest.main()
