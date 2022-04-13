
import unittest
from selenium import webdriver

class E2ETests(unittest.TestCase):

    def setUp(self):
        firefox_driver = 'Users\Home\Documents\geckodriver'
        self.driver = webdriver.Firefox(executable_path=firefox_driver)
        self.driver.get('http://localhost:5000')

    def tearDown(self):
        self.driver.quit()

    def test_browser_title_contains_app_names(self):
        self.assertIn('Named Entity', self.driver.title)