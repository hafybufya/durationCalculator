import unittest
from  mainCode import date_time_calc
import numpy as np
# define the unit tests
class my_unit_tests(unittest.TestCase):

        # tests if date difference is correctly caculated
    def test_date_difference(self):
        """"""
        today = np.datetime64('2025-10-20')
        user_inputed_test_date = date_time_calc("2025-10-10")
        result = today - np.datetime64(user_inputed_test_date)
        expected_result = np.timedelta64(10, 'D')  #expected result

        self.assertEqual(expected_result, result)


    # run the tests
if __name__ == "__main__":
    unittest.main()

