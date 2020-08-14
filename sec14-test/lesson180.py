# mock.patch
"""
$ pip install requests
"""

import unittest
from unittest.mock import MagicMock
from unittest import mock

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
    
    #あらかじめmockを使う宣言をする
    # @mock.patch('salary.ThirdPartyBonusRestApi.bonus_price',
    #             return_value=1)
    @mock.patch('salary.ThirdPartyBonusRestApi.bonus_price')
    def test_calculation_salary_no_salary(self, mock_bonus):
        mock_bonus.return_value = 1

        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()

        self.assertEqual(salary_price, 101)
        mock_bonus.assert_called()

     
    def test_calculation_salary_patch_with(self):
        with mock.patch(
                'salary.ThirdPartyBonusRestApi.bonus_price') as mock_bonus:
            mock_bonus.return_value = 1

            s = salary.Salary(year=2017)
            salary_price = s.calculation_salary()

            self.assertEqual(salary_price, 101)
            mock_bonus.assert_called()

    def setUp(self):
        self.patcher = mock.patch('salary.ThirdPartyBonusRestApi.bonus_price')
        self.mock_bonus = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_calculation_salary_patch_patcher(self):
        self.mock_bonus.return_value = 1

        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()

        self.assertEqual(salary_price, 101)
        self.mock_bonus.assert_called()

if __name__ == '__main__':
    unittest.main()