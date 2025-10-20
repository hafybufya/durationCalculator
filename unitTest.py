import unittest
from  mainCode import date_time_calc
import numpy as np
# define the unit tests
class my_unit_tests(unittest.TestCase):

    def test_date_difference(self):
        """Test that date difference is calculated correctly."""
        actual_result = date_time_calc("2025-10-10")
        expected_result = np.datetime64('today') - np.datetime64("2025-10-10")
        self.assertEqual(actual_result, expected_result)



    # run the tests
if __name__ == "__main__":
    unittest.main()

