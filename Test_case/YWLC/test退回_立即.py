from Setting.setting_file import xdw_TestCase
from Setting.cycl import cycl_TestCase
import unittest
import time
from Setting.setting_file import login_name_user1,login_name_password1,login_name_user4,login_name_password4,setting_xls
import xlrd
import random

Testdata = xlrd.open_workbook(setting_xls)
sheet_passenger=Testdata.sheet_by_name('旅客信息')
sheet_goods=Testdata.sheet_by_name('物品信息')


class xdwcy_TestCase(xdw_TestCase,cycl_TestCase):
    global test_num
    test_num = random.randint(1, 10)

    def Initialization_1(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        time.sleep(2)

    def Initialization_2(self):
        self.login_keyuan(login_name_user4, login_name_password4)
        time.sleep(2)

    def test01_退回_立即(self):
        self.Initialization_1()
        self.xdw_Inspection_addition(test_num, '退回', '立即')
        global id, jld_id
        id = self.dr.find_element_by_xpath('//*[@id="list"]/tbody[1]/tr/td[3]').text
        jld_id = self.dr.find_element_by_xpath('//*[@id="jldbh"]').get_attribute('value')

    def test02_现场退回记录(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.dr.find_element_by_xpath('//*[@id="dcefdfba1ea04e2db15876bd8673651d"]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="a5c5e173f18c4d0280bbfbf91b325b28"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_a5c5e173f18c4d0280bbfbf91b325b28"]/iframe')
        self.dr.switch_to.frame(iframe)
        self.dr.find_element_by_xpath('//*[@id="jldbh"]').send_keys(jld_id)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(2)
        self.assertEqual(jld_id,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[1]').text)


if __name__ == '__main__':
    unittest.main()