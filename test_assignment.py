import unittest
from list_approach import read_log_file, return_most_active_cookie
from pandas_approach import read_log_file,parse_input_date,return_most_active_cookie

class TestAssignment(unittest.TestCase):
    
    def test_pandas_date(self):
        result = parse_input_date('2018-12-09')
        self.assertEqual(1,1)


if __name__ == '__main__':
    
    unittest.main()
        