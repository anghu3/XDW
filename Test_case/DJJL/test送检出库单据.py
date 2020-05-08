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
        self.dr.find_element_by_xpath('//*[@id="572690ac226643d49731ea192e62b665"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_572690ac226643d49731ea192e62b665"]/iframe')
        self.dr.switch_to.frame(iframe)
        time.sleep(1)

    def test01_送检出库单据_查询_送检单号(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'sjdh':'SJ0000001907026','wpbh':'','start':'','end':'','ckr':''}
        self.xdw_sjckdj_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['sjdh'],1,0)

    def test02_送检出库单据_查询_物品编号(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'sjdh':'','wpbh':'00000019070043501','start':'','end':'','ckr':''}
        self.xdw_sjckdj_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['wpbh'],2,0)

    def test03_送检出库单据_查询_送检日期(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'sjdh':'','wpbh':'','start':'2019-07-19','end':'2019-07-19','ckr':''}
        self.xdw_sjckdj_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['start'],3,0)

    def test04_送检出库单据_查询_组合查询(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'sjdh':'SJ0000001907026','wpbh':'00000019070043501','start':'2019-07-19','end':'2019-07-19','ckr':''}
        self.xdw_sjckdj_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['sjdh'], 1, 0)
        self.pagination_num(search_num, search_value['wpbh'], 2, 0)
        self.pagination_num(search_num,search_value['start'],3,0)

if __name__ == '__main__':
    unittest.main()