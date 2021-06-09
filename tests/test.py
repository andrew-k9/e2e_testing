import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://localhost:8080/")


class TestWebPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get("http://localhost:8080/")

    def test_title(self):
        header = self.driver.find_element_by_id("header")
        self.assertEqual("Hello Selenium", header.text)

    def test_button(self):
        button = self.driver.find_element_by_id("button")
        saying = self.driver.find_element_by_id("saying")

        before = saying.text
        button.click()
        self.assertNotEqual(before, saying.text)
        self.assertEqual("heyy", saying.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
