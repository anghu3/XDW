from Setting.setting_file import xdw_TestCase
from Setting.cycl import cycl_TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from Setting.setting_file import login_name_user1,login_name_password1,login_name_user4,login_name_password4,setting_xls,findnum
from Setting.menu import data
import xlrd
import random

Testdata = xlrd.open_workbook(setting_xls)
sheet_passenger=Testdata.sheet_by_name('旅客信息')
sheet_goods=Testdata.sheet_by_name('物品信息')

class xdw_TestCase(xdw_TestCase,cycl_TestCase):

    global now
    now = time.strftime("%Y-%m-%d", time.localtime(time.time()))

    def Initialization(self):
        self.dr.find_element_by_xpath('//*[@id="'+data['现场转库或入库']+'"]').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_'+data['现场转库或入库']+'"]/iframe')
        self.dr.switch_to.frame(iframe)
        self.dr.implicitly_wait(3)

    def test01_现场转库或入库_查询_截获开始日期(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        self.Initialization()
        search_value={'startTime':now,'endTime':'','wpbh':'','wpmc':'香蕉','wplb':'--全部--','clff':'--全部--'}
        self.xdw_Onsite_transfer_or_storage_search(search_value)
        search_num=self.dr.find_element_by_xpath('//*[@id="3lists"]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,str(search_value['startTime']),9,1)
        ##导出功能
        # self.xdw_Onsite_transfer_or_storage_export()


    def test02_现场转库或入库_查询_截获结束日期(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        self.Initialization()
        search_value = {'startTime': now, 'endTime': now, 'wpbh': '', 'wpmc': '香蕉', 'wplb': '--全部--', 'clff': '--全部--'}
        self.xdw_Onsite_transfer_or_storage_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="3lists"]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, str(search_value['endTime']), 9,1)
        ##导出功能
        # self.xdw_Onsite_transfer_or_storage_export()

    def test03_现场转库或入库_查询_物品编号(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        self.Initialization()
        search_value = {'startTime': '', 'endTime': '', 'wpbh': '00000019110005501', 'wpmc': '香蕉', 'wplb': '--全部--', 'clff': '--全部--'}
        self.xdw_Onsite_transfer_or_storage_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="3lists"]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, str(search_value['wpbh']), 2,1)
        ##导出功能
        # self.xdw_Onsite_transfer_or_storage_export()

    def test04_现场转库或入库_查询_物品名称(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        self.Initialization()
        search_value = {'startTime': '2019-11-01', 'endTime': '', 'wpbh': '', 'wpmc': '	香蕉', 'wplb': '--全部--', 'clff': '--全部--'}
        self.xdw_Onsite_transfer_or_storage_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="3lists"]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, str(search_value['wpmc']), 3,1)
        ##导出功能
        # self.xdw_Onsite_transfer_or_storage_export()

    def test05_现场转库或入库_查询_分类(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        self.Initialization()
        search_value = {'startTime': now, 'endTime': now, 'wpbh': '', 'wpmc': '', 'wplb': '新鲜水果', 'clff': '--全部--'}
        self.xdw_Onsite_transfer_or_storage_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="3lists"]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, str(search_value['wplb']), 5,1)
        ##导出功能
        # self.xdw_Onsite_transfer_or_storage_export()

    def test06_现场转库或入库_查询_截获方法(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        self.Initialization()
        search_value = {'startTime': now, 'endTime': now, 'wpbh': '', 'wpmc': '香蕉', 'wplb': '--全部--', 'clff': '风险评估截留'}
        self.xdw_Onsite_transfer_or_storage_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="3lists"]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, str(search_value['clff']), 7,1)
        ##导出功能
        # self.xdw_Onsite_transfer_or_storage_export()

    def test07_现场转库或入库_查询_组合查询(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        self.Initialization()
        search_value = {'startTime': '', 'endTime': '', 'wpbh': '00000019110005501', 'wpmc': '香蕉', 'wplb': '新鲜水果', 'clff': '风险评估截留'}
        self.xdw_Onsite_transfer_or_storage_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="3lists"]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        # self.pagination_num(search_num, str(search_value['startTime']), 9)
        # self.pagination_num(search_num, str(search_value['endTime']), 9)
        self.pagination_num(search_num, str(search_value['wpbh']), 2,1)
        self.pagination_num(search_num, str(search_value['wpmc']), 3,1)
        self.pagination_num(search_num, str(search_value['wplb']), 5,1)
        self.pagination_num(search_num, str(search_value['clff']), 7,1)
        ##导出功能
        # self.xdw_Onsite_transfer_or_storage_export()

    # def test08_现场转库或入库_入库(self):
    #     self.login_keyuan(login_name_user1,login_name_password1)
    #     self.xdw_Inspection_addition(random.randint(1, 10),'销毁','')
    #     id = self.dr.find_element_by_xpath('//*[@id="list"]/tbody[1]/tr/td[3]').text
    #     jld_id = self.dr.find_element_by_xpath('//*[@id="jldbh"]').get_attribute('value')
    #     self.dr.switch_to_default_content()
    #     self.Initialization()
    #     search_value = {'startTime': '', 'endTime': '', 'wpbh': id, 'wpmc': '', 'wplb': '--全部--', 'clff': '--全部--'}
    #     self.xdw_Onsite_transfer_or_storage_search(search_value)
    #     search_num = self.dr.find_element_by_xpath('//*[@id="3lists"]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
    #     self.pagination_num(search_num,search_value['wpbh'],2,1)
    #     self.xdw_Onsite_transfer_or_storage_print()
    #     self.xdw_Onsite_transfer_or_storage_storage()

    # def test09_现场转库或入库_转库(self):
    #     self.login_keyuan(login_name_user1,login_name_password1)
    #     self.xdw_Inspection_addition(random.randint(1, 10), '销毁', '')
    #     id = self.dr.find_element_by_xpath('//*[@id="list"]/tbody[1]/tr/td[3]').text
    #     jld_id = self.dr.find_element_by_xpath('//*[@id="jldbh"]').get_attribute('value')
    #     self.dr.switch_to.default_content()
    #     self.Initialization()
    #     search_value = {'startTime': '', 'endTime': '', 'wpbh': id, 'wpmc': '', 'wplb': '--全部--', 'clff': '--全部--'}
    #     self.xdw_Onsite_transfer_or_storage_search(search_value)
    #     search_num = self.dr.find_element_by_xpath('//*[@id="3lists"]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
    #     self.pagination_num(search_num, search_value['wpbh'], 2,1)
    #     self.xdw_Onsite_transfer_or_storage_print()
    #     self.xdw_Onsite_transfer_or_storage_transfer()


if __name__ == '__main__':
    unittest.main()