# !/usr/bin/python
# -*- coding:utf-8 -*-

import time
import unittest
from  framework.browser_engine import BrowserEngine
from logs.logger import Logger

logger = Logger(logger="BaiduSearch").getlog()

class BaiduSearch(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserEngine(self)
        self.driver = self.browser.open_browser(self)

    def tearDown(self):
        logger.info("Now,Close and quit the browser.")
        # print(self.driver)
        self.driver.quit()

    def test_baidu_search(self):
        try:
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[3]/div/div[1]/div/p/i').click()
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[3]/div/div[1]/div/div/div/input').send_keys("maya")
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[3]/div/div[1]/div/div/div/span/span/i[2]').click()
            time.sleep(3)
            logger.info("aboutcg index page search maya")
            print(self.driver.title())
            time.sleep(11)
            assert 'maya' in self.driver.title
            logger.info("OK")
        except Exception as e:
            logger.info("Test Fail:%s" % format(e))

if __name__ == '__main__':
    unittest.main()