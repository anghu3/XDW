from Setting.setting_file import xdw_TestCase
from Setting.cycl import cycl_TestCase
import unittest
import time
from Setting.setting_file import login_name_user1,login_name_password1,login_name_user4,login_name_password4,setting_xls


class xdwcy_TestCase(xdw_TestCase,cycl_TestCase):

    def Initialization(self):
        self.dr.find_element_by_xpath('//*[@id="436c1edb6d364195beb2ca044dceb58f"]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="d98aa4bffc93479b984febde6df22110"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_d98aa4bffc93479b984febde6df22110"]/iframe')
        self.dr.switch_to.frame(iframe)
        time.sleep(1)

    def test01_转库接收确认_查询_物品编号(self):
        self.login_keyuan(login_name_user4,login_name_password4)
        self.Initialization()
        search_value={'wpbh':'00000019070061001','wpmc':'','start':'','end':''}
        self.xdw_Transfer_confirmation_receipt_search(search_value)
        search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['wpbh'],2,3)

    def test02_转库接收确认_查询_物品名称(self):
        self.login_keyuan(login_name_user4,login_name_password4)
        self.Initialization()
        search_value={'wpbh':'','wpmc':'香蕉','start':'','end':''}
        self.xdw_Transfer_confirmation_receipt_search(search_value)
        search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['wpmc'],3,3)

    def test03_转库接收确认_查询_截获时间(self):
        self.login_keyuan(login_name_user4,login_name_password4)
        self.Initialization()
        search_value={'wpbh':'','wpmc':'','start':'2019-07-22','end':'2019-07-22'}
        self.xdw_Transfer_confirmation_receipt_search(search_value)
        search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['wpmc'],5,3)

if __name__ == '__main__':
    unittest.main()