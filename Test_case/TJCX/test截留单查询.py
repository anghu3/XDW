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
        self.dr.find_element_by_xpath('//*[@id="f8003af6a46c4cf7aa6e670bffb992a7"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_f8003af6a46c4cf7aa6e670bffb992a7"]/iframe')
        self.dr.switch_to.frame(iframe)
        time.sleep(2)

    def test01_截留单查询_查询_截留单编号(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'jldbh':'000000190700853','ysh':'','lkxm':'','zjhm':''}
        self.xdw_jldcx_search(search_value)
        search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['jldbh'],1,4)

    def test02_截留单查询_查询_印刷号(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'jldbh':'','ysh':'859674','lkxm':'','zjhm':''}
        self.xdw_jldcx_search(search_value)
        search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['ysh'],2,4)

    def test03_截留单查询_查询_旅客姓名(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'jldbh':'','ysh':'','lkxm':'赵金林','zjhm':''}
        self.xdw_jldcx_search(search_value)
        search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['lkxm'],3,4)

    def test04_截留单查询_查询_证件号码(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'jldbh':'','ysh':'','lkxm':'','zjhm':'753951'}
        self.xdw_jldcx_search(search_value)
        search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['zjhm'],4,4)

    def test05_截留单查询_查询_组合查询(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'jldbh':'000000190700853','ysh':'859674','lkxm':'赵金林','zjhm':'753951'}
        self.xdw_jldcx_search(search_value)
        search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['jldbh'], 1, 4)
        self.pagination_num(search_num, search_value['ysh'], 2, 4)
        self.pagination_num(search_num, search_value['lkxm'], 3, 4)
        self.pagination_num(search_num,search_value['zjhm'],4,4)

    def test06_截留单查询_查看(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        self.Initialization()
        search_value = {'jldbh': '000000190700853', 'ysh': '859674', 'lkxm': '赵金林', 'zjhm': '753951'}
        self.xdw_jldcx_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['jldbh'], 1, 4)
        self.pagination_num(search_num, search_value['ysh'], 2, 4)
        self.pagination_num(search_num, search_value['lkxm'], 3, 4)
        self.pagination_num(search_num, search_value['zjhm'], 4, 4)
        self.xdw_jldcx_details()
        self.assertEqual(search_value['jldbh'],self.dr.find_element_by_xpath('//*[@id="dialog-edit"]/div[2]/div[2]').text)
        self.assertEqual(search_value['lkxm'],self.dr.find_element_by_xpath('//*[@id="dialog-edit"]/div[2]/div[3]').text)
        self.assertEqual(search_value['zjhm'],self.dr.find_element_by_xpath('//*[@id="dialog-edit"]/div[2]/div[4]').text)


if __name__ == '__main__':
    unittest.main()