from Setting.setting_file import xdw_TestCase
from Setting.cycl import cycl_TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from Setting.setting_file import login_name_user1,login_name_password1,login_name_user4,login_name_password4,setting_xls
import xlrd
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

Testdata = xlrd.open_workbook(setting_xls)
sheet_passenger=Testdata.sheet_by_name('旅客信息')
sheet_goods=Testdata.sheet_by_name('物品信息')

class xdwcy_TestCase(xdw_TestCase,cycl_TestCase):
    global test_num
    test_num = random.randint(1, 10)

    def Initialization_1(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        time.sleep(2)

    def Initialization_2(self):
        self.login_keyuan(login_name_user4, login_name_password4)
        time.sleep(2)

    def test01_实验室检疫_录单(self):
        self.Initialization_1()
        self.xdw_Inspection_addition(test_num, '截留', '补办手续')
        global id, jld_id
        id = self.dr.find_element_by_xpath('//*[@id="list"]/tbody[1]/tr/td[3]').text
        jld_id = self.dr.find_element_by_xpath('//*[@id="jldbh"]').get_attribute('value')

    def test02_截留物处理查询(self):
        self.Initialization_1()
        self.dr.find_element_by_xpath('//*[@id="88f0f33abf2d48419438a72637c27b49"]/a').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_88f0f33abf2d48419438a72637c27b49"]/iframe')
        self.dr.switch_to.frame(iframe)
        self.dr.find_element_by_xpath('//*[@id="form"]/div/div[2]/input').send_keys(id)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(2)
        self.assertEqual(id,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[1]').text)
        self.assertIsNotNone(self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[9]/div/button'))

    def test03_补办手续_入库(self):
        self.Initialization_1()
        self.dr.find_element_by_xpath('//*[@id="f683e4f46b094a8ba68ad201a6e5b7bf"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_f683e4f46b094a8ba68ad201a6e5b7bf"]/iframe')
        self.dr.switch_to.frame(iframe)
        self.dr.find_element_by_xpath('//*[@id="wpbh"]').send_keys(id)
        self.dr.find_element_by_xpath('//*[@id="search"]/span').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/div/button').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('//*[@id="'
                                      'inStorageBtn"]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[6]/div[3]/div/button[2]').click()
        time.sleep(3)
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text)

    def test04_补办手续_移交法制部门(self):
        self.Initialization_1()
        self.dr.find_element_by_xpath('//*[@id="88f0f33abf2d48419438a72637c27b49"]/a').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_88f0f33abf2d48419438a72637c27b49"]/iframe')
        self.dr.switch_to.frame(iframe)
        self.dr.find_element_by_xpath('//*[@id="form"]/div/div[2]/input').send_keys(id)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(2)
        self.assertEqual(id,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[1]').text)
        self.assertIsNotNone(self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[9]/div/button'))
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]/div/button').click()
        time.sleep(2)
        self.assertEqual(id,self.dr.find_element_by_xpath('//*[@id="wpmc"]').get_attribute('value'))
        Select(self.dr.find_element_by_xpath('//*[@id="jlcljg"]')).select_by_visible_text('移交法制部门')
        # Select(self.dr.find_element_by_xpath('//*[@id="jlwpjg"]')).select_by_visible_text('放行')
        time.sleep(1)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]').click()
        time.sleep(3)
        self.assertEqual('没有找到匹配的记录',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text)

    def test05_补办手续_移交法制部门_查询(self):
        self.Initialization_1()
        self.dr.find_element_by_xpath('//*[@id="8ca11cb733f843e8a4c63f8b579da538"]/a').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_8ca11cb733f843e8a4c63f8b579da538"]/iframe')
        self.dr.switch_to.frame(iframe)
        self.dr.find_element_by_xpath('//*[@id="form"]/div/div[2]/input').send_keys(jld_id)
        self.assertEqual(jld_id,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[1]').text)
        self.assertIsNotNone(self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[13]/div/button'))

if __name__ == '__main__':
    unittest.main()