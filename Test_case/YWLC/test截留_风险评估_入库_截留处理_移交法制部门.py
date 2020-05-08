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

    def test04_风险评估_截留物处理_移交法制部门(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.dr.find_element_by_xpath('//*[@id="88f0f33abf2d48419438a72637c27b49"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_88f0f33abf2d48419438a72637c27b49"]/iframe')
        self.dr.switch_to.frame(iframe)
        search_value = {'ks': '', 'wpbh': id, 'wpmc': '', 'clffmx': '--全部--', 'clzt': '--全部--'}
        self.xdw_Other_Interception_Processing_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="tbList"]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['wpbh'], 1, 3)
        self.xdw_Other_Interception_Processing_Handle({'jlcljg': '移交法制部门', 'jlwpjg': '----'})

    def test05_移交法制部门查询(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        self.dr.find_element_by_xpath('//*[@id="8ca11cb733f843e8a4c63f8b579da538"]/a').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_8ca11cb733f843e8a4c63f8b579da538"]/iframe')
        self.dr.switch_to.frame(iframe)
        self.dr.find_element_by_xpath('//*[@id="form"]/div/div[2]/input').send_keys(jld_id)
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(2)
        self.assertEqual(jld_id,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[1]').text)



if __name__ == '__main__':
    unittest.main()