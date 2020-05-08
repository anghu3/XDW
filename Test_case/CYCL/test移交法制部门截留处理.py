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
        self.dr.find_element_by_xpath('//*[@id="'+data['移交法制部门截留处理']+'"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_'+data['移交法制部门截留处理']+'"]/iframe')
        self.dr.switch_to.frame(iframe)
        time.sleep(3)

    def test01_移交法制部门截留处理_查询_截留单号(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        search_value={'ks':'携带物一科','jldbh':'000000191100035','wpmc':'','state':'待处理'}
        self.Initialization()
        self.xdw_yjfzbm_jlwcl_search(search_value)

    def test02_移交法制部门截留处理_查询_物品名称(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        search_value={'ks':'携带物一科','jldbh':'','wpmc':'芒果','state':'待处理'}
        self.Initialization()
        self.xdw_yjfzbm_jlwcl_search(search_value)

    def test03_移交法制部门截留处理_查询_状态(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        status=['--全部--','待处理','已处理']
        for state in status:
            if state == '--全部--':
                pass
            else:
                search_value={'ks':'携带物一科','jldbh':'','wpmc':'','state':state}
                self.xdw_yjfzbm_jlwcl_search(search_value)

if __name__ == '__main__':
    unittest.main()