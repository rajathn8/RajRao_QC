import unittest
from list_approach import read_log_file, return_most_active_cookie


class TestAssignment(unittest.TestCase):

    def test_read_file(self):
        result = read_log_file('QC.csv', '2018-12-09')
        self.assertIsNotNone(result)

    def test_return_most_active_cookie_1(self):
        '''
        Input date is there in the log file
        '''
        result = return_most_active_cookie(
            read_log_file('QC.csv', '2018-12-09'))
        self.assertEqual(['AtY0laUfhglK3lC7'], result)

    def test_return_most_active_cookie_2(self):
        '''
        Input date is not present in the Log File
        '''
        result = return_most_active_cookie(
            read_log_file('QC.csv', '2018-12-22'))
        self.assertEqual(['No Cookie for Mentioned Date'], result)


if __name__ == '__main__':

    unittest.main()
