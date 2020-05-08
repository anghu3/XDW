from Setting.setting_file import xdw_TestCase
from Setting.cycl import cycl_TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from Setting.setting_file import login_name_user1,login_name_password1,login_name_user4,login_name_password4,setting_xls
from Setting.menu import data
import xlrd
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class xdw_TestCase(xdw_TestCase,cycl_TestCase):

    global now
    now = time.strftime("%Y-%m-%d", time.localtime(time.time()))

    def Initialization(self):
        self.dr.switch_to.default_content()
        self.dr.find_element_by_xpath('//*[@id="'+data['送样结果录入']+'"]').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_'+data['送样结果录入']+'"]/iframe')
        self.dr.switch_to.frame(iframe)
        time.sleep(1)

    def test01_送样结果录入_查询_物品编号(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'00000019110001001','mc':'','start':'','end':'','zt':'--全部--'}
        self.xdw_Sampling_result_input_search(search_value)
        search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['wpbh'],2,4)

    def test02_送样结果录入_查询_物品名称(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'','mc':'石榴','start':'','end':'','zt':'--全部--'}
        self.xdw_Sampling_result_input_search(search_value)
        search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['mc'],3,4)

    def test03_送样结果录入_查询_送样时间开始(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'','mc':'','start':'2019-07-01','end':'','zt':'--全部--'}
        self.xdw_Sampling_result_input_search(search_value)

    def test04_送样结果录入_查询_送样时间结束(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'','mc':'','start':'2019-07-01','end':now,'zt':'--全部--'}
        self.xdw_Sampling_result_input_search(search_value)

    def test05_送样结果录入_查询_录入状态(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        zts=['--全部--','未录入','已录入']
        for zt in zts:
            if zt=='--全部--':
                pass
            else:
                search_value={'wpbh':'','mc':'','start':'','end':'','zt':zt}
                self.xdw_Sampling_result_input_search(search_value)
                search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
                self.pagination_num(search_num,search_value['zt'],9,4)

if __name__ == '__main__':
    unittest.main()