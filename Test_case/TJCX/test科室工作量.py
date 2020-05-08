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
        self.dr.find_element_by_xpath('//*[@id="a4c952f3cacd43168bab3412e61931c5"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_a4c952f3cacd43168bab3412e61931c5"]/iframe')
        self.dr.switch_to.frame(iframe)
        time.sleep(2)

    def test01_科室工作量_查询_截获日期(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'kssj':now,'jssj':now,'wplb':{'wpdl':'','wpxl':''},'wpmc':'','jldbh':'','cllx':'--全部--','lyd':''}
        self.xdw_ksgzl_search(search_value)
        search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['kssj'],2,4)

    # def test02_科室工作量_查询_物品类别(self):
    #     self.login_keyuan(login_name_user1,login_name_password1)
    #     self.Initialization()
    #     search_value={'kssj':'','jssj':'','wplb':{'wpdl':1,'wpxl':6},'wpmc':'','jldbh':'','cllx':'--全部--','lyd':''}
    #     self.xdw_ksgzl_search(search_value)
    #     search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
    #     self.pagination_num(search_num,'奶及奶制品',4,4)

    def test03_科室工作量_查询_物品名称(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'kssj':'','jssj':'','wplb':{'wpdl':'','wpxl':''},'wpmc':'车厘子','jldbh':'','cllx':'--全部--','lyd':''}
        self.xdw_ksgzl_search(search_value)
        search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['wpmc'],5,4)

    def test04_科室工作量_查询_截留单号(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'kssj':'','jssj':'','wplb':{'wpdl':'','wpxl':''},'wpmc':'','jldbh':'000000190500341','cllx':'--全部--','lyd':''}
        self.xdw_ksgzl_search(search_value)
        search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['jldbh'],3,4)

    def test05_科室工作量_查询_处理方式(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        cllxs=['--全部--','销毁','退回','截留','放行','隔离检疫']
        for cllx in cllxs:
            if cllx=='--全部--':
                pass
            else:
                search_value={'kssj':'','jssj':'','wplb':{'wpdl':'','wpxl':''},'wpmc':'车厘子','jldbh':'','cllx':cllx,'lyd':''}
                self.xdw_ksgzl_search(search_value)
                search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
                self.pagination_num(search_num,search_value['cllx'],9,4)

    def test06_科室工作量_查询_来源地(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'kssj':'','jssj':'','wplb':{'wpdl':'','wpxl':''},'wpmc':'','jldbh':'','cllx':'--全部--','lyd':'澳大利亚'}
        self.xdw_ksgzl_search(search_value)
        search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['lyd'],6,4)

    def test07_科室工作量_查询_组合查询(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        self.Initialization()
        search_value = {'kssj': '2019-05-28', 'jssj': '2019-05-28', 'wplb': {'wpdl': '', 'wpxl': ''}, 'wpmc': '车厘子', 'jldbh': '000000190500341',
                        'cllx': '销毁', 'lyd': '澳大利亚'}
        self.xdw_ksgzl_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['kssj'], 2, 4)
        self.pagination_num(search_num, search_value['jldbh'], 3, 4)
        self.pagination_num(search_num, search_value['wpmc'], 5, 4)
        self.pagination_num(search_num, search_value['cllx'], 9, 4)
        self.pagination_num(search_num, search_value['lyd'], 6, 4)

    def test08_科室工作量_查询_导出(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        self.Initialization()
        search_value = {'kssj': '2019-05-28', 'jssj': '2019-05-28', 'wplb': {'wpdl': '', 'wpxl': ''}, 'wpmc': '车厘子', 'jldbh': '000000190500341',
                        'cllx': '销毁', 'lyd': '澳大利亚'}
        self.xdw_ksgzl_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['kssj'], 2, 4)
        self.pagination_num(search_num, search_value['jldbh'], 3, 4)
        self.pagination_num(search_num, search_value['wpmc'], 5, 4)
        self.pagination_num(search_num, search_value['cllx'], 9, 4)
        self.pagination_num(search_num, search_value['lyd'], 6, 4)
        self.xdw_ksgzl_exprot()

    def test09_科室工作量_查询_打印(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        self.Initialization()
        search_value = {'kssj': '2019-05-28', 'jssj': '2019-05-28', 'wplb': {'wpdl': '', 'wpxl': ''}, 'wpmc': '车厘子', 'jldbh': '000000190500341',
                        'cllx': '销毁', 'lyd': '澳大利亚'}
        self.xdw_ksgzl_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['kssj'], 2, 4)
        self.pagination_num(search_num, search_value['jldbh'], 3, 4)
        self.pagination_num(search_num, search_value['wpmc'], 5, 4)
        self.pagination_num(search_num, search_value['cllx'], 9, 4)
        self.pagination_num(search_num, search_value['lyd'], 6, 4)
        self.xdw_ksgzl_print()

if __name__ == '__main__':
    unittest.main()