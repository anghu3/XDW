from Setting.setting_file import xdw_TestCase
from Setting.cycl import cycl_TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from Setting.setting_file import login_name_user1,login_name_password1,login_name_user2,login_name_password2,setting_xls
import random
import xlrd

Testdata = xlrd.open_workbook(setting_xls)
sheet_passenger=Testdata.sheet_by_name('旅客信息')
sheet_goods=Testdata.sheet_by_name('物品信息')

class xdw_TestCase(xdw_TestCase,cycl_TestCase):

    global now
    now = time.strftime("%Y-%m-%d", time.localtime(time.time()))

    def Initialization(self):
        self.dr.switch_to.default_content()
        self.dr.find_element_by_xpath('//*[@id="b08e88dd0b16404cabbbe73e40028c6f"]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="a4b959bb2049488394994e4aca722eb7"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_a4b959bb2049488394994e4aca722eb7"]/iframe')
        self.dr.switch_to.frame(iframe)
        time.sleep(2)

    def test01_旅客记录查询_新增(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.xdw_Inspection_addition(11, '销毁', '')

    def test02_旅客记录查询_查询_旅客姓名(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'lkxm':sheet_passenger.col_values(11,1,2)[0],'zjh':'','startTime':'','endTime':''}
        self.xdw_lkjlcx_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['lkxm'],2,7)

    def test03_旅客记录查询_查询_证件号码(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'lkxm':'','zjh':sheet_passenger.col_values(11,7,8)[0],'startTime':'','endTime':''}
        self.xdw_lkjlcx_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['zjh'],3,7)

    def test04_旅客记录查询_查询_时间(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'lkxm':'','zjh':'','startTime':'2019-07-01','endTime':now}
        self.xdw_lkjlcx_search(search_value)

    def test05_旅客记录查询_查询_组合查询(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'lkxm':sheet_passenger.col_values(11,1,2)[0],'zjh':sheet_passenger.col_values(11,7,8)[0],'startTime':now,'endTime':now}
        self.xdw_lkjlcx_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['lkxm'], 2, 7)
        self.pagination_num(search_num,search_value['zjh'],3,7)

    def test06_旅客记录查询_删除(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        self.Initialization()
        search_value = {'lkxm': sheet_passenger.col_values(11, 1, 2)[0], 'zjh': sheet_passenger.col_values(11, 7, 8)[0],
                        'startTime': now, 'endTime': now}
        self.xdw_lkjlcx_search(search_value)
        search_num = self.dr.find_element_by_xpath(
            '/html/body/div[1]/div/div[3]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['lkxm'], 2, 7)
        self.pagination_num(search_num, search_value['zjh'], 3, 7)
        self.xdw_lkjlcx_delete()

    def test07_旅客记录查询_批量删除(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        self.xdw_Inspection_addition(11, '销毁', '')
        self.Initialization()
        search_value = {'lkxm': sheet_passenger.col_values(11, 1, 2)[0], 'zjh': sheet_passenger.col_values(11, 7, 8)[0],
                        'startTime': now, 'endTime': now}
        self.xdw_lkjlcx_search(search_value)
        search_num = self.dr.find_element_by_xpath(
            '/html/body/div[1]/div/div[3]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['lkxm'], 2, 7)
        self.pagination_num(search_num, search_value['zjh'], 3, 7)
        self.xdw_lkjlcx_Batch_deletion()



if __name__ == '__main__':
    unittest.main()