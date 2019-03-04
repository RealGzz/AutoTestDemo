# -*- coding: utf-8 -*-

import unittest
from test_login import LoginTestCase
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    testsuite=unittest.TestSuite()
    #tests = [LoginTestCase("test_login"), LoginTestCase("test_phoneCutlogin")]
    #suite.addTests(tests)
    testsuite.addTests(unittest.TestLoader().loadTestsFromTestCase(LoginTestCase))

    with open('TestReportSir.html','wb') as fp:
        runner = HTMLTestRunner(stream=fp,
                                title='自动化登录报告',
                                description='用例执行情况：')
        runner.run(testsuite)
    #fp.close()

