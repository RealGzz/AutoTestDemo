# -*- coding: utf-8 -*-

import unittest
import pymysql
from selenium import webdriver
import time

#定义测试类
class LoginTestCase(unittest.TestCase):
# 打开浏览器
    def setUp(self):
        print("测试用例执行开始：")
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        self.driver=webdriver.Chrome(chrome_options=option)
        self.driver.implicitly_wait(5)
# 关闭浏览器、还原
    def tearDown(self):
        self.driver.quit()
        print("测试用例执行结束!")
        print('--------------------')
# 注意test_开头
    def test_login(self):
        '''用户名密码登录'''
        driver=self.driver
        driver.get("http://www.lavaradio.com")
        driver.find_element_by_class_name('loginBtn').click()
        driver.find_element_by_class_name('registerName').clear()
        driver.find_element_by_class_name('registerName').send_keys('Gzzweb')
        driver.find_element_by_class_name('registerPsd').clear()
        driver.find_element_by_class_name('registerPsd').send_keys('1234567')
        driver.find_element_by_css_selector("[class='saveRegister registerBtn']").click()
        time.sleep(3)
        print('1.用户名密码登录成功')
        #po=driver.find_element_by_partial_link_text("账户信息")

        #self.assertTrue('账户信息'in po.text)
        #self.assertEqual(po.text,'账户信息')

    def test_phoneCutlogin(self):
        "短信验证码登录"
        driver=self.driver
        driver.get("http://www.lavaradio.com")
        driver.find_element_by_class_name('loginBtn').click()
        driver.find_element_by_css_selector("[class='phoneShortCut']").click()
        driver.find_element_by_class_name('registerTel').send_keys('14878785656')
        """连接数据库相关
        db=pymysql.connect(host="",user="",password="",port=3306)
        try:
            cursor=db.cursor()
            sql="select * from d_sms_list where mobile='14878785656'"
            cursor.execute(sql)
            results=cursor.fetchall()
            for row in results:
                    id = row(0)
                    print("id=%s"%(id))
        except:
            print("数据库查询error")
        """
        driver.find_element_by_class_name('getCodeBtn').click()
        driver.find_element_by_class_name('authCodes').send_keys('1234567')
        driver.find_element_by_css_selector("[class='saveRegister noteBtn']").click()
        time.sleep(3)
        print('2.手机验证码登录成功')

    if __name__ == '__main__':
        unittest.main(verbosity=2)
