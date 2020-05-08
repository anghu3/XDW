from Setting.setting_file import xdw_TestCase
from Setting.cycl import cycl_TestCase
import unittest
import time
from Setting.setting_file import login_name_user1,login_name_password1,login_name_user4,login_name_password4,setting_xls
import random
import xlrd

Testdata = xlrd.open_workbook(setting_xls)
sheet_passenger=Testdata.sheet_by_name('旅客信息')
sheet_goods=Testdata.sheet_by_name('物品信息')
sheet_goods_articles=Testdata.sheet_by_name('物品类别')

class xdwcy_TestCase(xdw_TestCase,cycl_TestCase):

    def Initialization(self):
        self.dr.find_element_by_xpath('//*[@id="b08e88dd0b16404cabbbe73e40028c6f"]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="a08f7d954d8f4e0eba9efee71839986a"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_a08f7d954d8f4e0eba9efee71839986a"]/iframe')
        self.dr.switch_to.frame(iframe)
        time.sleep(1)

    def test01_工作量汇总_查询(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()

    def test02_工作量汇总_导出(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        self.xdw_gzlhz_exprot()

if __name__ == '__main__':
    unittest.main()