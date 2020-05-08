from Setting.setting_file import xdw_TestCase
from Setting.cycl import cycl_TestCase
import unittest
import time
from Setting.setting_file import login_name_user1,login_name_password1,login_name_user4,login_name_password4,setting_xls
import random


class xdwcy_TestCase(xdw_TestCase,cycl_TestCase):
    a=1

    def Initialization(self):
        self.dr.find_element_by_xpath('//*[@id="dcefdfba1ea04e2db15876bd8673651d"]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="758f1d8d5cb34a5f9873e07ce5c5fb59"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_758f1d8d5cb34a5f9873e07ce5c5fb59"]/iframe')
        self.dr.switch_to.frame(iframe)
        time.sleep(1)

    def test01_移交保护部门出库单据_查询_移交单号(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'yjdh':'ZJ0000001907053','wpbh':'','start':'','end':'','ckr':''}
        self.xdw_yjbhbm_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['yjdh'],1,0)

    def test02_移交保护部门出库单据_查询_物品编号(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'yjdh':'','wpbh':'00000019070073001','start':'','end':'','ckr':''}
        self.xdw_yjbhbm_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['wpbh'],2,0)

    def test03_移交保护部门出库单据_查询_送检日期(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'yjdh':'','wpbh':'','start':'2019-07-25','end':'2019-07-25','ckr':''}
        self.xdw_yjbhbm_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['start'],7,0)

    def test04_移交保护部门出库单据_查询_组合查询(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'yjdh':'ZJ0000001907053','wpbh':'00000019070073001','start':'2019-07-25','end':'2019-07-25','ckr':''}
        self.xdw_yjbhbm_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['yjdh'], 1, 0)
        self.pagination_num(search_num, search_value['wpbh'], 2, 0)
        self.pagination_num(search_num,search_value['start'],7,0)

if __name__ == '__main__':
    unittest.main()