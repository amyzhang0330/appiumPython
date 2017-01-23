# https://github.com/awslabs/aws-device-farm-sample-web-app-using-appium-python

import os
import unittest
from appium import webdriver
from time import sleep


class WebViewTests(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        self.driver = webdriver.Remote(
            'http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_get_url(self):
        self.driver.get("http://www.python.org")
        assert "Python" in self.driver.title
        sleep(5)
        screenshot_folder = os.getenv('SCREENSHOT_PATH', '/tmp')
        self.driver.save_screenshot(screenshot_folder + '/devicefarm.png')
        sleep(5)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WebViewTests)
    unittest.TextTestRunner().run(suite)
