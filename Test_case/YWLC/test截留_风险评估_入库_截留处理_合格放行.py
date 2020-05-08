from Setting.setting_file import xdw_TestCase
from Setting.cycl import cycl_TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from Setting.setting_file import login_name_user1,login_name_password1,login_name_user4,login_name_password4,setting_xls
import xlrd
import random


class xdwcy_TestCase(xdw_TestCase,cycl_TestCase):

    def test01_风险评估_录单(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        test_num = random.randint(1, 10)
        self.xdw_Inspection_addition(test_num, '截留', '风险评估')
        global id, jld_id
        id = self.dr.find_element_by_xpath('//*[@id="list"]/tbody[1]/tr/td[3]').text
        jld_id = self.dr.find_element_by_xpath('//*[@id="jldbh"]').get_attribute('value')

    def test02_风险评估_截留物处理查询(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.dr.find_element_by_xpath('//*[@id="88f0f33abf2d48419438a72637c27b49"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_88f0f33abf2d48419438a72637c27b49"]/iframe')
        self.dr.switch_to.frame(iframe)
        search_value = {'ks': '', 'wpbh': id, 'wpmc': '', 'clffmx': '--全部--', 'clzt': '--全部--'}
        self.xdw_Other_Interception_Processing_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="tbList"]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['wpbh'], 1, 3)
        self.assertEqual('请先入库',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]').text)

    def test03_风险评估_入库(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.dr.find_element_by_xpath('//*[@id="f683e4f46b094a8ba68ad201a6e5b7bf"]/a/span').click()
        iframe = self.dr.find_element_by_xpath('//*[@id="sub_f683e4f46b094a8ba68ad201a6e5b7bf"]/iframe')
        self.dr.switch_to.frame(iframe)
        search_value = {'startTime': '', 'endTime': '', 'wpbh': id, 'wpmc': '', 'wplb': '--全部--', 'clff': '--全部--'}
        self.xdw_Onsite_transfer_or_storage_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="3lists"]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['wpbh'], 2, 1)
        self.xdw_Onsite_transfer_or_storage_print()
        self.xdw_Onsite_transfer_or_storage_storage()

    def test04_风险评估_截留物处理_合格放行(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.dr.find_element_by_xpath('//*[@id="88f0f33abf2d48419438a72637c27b49"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_88f0f33abf2d48419438a72637c27b49"]/iframe')
        self.dr.switch_to.frame(iframe)
        search_value = {'ks': '', 'wpbh': id, 'wpmc': '', 'clffmx': '--全部--', 'clzt': '--全部--'}
        self.xdw_Other_Interception_Processing_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="tbList"]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['wpbh'], 1, 3)
        self.xdw_Other_Interception_Processing_Handle({'jlcljg': '合格', 'jlwpjg': '放行'})

    def test05_风险评估_合格放行出库(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.dr.find_element_by_xpath('//*[@id="436c1edb6d364195beb2ca044dceb58f"]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="6c25cddc87d7418fb9825b762737a2c0"]/a').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_6c25cddc87d7418fb9825b762737a2c0"]/iframe')
        self.dr.switch_to.frame(iframe)
        search_value = {'wpbh': id, 'wpmc': '', 'startTime': '', 'endTime': '', 'clff': '--全部--',
                        'ckjglx': '--全部--'}
        self.xdw_ck_normal_search(search_value)
        search_num = self.dr.find_element_by_xpath(
            '/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['wpbh'], 2, 0)
        self.xdw_ck_normal_fxck()

    def test06_出库记录查询(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        self.dr.find_element_by_xpath('//*[@id="dcefdfba1ea04e2db15876bd8673651d"]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="487efff4218945aca782559296990c47"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_487efff4218945aca782559296990c47"]/iframe')
        self.dr.switch_to.frame(iframe)
        search_value = {'wpbh': id, 'wpmc': '', 'wplb': {'wpdl': '', 'wpxl': ''}, 'startTime': '',
                        'endTime': '', 'ckjglx': '放行'}
        self.xdw_ckjl_search(search_value)
        search_num = self.dr.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['wpbh'], 1, 7)
        self.pagination_num(search_num, search_value['ckjglx'], 6, 7)

if __name__ == '__main__':
    unittest.main()