# 有了mytestcase 以后,在写测试用例
import os

from  selenium  import webdriver
from day5.myTestCase import MyTestCase


class ZhuCeTest(MyTestCase):
    # 3个双引号,表示文档字符串,也是一种注释,和# 号的区别就是可以显示在文档中
    """注册模块测试用例组"""
    # 因为MyTestCase
    def test_zhu_ce(self):
        """打开注册页面的用例"""
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        # driver.current_url # 用来获取当前浏览器网址
        actual = driver.title  # 用來獲取当前浏览器标签页的title
        expected = "用户注册 - 道e坊商城 - Powered by Haidao"
        base_path= os.path.dirname(__file__)
        path = base_path.replace('day5','report/image/')
        driver.get_screenshot_as_file(path + "zhuce1.png")
        self.assertEqual(actual, expected)