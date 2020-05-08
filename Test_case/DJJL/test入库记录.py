from Setting.setting_file import xdw_TestCase
from Setting.cycl import cycl_TestCase
import unittest
import time
from Setting.setting_file import login_name_user1,login_name_password1,login_name_user4,login_name_password4,setting_xls
import random


class xdwcy_TestCase(xdw_TestCase,cycl_TestCase):

    def Initialization(self):
        self.dr.find_element_by_xpath('//*[@id="dcefdfba1ea04e2db15876bd8673651d"]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="9de9b44301aa4dba960c5057eeb31404"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_9de9b44301aa4dba960c5057eeb31404"]/iframe')
        self.dr.switch_to.frame(iframe)
        time.sleep(1)

    def test01_入库记录_查询_物品编号(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'00000019070076301','wpmc':'','startTime':'','endTime':''}
        self.xdw_rkjl_search(search_value)
        search_nunm=self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_nunm,search_value['wpbh'],1,7)

    def test02_入库记录_查询_物品名称(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'','wpmc':'香肠','startTime':'','endTime':''}
        self.xdw_rkjl_search(search_value)
        search_nunm=self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_nunm,search_value['wpmc'],2,7)

    def test03_入库记录_查询_入库日期(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'','wpmc':'','startTime':'2019-07-25','endTime':'2019-07-25'}
        self.xdw_rkjl_search(search_value)
        search_nunm=self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_nunm,search_value['startTime'],5,7)

    def test04_入库记录_查询_组合查询(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'00000019070076301','wpmc':'香肠','startTime':'2019-07-25','endTime':'2019-07-25'}
        self.xdw_rkjl_search(search_value)
        search_nunm=self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_nunm, search_value['wpbh'], 1, 7)
        self.pagination_num(search_nunm, search_value['wpmc'], 2, 7)
        self.pagination_num(search_nunm,search_value['startTime'],5,7)

    def test05_入库记录_查询_导出(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'00000019070076301','wpmc':'香肠','startTime':'2019-07-25','endTime':'2019-07-25'}
        self.xdw_rkjl_search(search_value)
        search_nunm=self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_nunm, search_value['wpbh'], 1, 7)
        self.pagination_num(search_nunm, search_value['wpmc'], 2, 7)
        self.pagination_num(search_nunm,search_value['startTime'],5,7)
        self.xdw_rkjl_export()

if __name__ == '__main__':
    unittest.main()