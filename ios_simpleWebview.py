"""
Simple iOS WebView tests.
"""
import unittest
import os
from random import randint
from appium import webdriver
from time import sleep

from selenium.webdriver.common.keys import Keys

class WebViewIOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        app = os.path.join(os.path.dirname(__file__),
                           '../../apps/WebViewApp/build/release-iphonesimulator',
                           'WebViewApp.app')
        app = os.path.abspath(app)
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'deviceName': 'iPhone Simulator',
                'platformName': 'iOS',
                'browserName': 'Safari',
            })

    def tearDown(self):
        self.driver.quit()

    def test_get_url(self):
        self.driver.get("http://www.python.org")
        assert "Python" in self.driver.title
        sleep(1)

        self.driver.close()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WebViewIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
