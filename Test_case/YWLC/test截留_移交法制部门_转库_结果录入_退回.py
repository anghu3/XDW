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

    global now
    now = time.strftime("%Y-%m-%d", time.localtime(time.time()))

    def test01_实验室检疫_录单(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        test_num = random.randint(1, 10)
        self.xdw_Inspection_addition(test_num, '截留', '移交法制部门')
        global id, jld_id
        id = self.dr.find_element_by_xpath('//*[@id="list"]/tbody[1]/tr/td[3]').text
        jld_id = self.dr.find_element_by_xpath('//*[@id="jldbh"]').get_attribute('value')

    def test02_移交法制部门_查询(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        self.dr.find_element_by_xpath('//*[@id="8ca11cb733f843e8a4c63f8b579da538"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_8ca11cb733f843e8a4c63f8b579da538"]/iframe')
        self.dr.switch_to.frame(iframe)
        search_value = {'ks': '携带物一科', 'jldbh': jld_id, 'wpmc': '', 'state': '待处理'}
        self.xdw_yjfzbm_jlwcl_search(search_value)
        self.assertEqual(jld_id, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[1]').text)
        self.assertEqual('请先入库', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[13]').text)

    def test03_移交法制部门_转库(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        self.dr.find_element_by_xpath('//*[@id="f683e4f46b094a8ba68ad201a6e5b7bf"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_f683e4f46b094a8ba68ad201a6e5b7bf"]/iframe')
        self.dr.switch_to.frame(iframe)
        search_value = {'startTime': '', 'endTime': '', 'wpbh': id, 'wpmc': '', 'wplb': '--全部--', 'clff': '--全部--'}
        self.xdw_Onsite_transfer_or_storage_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="3lists"]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['wpbh'], 2, 1)
        self.xdw_Onsite_transfer_or_storage_print()
        self.xdw_Onsite_transfer_or_storage_transfer()

    def test04_移交法制部门_转库确认接收(self):
        self.login_keyuan(login_name_user4, login_name_password4)
        self.dr.find_element_by_xpath('//*[@id="436c1edb6d364195beb2ca044dceb58f"]/a').click()
        self.dr.find_element_by_xpath('//*[@id="d98aa4bffc93479b984febde6df22110"]/a/span').click()
        iframe = self.dr.find_element_by_xpath('//*[@id="sub_d98aa4bffc93479b984febde6df22110"]/iframe')
        self.dr.switch_to.frame(iframe)
        search_value = {'wpbh': id, 'wpmc': '', 'start': '', 'end': ''}
        self.xdw_Transfer_confirmation_receipt_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="tbList"]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['wpbh'], 2, 3)
        self.xdw_Transfer_confirmation_receipt()

    def test05_移交法制部门_处理_退回(self):
        self.login_keyuan(login_name_user4, login_name_password4)
        self.dr.find_element_by_xpath('//*[@id="8ca11cb733f843e8a4c63f8b579da538"]/a/span').click()
        iframe = self.dr.find_element_by_xpath('//*[@id="sub_8ca11cb733f843e8a4c63f8b579da538"]/iframe')
        self.dr.switch_to.frame(iframe)
        self.dr.find_element_by_xpath('//*[@id="form"]/div/div[2]/input').send_keys(jld_id)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        self.assertIsNotNone(self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[13]/div/button'))
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[13]/div/button').click()
        time.sleep(2)
        Select(self.dr.find_element_by_xpath('//*[@id="jlwpjglx"]')).select_by_visible_text('退回')
        self.dr.find_element_by_xpath('//*[@id="ajjg"]').send_keys('退回')
        date = time.strftime("%Y-%m-%d",time.localtime(time.time()))
        self.dr.find_element_by_xpath('//*[@id="jasj"]').send_keys(date)
        time.sleep(3)
        self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[2]/td[2]').click()
        self.dr.find_element_by_xpath('/html/body/div[4]/div[3]/div/button[2]').click()
        time.sleep(2)
        self.assertEqual('没有找到匹配的记录',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text)

    def test06_移交法制部门_退回出库(self):
        self.login_keyuan(login_name_user4, login_name_password4)
        self.dr.find_element_by_xpath('//*[@id="436c1edb6d364195beb2ca044dceb58f"]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="c41ac273606c43a9beaf3eebd4c86887"]/a/span').click()
        iframe = self.dr.find_element_by_xpath('//*[@id="sub_c41ac273606c43a9beaf3eebd4c86887"]/iframe')
        self.dr.switch_to.frame(iframe)
        search_value = {'wpbh': id, 'wpmc': '', 'startTime': '', 'endTime': ''}
        self.xdw_return_search(search_value)
        search_num = self.dr.find_element_by_xpath(
            '/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['wpbh'], 1, 0)
        self.xdw_return_th()

    def test07_移交法制部门_出库记录(self):
        self.login_keyuan(login_name_user4, login_name_password4)
        self.dr.find_element_by_xpath('//*[@id="dcefdfba1ea04e2db15876bd8673651d"]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="487efff4218945aca782559296990c47"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_487efff4218945aca782559296990c47"]/iframe')
        self.dr.switch_to.frame(iframe)
        self.dr.find_element_by_xpath('//*[@id="wpbh"]').send_keys(id)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(2)
        self.assertEqual(id,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[1]').text)
        self.assertEqual('退回',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[6]').text)

if __name__ == '__main__':
    unittest.main()