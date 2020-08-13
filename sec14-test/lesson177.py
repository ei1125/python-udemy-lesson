# seleniumでUIの自動テスト
"""
$ pip install selenium
$ brew install geckodriver
"""

import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


"""
unittest化すると実行できない
そのまま入力だと実行できた
"""
# driver = webdriver.Chrome()
# driver.get('https://www.python.org')
# time.sleep(10)
# driver.close()
class PythonOrgTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_python_org(self):
        self.driver.get('https://www.python.org')
        time.sleep(10)
        # self.assertIn('Python', self.driver.title)

        # self.driver.find_element_by_link_text('Downloads').click()

        # element = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located(
        #         (By.CLASS_NAME, 'widget-title')))
        # self.assertEqual('Lookin for a specific release?', element.text)

        # self.driver.find_element_by_link_text('Documentation').click()

        # element = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located(
        #         (By.CLASS_NAME, 'call-to-action')))
        # self.assertIn('Browse the docs', element.text)

        # element = self.driver.find_element_by_name('q')
        # element.clear()
        # element.send_keys('pycon')
        # element.send_keys(Keys.RETURN)
        # assert 'No results found' not in self.driver.page_source

