import unittest
from appium import webdriver

class TestiOSApp(unittest.TestCase):

    def setUp(self):
        self.desired_caps = dict(
            platformName='iOS',
            platformVersion='14.5',
            automationName='xcuitest',
            deviceName='iPhone Simulator',
            noReset=True,
            app='/Users/andrewk/Library/Developer/Xcode/DerivedData/basicApp-bdratripqbsilgffnpiksscrhbrq/Build/Products/Debug-iphonesimulator/basicApp.app'
        )
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)

    def test_title(self):
        header = self.driver.find_element_by_xpath("//XCUIElementTypeStaticText[1]")
        self.assertEqual("Hello Selenium", header.text)

    def test_button(self):
        button = self.driver.find_element_by_xpath("//XCUIElementTypeButton")
        saying = self.driver.find_element_by_xpath("//XCUIElementTypeStaticText[2]")

        before = saying.text
        button.click()
        self.assertNotEqual(before, saying.text)
        self.assertEqual("heyy", saying.text)

    def tearDown(self):
        self.driver.quit()
     

if __name__ == '__main__':
    unittest.main()
