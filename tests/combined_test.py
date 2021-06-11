import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from appium import webdriver as wd

class TestSuite(unittest.TestCase):
    SYSTEM = ''

    def setUp(self):
        if self.SYSTEM == 'web':
            self.__webSetup()
        elif self.SYSTEM == 'iOS':
            self.__iosSetup()
        else:
            raise NameError('Wrong SYSTEM variable: {}'.format(self.SYSTEM))

    def testTitle(self):
        header = self.__findIdOrXpath("header", "//XCUIElementTypeStaticText[1]")
        self.assertEqual("Hello Selenium", header.text)

    def testButton(self):
        button = self.__findIdOrXpath("button", "//XCUIElementTypeButton")
        saying = self.__findIdOrXpath("saying", "//XCUIElementTypeStaticText[2]")

        before = saying.text
        button.click()
        self.assertNotEqual(before, saying.text)
        self.assertEqual("heyy", saying.text) 

    def tearDown(self):
        self.driver.quit()

    def __findIdOrXpath(self, id: str, xpath: str):
        if self.SYSTEM == 'web':
            return self.driver.find_element_by_id(id)
        else:
            return self.driver.find_element_by_xpath(xpath)

    def __iosSetup(self):
        self.desired_caps = dict(
            platformName='iOS',
            platformVersion='14.5',
            automationName='xcuitest',
            deviceName='iPhone Simulator',
            noReset=True,
            app='/Users/andrewk/Library/Developer/Xcode/DerivedData/basicApp-bdratripqbsilgffnpiksscrhbrq/Build/Products/Debug-iphonesimulator/basicApp.app'
        )
        self.driver = wd.Remote('http://localhost:4723/wd/hub', self.desired_caps)


    def __webSetup(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get("http://localhost:8080/")



if __name__ == '__main__':
    TestSuite.SYSTEM = 'web'
    unittest.main()
