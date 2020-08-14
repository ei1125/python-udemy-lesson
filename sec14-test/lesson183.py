# どこまでmockするか

"""
自分のコードget_from_bossをmoc化
"""

import unittest
from unittest.mock import MagicMock
from unittest import mock

import salary

class TestSalary(unittest.TestCase):

    @mock.patch('salary.ThirdPartyBonusRestApi', spec=True)
    @mock.patch('salary.Salary.get_from_boss')
    def test_calculation_salary_class(
            self, mock_boss, mock_rest):
        mock_boss.return_value = 10
        mock_rest = mock_rest.return_value
        # mock_rest = MockRest()
        mock_rest.bonus_price.return_value = 1
        mock_rest.get_api_name.return_value = 'Money'

        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()

        self.assertEqual(salary_price, 111)
        mock_rest.bonus_price.assert_called()

if __name__ == '__main__':
    unittest.main()