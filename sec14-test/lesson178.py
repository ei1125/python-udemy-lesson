# mock
"""
$ pip install requests
"""

import unittest
from unittest.mock import MagicMock
import salary

class TestSalary(unittest.TestCase):
    def test_calculation_salary(self):
        s = salary.Salary(year=2017)
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        self.assertEqual(s.calculation_salary(), 101)
        #呼ばれているのか確認
        s.bonus_api.bonus_price.assert_called()
        s.bonus_api.bonus_price.assert_called_once()
        s.bonus_api.bonus_price.assert_called_with(year=2017)
        s.bonus_api.bonus_price.assert_called_once_with(
            year=2017)
        #何回呼ばれたか確認
        self.assertEqual(s.bonus_api.bonus_price.call_count, 1)

    def test_calculation_salary_no_salary(self):
        s = salary.Salary(year=2050)
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        self.assertEqual(s.calculation_salary(), 100)
        # 呼ばれて欲しくないのを確認
        s.bonus_api.bonus_price.assert_not_called()

if __name__ == '__main__':
    unittest.main()