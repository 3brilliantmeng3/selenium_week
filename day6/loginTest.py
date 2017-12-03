import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from day5.myTestCase import MyTestCase
from day6.page_object.loginPage import LoginPage
from day6.page_object.personalcenterPage import PersonalcenterPage


class LoginTest(MyTestCase):
    def test_login(self):

        # 1.打开网页
        # self.driver.get("http://localhost/index.php?m=user&c=public&a=login")
        lp = LoginPage(self.driver)  # 实例化一个登陆页面
        lp.open()
        # 2.输入用户名
        # self.driver.find_element(By.ID,"username").send_keys("meng")
        lp.input_username("meng")

        #2.输入密码
        # self.driver.find_element(By.ID,"password").send_keys("1234567890")
        lp.input_password("1234567890")
        # 4.点击登陆
        lp.click_login_button()
        # self.driver.find_element(By.CSS_SELECTOR,"body > div.login_main.w1180.clearfix > div.login.fr > form > ul > li:nth-child(5) > input").click()
        # 5.验证是否跳转到管理中心页面
        # expected = "用户登录 - 道e坊商城 - Powered by Haidao"

        # self.assertIn("我的会员中心",self.driver.title)
        pcp = PersonalcenterPage(self.driver)
        time.sleep(5)
        self.assertEqual(pcp.title, self.driver.title)


