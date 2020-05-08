from Setting.setting_file import xdw_TestCase
from Setting.cycl import cycl_TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from Setting.setting_file import login_name_user1,login_name_password1,login_name_user2,login_name_password2,setting_xls
import random

class xdw_TestCase(xdw_TestCase,cycl_TestCase):

    global now
    now = time.strftime("%Y-%m-%d", time.localtime(time.time()))

    def Initialization(self):
        self.dr.switch_to.default_content()
        self.dr.find_element_by_xpath('//*[@id="b08e88dd0b16404cabbbe73e40028c6f"]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="776fac442f36422481f6a06d2ec326c5"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_776fac442f36422481f6a06d2ec326c5"]/iframe')
        self.dr.switch_to.frame(iframe)
        time.sleep(2)

    def test01_业务流程查询_查询(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        test_num = random.randint(1, 10)
        self.xdw_Inspection_addition(test_num, '销毁', '')
        id = self.dr.find_element_by_xpath('//*[@id="list"]/tbody[1]/tr/td[3]').text
        jld_id = self.dr.find_element_by_xpath('//*[@id="jldbh"]').get_attribute('value')

        self.Initialization()
        # search_value={'lx':'物品记录','wpbh':id,'jldh':jld_id}
        self.xdw_ywlccx_search({'lx':'物品记录','wpbh':id,'jldh':jld_id})
        self.xdw_ywlccx_search({'lx': '截留单记录', 'wpbh': id, 'jldh': jld_id})



if __name__ == '__main__':
    unittest.main()