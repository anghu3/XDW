from Setting.setting_file import xdw_TestCase
from Setting.cycl import cycl_TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from Setting.setting_file import login_name_user1,login_name_password1,login_name_user2,login_name_password2,setting_xls
import random

class xdw_TestCase(xdw_TestCase,cycl_TestCase):

    global now
    now = time.strftime("%Y-%m-%d", time.localtime(time.time()))

    def Initialization(self):
        self.dr.switch_to.default_content()
        self.dr.find_element_by_xpath('//*[@id="b08e88dd0b16404cabbbe73e40028c6f"]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="82970a3a28da49a88dc842b9202e8d2e"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_82970a3a28da49a88dc842b9202e8d2e"]/iframe')
        self.dr.switch_to.frame(iframe)
        time.sleep(5)

    def test01_截留物查询_查询_物品编号(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value = {'wpbh': '00000019070085101', 'wpmc': '', 'wplb': {'wpdl': '', 'wpxl': ''}, 'cllx': '--全部--',
                        'kssj': '', 'jssj': '', 'zjh': ''}
        self.xdw_jlwcy_search(search_value)
        search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['wpbh'],1,4)

    def test02_截留物查询_查询_物品名称(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value = {'wpbh': '', 'wpmc': '牛奶', 'wplb': {'wpdl': '', 'wpxl': ''}, 'cllx': '--全部--', 'kssj': '',
                        'jssj': '', 'zjh': ''}
        self.xdw_jlwcy_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['wpmc'], 2, 4)

    def test03_截留物查询_查询_物品类别(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value = {'wpbh': '', 'wpmc': '', 'wplb': {'wpdl': 1, 'wpxl': 6}, 'cllx': '--全部--', 'kssj': '2019-07-25',
                        'jssj': '2019-07-25', 'zjh': ''}
        self.xdw_jlwcy_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,'奶及奶制品', 4, 4)

    def test04_截留物查询_查询_处理方式(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        cllxs=['--全部--','销毁','退回','截留','放行','隔离检疫']
        for cllx in cllxs:
            if cllx=='--全部--':
                pass
            else:
                search_value={'wpbh':'','wpmc':'牛奶','wplb':{'wpdl':'','wpxl':''},'cllx':cllx,'kssj':'','jssj':'','zjh':''}
                self.xdw_jlwcy_search(search_value)
                search_num = self.dr.find_element_by_xpath(
                    '//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
                self.pagination_num(search_num, search_value['cllx'], 11, 4)

    def test05_截留物查询_查询_截获日期(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value = {'wpbh': '', 'wpmc': '', 'wplb': {'wpdl': '', 'wpxl': ''}, 'cllx': '--全部--', 'kssj': '2019-07-25',
                        'jssj': '2019-07-25', 'zjh': ''}
        self.xdw_jlwcy_search(search_value)
        search_num = self.dr.find_element_by_xpath(
            '//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['kssj'], 3, 4)

    def test06_截留物查询_查询_证件号(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value = {'wpbh': '', 'wpmc': '', 'wplb': {'wpdl': '', 'wpxl': ''}, 'cllx': '--全部--', 'kssj': '2019-07-01',
                        'jssj': now, 'zjh': '157874'}
        self.xdw_jlwcy_search(search_value)
        search_num = self.dr.find_element_by_xpath(
            '//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['zjh'], 8, 4)

    def test07_截留物查询_查询_组合查询(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value = {'wpbh': '00000019070085101', 'wpmc': '牛奶', 'wplb': {'wpdl': '1', 'wpxl': '6'}, 'cllx': '销毁', 'kssj': '2019-07-01',
                        'jssj': now, 'zjh': '157874'}
        self.xdw_jlwcy_search(search_value)
        search_num = self.dr.find_element_by_xpath(
            '//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['wpbh'], 1, 4)
        self.pagination_num(search_num, search_value['wpmc'], 2, 4)
        self.pagination_num(search_num, '奶及奶制品', 4, 4)
        self.pagination_num(search_num, search_value['cllx'], 11, 4)
        self.pagination_num(search_num, search_value['zjh'], 8, 4)

    def test08_截留物查询_导出(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value = {'wpbh': '00000019070085101', 'wpmc': '牛奶', 'wplb': {'wpdl': '1', 'wpxl': '6'}, 'cllx': '销毁', 'kssj': '2019-07-01',
                        'jssj': now, 'zjh': '157874'}
        self.xdw_jlwcy_search(search_value)
        search_num = self.dr.find_element_by_xpath(
            '//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['wpbh'], 1, 4)
        self.pagination_num(search_num, search_value['wpmc'], 2, 4)
        self.pagination_num(search_num, '奶及奶制品', 4, 4)
        self.pagination_num(search_num, search_value['cllx'], 11, 4)
        self.pagination_num(search_num, search_value['zjh'], 8, 4)
        self.xdw_jlwcy_export()

if __name__ == '__main__':
    unittest.main()