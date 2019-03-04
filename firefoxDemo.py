#coding:utf-8

#import unittest
from selenium import webdriver

# 加启动配置、规避chrome正受到自动测试软件的控制信息弹出
option=webdriver.ChromeOptions()
option.add_argument('disable-infobars')

# 加时延5秒关闭 chrome最大化打开百度
import time
driver=webdriver.Chrome(chrome_options=option)

# 正常账号密码登录lavaradio官网，无异常
driver.get("http://www.lavaradio.com")
# 最大化
driver.maximize_window()
time.sleep(1)
# 利用属性class元素定位方法
driver.implicitly_wait(10)
driver.find_element_by_class_name('loginBtn').click()
#time.sleep(1)
driver.find_element_by_class_name('registerName').clear()
#time.sleep(1)
driver.find_element_by_class_name('registerName').send_keys('Gzzweb')
#time.sleep(1)
driver.find_element_by_class_name('registerPsd').clear()
#time.sleep(1)
driver.find_element_by_class_name('registerPsd').send_keys('1234567')
#time.sleep(1)

# 用class定位时若字符串中间存在空格，选择find_element_by_css_seletor()方法定位
driver.find_element_by_css_selector("[class='saveRegister registerBtn']").click()
time.sleep(3)

#刷新页面，查看登录状态
#driver.get("http://www.lavaradio.com")

#login out

driver.find_element_by_class_name('loginSpan').click()
time.sleep(1)
driver.find_element_by_class_name('logOut').click()
time.sleep(3)

#正常短信验证码登录，没有解决获取手机验证码的问题，先用148
driver.find_element_by_class_name('loginBtn').click()
#time.sleep(2)
driver.find_element_by_css_selector("[class='phoneShortCut']").click()
#time.sleep(2)
driver.find_element_by_class_name('registerTel').send_keys('14878785656')
#time.sleep(2)
driver.find_element_by_class_name('getCodeBtn').click()
#time.sleep(2)
driver.find_element_by_class_name('authCodes').send_keys('123456')
#time.sleep(2)
driver.find_element_by_css_selector("[class='saveRegister noteBtn']").click()
time.sleep(3)
driver.quit()

# 缺 def ！！！！调用
# 缺 短验处理
# 缺 循环
# 缺 用例设计
# 缺 调试报错信息处理
# 缺 服务器布置、邮件报告
# 缺 参数化









