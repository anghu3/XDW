from Setting.setting_file import xdw_TestCase
from Setting.cycl import cycl_TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from Setting.setting_file import login_name_user1,login_name_password1,login_name_user4,login_name_password4,setting_xls
from Setting.menu import data
import xlrd
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

Testdata = xlrd.open_workbook(setting_xls)
sheet_passenger=Testdata.sheet_by_name('旅客信息')
sheet_goods=Testdata.sheet_by_name('物品信息')

class xdw_TestCase(xdw_TestCase,cycl_TestCase):

    global now
    now = time.strftime("%Y-%m-%d", time.localtime(time.time()))

    def test01_销毁(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        # self.Initialization()
        test_num = random.randint(1, 10)
        self.xdw_Inspection_addition(test_num,'销毁','')

    def test02_退回_立即(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        test_num = random.randint(1, 10)
        self.xdw_Inspection_addition(test_num,'退回','立即')

    def test03_退回_限期(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        test_num = random.randint(1, 10)
        self.xdw_Inspection_addition(test_num, '退回', '限期')

    def test04_截留_移交法制部门(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        test_num = random.randint(1, 10)
        self.xdw_Inspection_addition(test_num, '截留', '移交法制部门')

    def test05_截留_补办手续(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        test_num = random.randint(1, 10)
        self.xdw_Inspection_addition(test_num, '截留', '补办手续')

    def test06_截留_实验室检疫(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        test_num = random.randint(1, 10)
        self.xdw_Inspection_addition(test_num, '截留', '实验室检疫')

    def test07_截留_风险评估(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        test_num = random.randint(1, 10)
        self.xdw_Inspection_addition(test_num, '截留', '风险评估')

    def test08_放行(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        test_num = random.randint(1, 10)
        self.xdw_Inspection_addition(test_num, '放行', '')

    def test09_隔离检疫(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        test_num = random.randint(1, 10)
        self.xdw_Inspection_addition(test_num, '隔离检疫', '')

if __name__ == '__main__':
    unittest.main()