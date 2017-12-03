import  unittest
from  selenium import webdriver
from selenium.webdriver.common.keys import Keys


class  DengLuTest(unittest.TestCase):
    """"登陆模块测试用例组"""
    def setUp(self):
        # 打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 浏览器的版本和 driver 的版本必须匹配
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()

    def test_denglu(self):
        """登陆测试正常情况测试用例"""
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        driver.find_element_by_id("username").send_keys("meng")
        # driver.find_element_by_id("password").send_keys("1234567890").send_keys(Keys.TAB).send_keys(Keys.ENTER)
        driver.find_element_by_id("password").send_keys("1234567890")
        # driver.find_element_by_class_name("login_btn fl").click()
        driver.find_element_by_css_selector("body > div.login_main.w1180.clearfix > div.login.fr > form > ul > li:nth-child(5) > input").click()
        print("当前用户")
        





