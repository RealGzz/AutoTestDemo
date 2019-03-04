# -*- coding: utf-8 -*-

#直接调用test_login文件的 LoginTestCase这个测试用例类
"""
直接调用test_login文件的 LoginTestCase这个测试用例类，
或者不用from test_login import LoginTestCase，直接suite.addTests(unittest.TestLoader().loadTestsFromName('test_login.LoginTestCase'))"""
import unittest
from test_login import LoginTestCase

if __name__=='__main__':
    #测试用例集合定义
    suite=unittest.TestSuite()

    """suite.addTests(unittest.TestLoader().loadTestsFromName('test_login.LoginTestCase'))"""
    #把LoginTestCase类添加到测试用例集合中
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(LoginTestCase))
    #调用runner的run方法执行用例
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite)