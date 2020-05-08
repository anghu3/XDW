from Setting.setting_file import xdw_TestCase
from Setting.cycl import cycl_TestCase
import unittest
import time
from Setting.setting_file import login_name_user1,login_name_password1,login_name_user4,login_name_password4,setting_xls
import random


class xdwcy_TestCase(xdw_TestCase,cycl_TestCase):

    def Initialization(self):
        self.dr.find_element_by_xpath('//*[@id="436c1edb6d364195beb2ca044dceb58f"]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="c41ac273606c43a9beaf3eebd4c86887"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_c41ac273606c43a9beaf3eebd4c86887"]/iframe')
        self.dr.switch_to.frame(iframe)
        time.sleep(1)


    def test01_退回_查询_物品编号(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'00000019070044901','wpmc':'','startTime':'','endTime':''}
        self.xdw_return_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['wpbh'],1,0)

    def test02_退回_查询_物品名称(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'','wpmc':'酸奶','startTime':'','endTime':''}
        self.xdw_return_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['wpmc'],2,0)

    def test03_退回_查询_截获日期(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'','wpmc':'','startTime':'2019-07-19','endTime':'2019-07-19'}
        self.xdw_return_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['startTime'],4,0)

    def test04_退回_查询_组合查询(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'00000019070044901','wpmc':'酸奶','startTime':'2019-07-19','endTime':'2019-07-19'}
        self.xdw_return_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['wpbh'], 1, 0)
        self.pagination_num(search_num, search_value['wpmc'], 2, 0)
        self.pagination_num(search_num,search_value['startTime'],4,0)

if __name__ == '__main__':
    unittest.main()