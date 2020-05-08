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
        self.dr.find_element_by_xpath('//*[@id="dcefdfba1ea04e2db15876bd8673651d"]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="a5c5e173f18c4d0280bbfbf91b325b28"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_a5c5e173f18c4d0280bbfbf91b325b28"]/iframe')
        self.dr.switch_to.frame(iframe)
        time.sleep(1)

    def test01_隔离检疫记录_查询_物品编号(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value = {'jldh': '000000190700785', 'zjh': '', 'wpmc': ''}
        self.xdw_xcthjl_search(search_value)
        search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['jldh'],1,4)

    def test02_隔离检疫记录_查询_证件号(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value = {'jldh': '', 'zjh': '524152', 'wpmc': ''}
        self.xdw_xcthjl_search(search_value)
        search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['zjh'],4,4)

    def test03_隔离检疫记录_查询_物品名称(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value = {'jldh': '', 'zjh': '', 'wpmc': '香蕉'}
        self.xdw_xcthjl_search(search_value)
        search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['wpmc'],5,4)

    def test04_隔离检疫记录_查询_组合查询(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value = {'jldh': '000000190700785', 'zjh': '524152', 'wpmc': '香蕉'}
        self.xdw_xcthjl_search(search_value)
        search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['jldh'], 1, 4)
        self.pagination_num(search_num, search_value['zjh'], 4, 4)
        self.pagination_num(search_num,search_value['wpmc'],5,4)

    def test05_隔离检疫记录_查看(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        self.Initialization()
        search_value = {'jldh': '000000190700785', 'zjh': '524152', 'wpmc': '香蕉'}
        self.xdw_xcthjl_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['jldh'], 1, 4)
        self.pagination_num(search_num, search_value['zjh'], 4, 4)
        self.pagination_num(search_num, search_value['wpmc'], 5, 4)
        self.xdw_xcthjl_details(search_value['jldh'])

    def test06_隔离检疫记录_导出(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        self.Initialization()
        search_value = {'jldh': '000000190700785', 'zjh': '524152', 'wpmc': '香蕉'}
        self.xdw_xcthjl_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['jldh'], 1, 4)
        self.pagination_num(search_num, search_value['zjh'], 4, 4)
        self.pagination_num(search_num, search_value['wpmc'], 5, 4)
        self.xdw_xcthjl_export()

if __name__ == '__main__':
    unittest.main()