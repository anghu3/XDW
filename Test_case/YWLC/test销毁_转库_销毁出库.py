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

    def test01_销毁_录单(self):
        self.Initialization_1()
        self.xdw_Inspection_addition(test_num, '销毁', '')
        global id, jld_id
        id = self.dr.find_element_by_xpath('//*[@id="list"]/tbody[1]/tr/td[3]').text
        jld_id = self.dr.find_element_by_xpath('//*[@id="jldbh"]').get_attribute('value')

    def test02_销毁_转库(self):
        self.Initialization_1()
        self.dr.find_element_by_xpath('//*[@id="f683e4f46b094a8ba68ad201a6e5b7bf"]/a/span').click()
        iframes = self.dr.find_element_by_xpath('//*[@id="sub_f683e4f46b094a8ba68ad201a6e5b7bf"]/iframe')
        self.dr.switch_to.frame(iframes)
        self.dr.find_element_by_xpath('//*[@id="wpbh"]').send_keys(id)
        self.dr.find_element_by_xpath('//*[@id="search"]/span').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/div/button').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="transferBtn"]').click()
        time.sleep(2)
        Select(self.dr.find_element_by_xpath('//*[@id="selCkid"]')).select_by_visible_text('仓库2')
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[5]/div[3]/div/button[2]').click()
        time.sleep(3)
        handles = self.dr.window_handles
        self.assertEqual(2,len(handles))

    def test03_销毁_转库单据查询(self):
        self.Initialization_1()
        self.dr.find_element_by_xpath('//*[@id="dcefdfba1ea04e2db15876bd8673651d"]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="047b073794584993be96d086e3b9b5cb"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_047b073794584993be96d086e3b9b5cb"]/iframe')
        self.dr.switch_to.frame(iframe)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/div[2]/input').send_keys(id)
        self.dr.find_element_by_xpath('//*[@id="search"]/span').click()
        self.assertEqual(id,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[2]').text)

    def test04_销毁_转库确认接收(self):
        self.Initialization_2()
        self.dr.find_element_by_xpath('//*[@id="436c1edb6d364195beb2ca044dceb58f"]/a').click()
        self.dr.find_element_by_xpath('//*[@id="d98aa4bffc93479b984febde6df22110"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_d98aa4bffc93479b984febde6df22110"]/iframe')
        self.dr.switch_to.frame(iframe)
        search_value = {'wpbh': id, 'wpmc': '', 'start': '', 'end': ''}
        self.xdw_Transfer_confirmation_receipt_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="tbList"]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['wpbh'], 2, 3)
        self.xdw_Transfer_confirmation_receipt()

    def test05_销毁_出库(self):
        self.Initialization_2()
        self.dr.find_element_by_xpath('//*[@id="436c1edb6d364195beb2ca044dceb58f"]/a').click()
        self.dr.find_element_by_xpath('//*[@id="6c25cddc87d7418fb9825b762737a2c0"]/a').click()
        iframes=self.dr.find_element_by_xpath('//*[@id="sub_6c25cddc87d7418fb9825b762737a2c0"]/iframe')
        self.dr.switch_to.frame(iframes)
        time.sleep(1)
        # js = "window.scrollTo(0, document.body.scrollHeight)"
        # self.dr.execute_script(js)
        # time.sleep(3)
        # self.dr.find_element_by_xpath(
        #     '/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[2]/span/button').click()
        # self.dr.find_element_by_xpath(
        #     '/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[2]/span/ul/li[1]/a').click()
        # time.sleep(1)
        search_value = {'wpbh': id, 'wpmc': '', 'startTime': '', 'endTime': '', 'clff': '--全部--', 'ckjglx': '--全部--'}
        self.xdw_ck_normal_search(search_value)
        search_num = self.dr.find_element_by_xpath(
            '/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['wpbh'], 2, 0)
        self.xdw_ck_normal_xhck()

    def test06_销毁单据(self):
        self.Initialization_2()
        self.dr.find_element_by_xpath('//*[@id="dcefdfba1ea04e2db15876bd8673651d"]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="2de3690e1692476caa343748aa27c5ec"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_2de3690e1692476caa343748aa27c5ec"]/iframe')
        self.dr.switch_to.frame(iframe)
        self.dr.find_element_by_xpath('//*[@id="form"]/div/div/div[2]/input').send_keys(id)
        self.dr.find_element_by_xpath('//*[@id="search"]/span').click()
        time.sleep(2)
        self.assertEqual(id,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]').text)

if __name__ == '__main__':
    unittest.main()