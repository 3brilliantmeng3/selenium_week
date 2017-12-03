import unittest

import time

from day5.myTestCase import MyTestCase
from day6.data_base.connectDB import connectDb


class ZhuCeTest(MyTestCase):
    def test_zhu_ce(self):
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver.find_element_by_name("username").send_keys("daxiaxia")
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_name("userpassword2").send_keys("123456")
        driver.find_element_by_name("mobile_phone").send_keys("18665432565")
        driver.find_element_by_name("email").send_keys("98787@qq.com")
        driver.find_element_by_class_name("reg_btn").click()
        # 检查数据库中,新增的记录的用户名和我们新注册的用户名是否一致
        expected = "daxiaxia"
        time.sleep(3)
        actual = connectDb()[1]
        self.assertEqual(expected,actual)
        print(connectDb()[1])

