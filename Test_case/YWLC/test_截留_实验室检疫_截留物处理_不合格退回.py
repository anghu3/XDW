from Setting.setting_file import xdw_TestCase
from Setting.cycl import cycl_TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from Setting.setting_file import login_name_user1,login_name_password1,login_name_user4,login_name_password4,setting_xls
import xlrd
import random
from Setting.menu import data
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
        self.login_keyuan(login_name_user1,login_name_password1)
        time.sleep(2)

    def Initialization_2(self):
        self.login_keyuan(login_name_user4,login_name_password4)
        time.sleep(2)

    def test01_实验室检疫_录单(self):
        self.Initialization_1()
        self.xdw_Inspection_addition(test_num, '截留', '实验室检疫')
        global id, jld_id
        id = self.dr.find_element_by_xpath('//*[@id="list"]/tbody[1]/tr/td[3]').text
        jld_id = self.dr.find_element_by_xpath('//*[@id="jldbh"]').get_attribute('value')

    def test02_实验室检疫_截留物处理查询(self):
        self.Initialization_1()
        self.dr.find_element_by_xpath('//*[@id="' + data['截留物处理'] + '"]').click()
        iframe = self.dr.find_element_by_xpath('//*[@id="sub_' + data['截留物处理'] + '"]/iframe')
        self.dr.switch_to.frame(iframe)
        time.sleep(1)
        search_value = {'ks': '', 'wpbh': id, 'wpmc': '', 'clffmx': '--全部--', 'clzt': '--全部--'}
        self.xdw_Other_Interception_Processing_search(search_value)
        time.sleep(2)
        self.assertEqual(id,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[1]').text)
        self.assertEqual('请先入库',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]').text)

    def test03_实验室检疫_入库(self):
        self.Initialization_1()
        self.dr.find_element_by_xpath('//*[@id="' + data['现场转库或入库'] + '"]').click()
        iframe = self.dr.find_element_by_xpath('//*[@id="sub_' + data['现场转库或入库'] + '"]/iframe')
        self.dr.switch_to.frame(iframe)
        time.sleep(1)
        print(id)
        search_value = {'startTime': '', 'endTime': '', 'wpbh': jld_id, 'wpmc': '', 'wplb': '--全部--',
                        'clff': '--全部--'}
        self.xdw_Onsite_transfer_or_storage_search(search_value)
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[10]/div/button').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('//*[@id="'
                                      'inStorageBtn"]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[6]/div[3]/div/button[2]').click()
        time.sleep(3)
        self.assertEqual('没有找到匹配的记录', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text)

    def test04_实验室检疫_截留物处理查询(self):
        self.Initialization_1()
        self.dr.find_element_by_xpath('//*[@id="' + data['截留物处理'] + '"]').click()
        iframe = self.dr.find_element_by_xpath('//*[@id="sub_' + data['截留物处理'] + '"]/iframe')
        self.dr.switch_to.frame(iframe)
        search_value = {'ks': '', 'wpbh': id, 'wpmc': '', 'clffmx': '--全部--', 'clzt': '--全部--'}
        self.xdw_Other_Interception_Processing_search(search_value)
        time.sleep(2)
        self.assertEqual(id,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[1]').text)
        self.assertEqual('请先出库',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]').text)

    def test05_实验室检疫_出库(self):
        self.Initialization_1()
        self.dr.find_element_by_xpath('//*[@id="'+data['仓库管理']+'"]').click()
        self.dr.find_element_by_xpath('//*[@id="'+data['出库']+'"]').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_'+data['出库']+'"]/iframe')
        self.dr.switch_to.frame(iframe)
        search_value = {'wpbh': id, 'wpmc': '', 'startTime': '', 'endTime': '', 'clff': '--全部--',
                        'ckjglx': '--全部--'}
        self.xdw_ck_Inspection_search()
        self.xdw_ck_normal_search(search_value)
        search_num = self.dr.find_element_by_xpath(
            '/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['wpbh'], 2, 0)
        self.xdw_ck_normal_sjck({'telphone': '15263859674', 'ypmc': '15263857485'})

    # def test06_送检出库单据查询(self):
    #     self.Initialization_1()
    #     self.dr.find_element_by_xpath('//*[@id="dcefdfba1ea04e2db15876bd8673651d"]').click()
    #     self.dr.find_element_by_xpath('//*[@id="572690ac226643d49731ea192e62b665"]').click()
    #     iframe=self.dr.find_element_by_xpath('//*[@id="sub_572690ac226643d49731ea192e62b665"]/iframe')
    #     self.dr.switch_to.frame(iframe)
    #     self.dr.find_element_by_xpath('//*[@id="wpbh"]').send_keys(id)
    #     self.dr.find_element_by_xpath('//*[@id="search"]').click()
    #     time.sleep(2)
    #     self.assertEqual(id,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[2]').text)
    #
    # def test07_实验室检疫_送样结果录入(self):
    #     self.Initialization_1()
    #     self.dr.find_element_by_xpath('//*[@id="90572387ce7e48fba50f57eaf0dc3049"]').click()
    #     iframe=self.dr.find_element_by_xpath('//*[@id="sub_90572387ce7e48fba50f57eaf0dc3049"]/iframe')
    #     self.dr.switch_to.frame(iframe)
    #     search_value = {'wpbh': id, 'mc': '', 'start': '', 'end': '', 'zt': '--全部--'}
    #     self.xdw_Sampling_result_input_search(search_value)
    #     search_num = self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
    #     self.pagination_num(search_num, search_value['wpbh'], 2, 4)
    #     self.xdw_Sampling_result_input_input(id)
    #
    # def test08_截留物处理_不合格退回(self):
    #     self.Initialization_1()
    #     self.dr.find_element_by_xpath('//*[@id="88f0f33abf2d48419438a72637c27b49"]/a').click()
    #     iframe=self.dr.find_element_by_xpath('//*[@id="sub_88f0f33abf2d48419438a72637c27b49"]/iframe')
    #     self.dr.switch_to.frame(iframe)
    #     search_value = {'ks': '', 'wpbh': id, 'wpmc': '', 'clffmx': '--全部--', 'clzt': '--全部--'}
    #     self.xdw_Other_Interception_Processing_search(search_value)
    #     search_num = self.dr.find_element_by_xpath('//*[@id="tbList"]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
    #     self.pagination_num(search_num, search_value['wpbh'], 1, 3)
    #     self.xdw_Other_Interception_Processing_Handle({'jlcljg': '不合格', 'jlwpjg': '退回'})
    #
    # def test09_实验室检疫_不合格退回出库(self):
    #     self.Initialization_1()
    #     self.dr.find_element_by_xpath('//*[@id="436c1edb6d364195beb2ca044dceb58f"]').click()
    #     self.dr.find_element_by_xpath('//*[@id="c41ac273606c43a9beaf3eebd4c86887"]').click()
    #     iframe=self.dr.find_element_by_xpath('//*[@id="sub_c41ac273606c43a9beaf3eebd4c86887"]/iframe')
    #     self.dr.switch_to.frame(iframe)
    #     search_value = {'wpbh': id, 'wpmc': '', 'startTime': '', 'endTime': ''}
    #     self.xdw_return_search(search_value)
    #     search_num = self.dr.find_element_by_xpath(
    #         '/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
    #     self.pagination_num(search_num, search_value['wpbh'], 1, 0)
    #     self.xdw_return_th()
    #
    # def test10_实验室检疫_不合格退回_出库记录查询(self):
    #     self.Initialization_1()
    #     self.dr.find_element_by_xpath('//*[@id="dcefdfba1ea04e2db15876bd8673651d"]').click()
    #     self.dr.find_element_by_xpath('//*[@id="487efff4218945aca782559296990c47"]').click()
    #     iframe=self.dr.find_element_by_xpath('//*[@id="sub_487efff4218945aca782559296990c47"]/iframe')
    #     self.dr.switch_to.frame(iframe)
    #     self.dr.find_element_by_xpath('//*[@id="wpbh"]').send_keys(id)
    #     self.dr.find_element_by_xpath('//*[@id="search"]/span').click()
    #     time.sleep(1)
    #     self.assertEqual(id,self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[1]').text)
    #     self.assertEqual('退回',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[6]').text)

if __name__ == '__main__':
    unittest.main()