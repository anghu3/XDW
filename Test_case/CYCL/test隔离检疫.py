from Setting.setting_file import xdw_TestCase
from Setting.cycl import cycl_TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from Setting.setting_file import login_name_user1,login_name_password1,login_name_user2,login_name_password2,setting_xls
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
        self.dr.switch_to.default_content()
        self.dr.find_element_by_xpath('//*[@id="'+data['隔离检疫']+'"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_'+data['隔离检疫']+'"]/iframe')
        self.dr.switch_to.frame(iframe)
        time.sleep(1)

    def test01_隔离检疫_查询_状态(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        status=['未处理','待审核','已完结','--全部--']
        for state in status:
            if state=='--全部--':
                pass
            else:
                search_value={'status':state}
                self.xdw_Isolation_and_Quarantine_search(search_value)

    def test02_隔离检疫_合格放行处理(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        self.xdw_Isolation_and_Quarantine_Handle_Unqualified({'clfs':'退回'})

    def test02_隔离检疫_审核(self):
        self.login_keyuan(login_name_user2,login_name_password2)
        self.Initialization()
        self.xdw_Isolation_and_Quarantine_Handle_Unqualified({'clfs':'退回'})
        self.xdw_Isolation_and_Quarantine_search({'status': '待审核'})
        self.xdw_Isolation_and_Quarantine_Handle_examine()

if __name__ == '__main__':
    unittest.main()