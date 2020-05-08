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

Testdata = xlrd.open_workbook(setting_xls)
sheet_passenger=Testdata.sheet_by_name('旅客信息')
sheet_goods=Testdata.sheet_by_name('物品信息')

class xdw_TestCase(xdw_TestCase,cycl_TestCase):

    global now
    now = time.strftime("%Y-%m-%d", time.localtime(time.time()))

    def Initialization(self):
        self.dr.find_element_by_xpath('//*[@id="'+data['异常单据处理']+'"]').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_'+data['异常单据处理']+'"]/iframe')
        self.dr.switch_to.frame(iframe)
        self.dr.implicitly_wait(3)

    def test01_异常单据处理_查询_截留单号(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'Jldbh':'000000191100013','Wpmc':'','startTime':'','endTime':'','shzt':'全部'}
        self.xdw_Abnormal_Document_Processing_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['Jldbh'],1,2)

    def test02_异常单据处理_查询_物品名称(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'Jldbh':'','Wpmc':'香蕉','startTime':'2019-11-01','endTime':'','shzt':'全部'}
        self.xdw_Abnormal_Document_Processing_search(search_value)
        search_num = self.dr.find_element_by_xpath(
            '/html/body/div[1]/div/div[3]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['Wpmc'], 6, 2)

    def test03_异常单据处理_查询_录入时间开始(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'Jldbh':'','Wpmc':'','startTime':'2019-11-11','endTime':'2019-11-11','shzt':'全部'}
        self.xdw_Abnormal_Document_Processing_search(search_value)
        search_num = self.dr.find_element_by_xpath(
            '/html/body/div[1]/div/div[3]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['startTime'], 10, 2)

    def test04_异常单据处理_查询_录入时间结束(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'Jldbh':'','Wpmc':'','startTime':'2019-11-11','endTime':'2019-11-11','shzt':'全部'}
        self.xdw_Abnormal_Document_Processing_search(search_value)
        search_num = self.dr.find_element_by_xpath(
            '/html/body/div[1]/div/div[3]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['endTime'], 10, 2)

    def test05_异常单据处理_查询_审核状态(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'Jldbh':'','Wpmc':'','startTime':'2019-11-11','endTime':'2019-11-11','shzt':'未审核'}
        self.xdw_Abnormal_Document_Processing_search(search_value)
        search_num = self.dr.find_element_by_xpath(
            '/html/body/div[1]/div/div[3]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['shzt'], 9, 2)

    def test06_异常单据处理_查询_组合查询(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'Jldbh':'000000191100013','Wpmc':'香蕉','startTime':'2019-11-11','endTime':'2019-11-11','shzt':'未审核'}
        self.xdw_Abnormal_Document_Processing_search(search_value)
        search_num = self.dr.find_element_by_xpath(
            '/html/body/div[1]/div/div[3]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['Jldbh'], 1, 2)
        self.pagination_num(search_num, search_value['Wpmc'], 6, 2)
        self.pagination_num(search_num, search_value['shzt'], 9, 2)


if __name__ == '__main__':
    unittest.main()