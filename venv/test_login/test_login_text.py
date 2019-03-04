# -*- coding: utf-8 -*-

import unittest
from test_login import LoginTestCase

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(LoginTestCase))

    with open('UnittestTextReport.txt', 'a') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)
