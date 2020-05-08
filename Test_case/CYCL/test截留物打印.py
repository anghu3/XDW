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
        self.dr.find_element_by_xpath('//*[@id="'+data['截留物打印']+'"]').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_'+data['截留物打印']+'"]/iframe')
        self.dr.switch_to.frame(iframe)

    def test01_截留物打印_查询_截留单编号(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search = {'jldbh': '000000191100011', 'wpmc': '', 'startTime': '2019-11-01', 'endTime': now, 'dyzt': '全部', 'ysbh': ''}
        self.xdw_Print_search(search)
        search_num = self.dr.find_element_by_xpath(
            '/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search['jldbh'], 2,0)

    def test02_截留物打印_查询_名称(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        self.Initialization()
        search = {'jldbh': '', 'wpmc': '燕窝', 'startTime': '2019-11-01', 'endTime':now, 'dyzt': '全部', 'ysbh': ''}
        # column={'jldbh':2 , 'wpmc': 3, 'startTime': '', 'endTime': '', 'dyzt': 9, 'ysbh': 8}
        self.xdw_Print_search(search)
        search_num = self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search['wpmc'],3,0)

    def test03_截留物打印_查询_结果日期_开始(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        self.Initialization()
        search = {'jldbh': '', 'wpmc': '', 'startTime': now, 'endTime': '', 'dyzt': '全部', 'ysbh': ''}
        self.xdw_Print_search(search)

    def test04_截留物打印_查询_截获日期_结束(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        self.Initialization()
        search = {'jldbh': '', 'wpmc': '', 'startTime': '', 'endTime': now, 'dyzt': '全部', 'ysbh': ''}
        self.xdw_Print_search(search)

    def test05_截留物打印_查询_状态_已打印(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        self.Initialization()
        search = {'jldbh': '', 'wpmc': '', 'startTime': '2019-11-12', 'endTime': now, 'dyzt': '已打印', 'ysbh': ''}
        self.xdw_Print_search(search)
        search_num = self.dr.find_element_by_xpath(
            '/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search['dyzt'], 9,0)

    def test06_截留物打印_查询_状态_未打印(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        self.Initialization()
        search = {'jldbh': '', 'wpmc': '', 'startTime': '2019-11-12', 'endTime': now, 'dyzt': '未打印', 'ysbh': ''}
        self.xdw_Print_search(search)
        # search_num = self.dr.find_element_by_xpath(
        #     '/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        # self.pagination_num(search_num, search['dyzt'], 9)

    def test07_截留物打印_查询_印刷号(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        self.Initialization()
        search = {'jldbh': '', 'wpmc': '', 'startTime': '2019-11-12', 'endTime': now, 'dyzt': '全部', 'ysbh': '456'}
        self.xdw_Print_search(search)
        search_num = self.dr.find_element_by_xpath(
            '/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search['ysbh'], 8,0)

    def test08_截留物打印_查询_全部条件组合(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        self.Initialization()
        search = {'jldbh': '000000191100026', 'wpmc': '石榴', 'startTime': '2019-11-01', 'endTime': now, 'dyzt': '已打印', 'ysbh': '456'}
        self.xdw_Print_search(search)
        search_num = self.dr.find_element_by_xpath(
            '/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search['jldbh'], 2,0)
        self.pagination_num(search_num, search['wpmc'], 3,0)
        self.pagination_num(search_num, search['dyzt'], 9,0)
        self.pagination_num(search_num, search['ysbh'], 8,0)

if __name__ == '__main__':
    unittest.main()