from Setting.setting_file import xdw_TestCase
from Setting.cycl import cycl_TestCase
import unittest
import time
from Setting.setting_file import login_name_user1,login_name_password1,login_name_user4,login_name_password4,setting_xls
from Setting.menu import data
import xlrd
import random

class xdw_TestCase(xdw_TestCase,cycl_TestCase):

    global now
    now = time.strftime("%Y-%m-%d", time.localtime(time.time()))

    def Initialization(self):
        self.dr.switch_to.default_content()
        self.dr.find_element_by_xpath('//*[@id="'+data['截留物处理']+'"]').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_'+data['截留物处理']+'"]/iframe')
        self.dr.switch_to.frame(iframe)
        time.sleep(1)

    def test01_其他截留物处理_查询_物品编号(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'ks':'','wpbh':'00000019060008801','wpmc':'','clffmx':'--全部--','clzt':'--全部--'}
        self.xdw_Other_Interception_Processing_search(search_value)
        search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['wpbh'],1,3)

    def test02_其他截留物处理_查询_物品名称(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'ks':'','wpbh':'','wpmc':'柠檬','clffmx':'--全部--','clzt':'--全部--'}
        self.xdw_Other_Interception_Processing_search(search_value)
        search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['wpmc'],2,3)

    def test03_其他截留物处理_查询_截留状态(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        clffmxs=['--全部--','补办手续','实验室检疫','风险评估']
        for clffmx in clffmxs:
            if clffmx=='--全部--':
                pass
            else:
                search_value={'ks':'','wpbh':'','wpmc':'芒果','clffmx':clffmx,'clzt':'--全部--'}
                self.xdw_Other_Interception_Processing_search(search_value)
                search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
                self.pagination_num(search_num,search_value['clffmx'],5,3)

    def test04_其他截留物处理_查询_状态(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        clzts=['--全部--','待处理','已处理']
        for clzt in clzts:
            if clzt=='--全部--':
                pass
            else:
                search_value={'ks':'','wpbh':'','wpmc':'芒果','clffmx':'--全部--','clzt':clzt}
                self.xdw_Other_Interception_Processing_search(search_value)
                search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
                self.pagination_num(search_num,search_value['clzt'],6,3)

    def test05_其他截留物处理_查询_组合查询(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        self.Initialization()
        search_value = {'ks': '', 'wpbh': '00000019060008801', 'wpmc': '柠檬', 'clffmx': '补办手续', 'clzt': '待处理'}
        self.xdw_Other_Interception_Processing_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="tbList"]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['wpbh'], 1, 3)
        self.pagination_num(search_num, search_value['wpmc'], 2, 3)
        self.pagination_num(search_num, search_value['clffmx'], 5, 3)
        self.pagination_num(search_num, search_value['clzt'], 6, 3)

    # def test06_其他截留物处理_处理_合格放行(self):
    #     self.login_keyuan(login_name_user1,login_name_password1)
    #     test_num = random.randint(1, 10)
    #     self.xdw_Inspection_addition(test_num, '截留', '风险评估')
    #     id = self.dr.find_element_by_xpath('//*[@id="list"]/tbody[1]/tr/td[3]').text
    #     jld_id = self.dr.find_element_by_xpath('//*[@id="jldbh"]').get_attribute('value')
    #     self.dr.switch_to.default_content()
    #     self.dr.find_element_by_xpath('//*[@id="88f0f33abf2d48419438a72637c27b49"]').click()
    #     iframe = self.dr.find_element_by_xpath('//*[@id="sub_88f0f33abf2d48419438a72637c27b49"]/iframe')
    #     self.dr.switch_to.frame(iframe)
    #     time.sleep(2)
    #     search_value = {'startTime': '', 'endTime': '', 'wpbh': id, 'wpmc': '', 'wplb': '--全部--', 'clff': '--全部--'}
    #     self.xdw_Onsite_transfer_or_storage_search(search_value)
    #     search_num = self.dr.find_element_by_xpath('//*[@id="3lists"]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
    #     self.pagination_num(search_num, search_value['wpbh'], 2, 1)
    #     self.xdw_Onsite_transfer_or_storage_print()
    #     self.xdw_Onsite_transfer_or_storage_storage()
    #     self.Initialization()
    #     search_value = {'ks': '', 'wpbh': id, 'wpmc': '', 'clffmx': '--全部--', 'clzt': '--全部--'}
    #     self.xdw_Other_Interception_Processing_search(search_value)
    #     search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
    #     time.sleep(5)
    #     self.pagination_num(search_num,search_value['wpbh'],1,3)
    #     self.xdw_Other_Interception_Processing_Handle({'jlcljg':'合格','jlwpjg':'放行'})


if __name__ == '__main__':
    unittest.main()