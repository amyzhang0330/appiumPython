# https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/mobile-web.md

"""
Simple WebView tests, run in SauceLabs.
"""
import unittest
from appium import webdriver
from time import sleep


class WebViewTests(unittest.TestCase):

    def setUp(self):

        SAUCE_USERNAME = ''
        SAUCE_ACCESS_KEY = ''
        self.driver = webdriver.Remote(
            command_executor='http://'+SAUCE_USERNAME+':'+SAUCE_ACCESS_KEY+'@ondemand.saucelabs.com:80/wd/hub',
            desired_capabilities=
            # {
            #     # 'app': app,
            #     'deviceName': 'iPhone 6',
            #     'platformName': 'iOS',
            #     'platformVersion': '7.1',
            #     'browserName': 'Safari'
            # }
            {
                'platformName': 'Android',
                'platformVersion': '5.0',
                'deviceName': 'Android Emulator',
                'deviceType': 'tablet',
                'browserName': 'Browser'
            }
        )

    def tearDown(self):
        self.driver.quit()

    def test_get_url(self):
        self.driver.get("http://www.python.org")
        assert "Python" in self.driver.title
        sleep(1)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WebViewTests)
    unittest.TextTestRunner().run(suite)