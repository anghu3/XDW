from Setting.setting_file import xdw_TestCase
from Setting.cycl import cycl_TestCase
import unittest
import time
from Setting.setting_file import login_name_user1,login_name_password1,login_name_user4,login_name_password4,setting_xls


class xdwcy_TestCase(xdw_TestCase,cycl_TestCase):

    def Initialization(self):
        self.dr.find_element_by_xpath('//*[@id="436c1edb6d364195beb2ca044dceb58f"]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="afea927b3edb4f418885a80eb7b81880"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_afea927b3edb4f418885a80eb7b81880"]/iframe')
        self.dr.switch_to.frame(iframe)
        time.sleep(1)

    def test01_转库_查询_物品编号(self):
        self.login_keyuan(login_name_user4,login_name_password4)
        self.Initialization()
        search_value={'wpbh':'00000019060004301','wpmc':'','rkr':'','start':'','end':''}
        self.xdw_Transfer_search(search_value)
        search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['wpbh'],2,4)

    def test02_转库_查询_物品名称(self):
        self.login_keyuan(login_name_user4,login_name_password4)
        self.Initialization()
        search_value={'wpbh':'','wpmc':'香肠','rkr':'','start':'','end':''}
        self.xdw_Transfer_search(search_value)
        search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['wpmc'],3,4)

    def test03_转库_查询_入库人(self):
        self.login_keyuan(login_name_user4,login_name_password4)
        self.Initialization()
        search_value={'wpbh':'','wpmc':'','rkr':'胡亮5','start':'','end':''}
        self.xdw_Transfer_search(search_value)
        search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['rkr'],8,4)

    def test04_转库_查询_入库日期(self):
        self.login_keyuan(login_name_user4,login_name_password4)
        self.Initialization()
        search_value={'wpbh':'','wpmc':'','rkr':'','start':'2019-07-15','end':'2019-07-15'}
        self.xdw_Transfer_search(search_value)
        search_num=self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['start'],7,4)

if __name__ == '__main__':
    unittest.main()