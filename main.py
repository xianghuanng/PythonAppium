"""
-*- coding: utf-8 -*-
File    : main.py
Version : 0.1
Author  : usrpi
Date    :2021/2/4
"""
import pytest
from TestCases.test_login_pytest import TestLogin

if __name__ == '__main__':
    pytest.main(['-vs','test_login_pytest.py'])