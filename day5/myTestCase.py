import  unittest
from  selenium import webdriver
from selenium.webdriver.common.keys import Keys


class  MyTestCase(unittest.TestCase):
    def setUp(self):
        # 打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 浏览器的版本和 driver 的版本必须匹配
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()