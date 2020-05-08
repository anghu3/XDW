from Setting.setting_file import xdw_TestCase
from Setting.cycl import cycl_TestCase
import unittest
import time
from Setting.setting_file import login_name_user1,login_name_password1,login_name_user4,login_name_password4,setting_xls
import random


class xdwcy_TestCase(xdw_TestCase,cycl_TestCase):

    def Initialization(self):
        self.dr.find_element_by_xpath('//*[@id="dcefdfba1ea04e2db15876bd8673651d"]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="2de3690e1692476caa343748aa27c5ec"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_2de3690e1692476caa343748aa27c5ec"]/iframe')
        self.dr.switch_to.frame(iframe)
        time.sleep(1)

    def test01_销毁出库单据_查询_销毁单号(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'xhdh':'XH0000001907108','wpbh':'','start':'','end':'','ckr':''}
        self.xdw_xhckdj_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['xhdh'],2,5)

    def test02_销毁出库单据_查询_物品编号(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'xhdh':'','wpbh':'00000019070055701','start':'','end':'','ckr':''}
        self.xdw_xhckdj_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['wpbh'],3,5)

    def test03_销毁出库单据_查询_出库日期(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'xhdh':'','wpbh':'','start':'2019-07-22','end':'2019-07-22','ckr':''}
        self.xdw_xhckdj_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['start'],4,5)

    def test04_销毁出库单据_查询_组合查询(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'xhdh':'XH0000001907108','wpbh':'00000019070055701','start':'2019-07-22','end':'2019-07-22','ckr':''}
        self.xdw_xhckdj_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['xhdh'], 2, 5)
        self.pagination_num(search_num, search_value['wpbh'], 3, 5)
        self.pagination_num(search_num,search_value['start'],4,5)

if __name__ == '__main__':
    unittest.main()