from Setting.setting_file import xdw_TestCase
from Setting.cycl import cycl_TestCase
import unittest
import time
from Setting.setting_file import login_name_user1,login_name_password1,login_name_user4,login_name_password4,setting_xls
import random


class xdwcy_TestCase(xdw_TestCase,cycl_TestCase):

    def Initialization(self):
        self.dr.find_element_by_xpath('//*[@id="dcefdfba1ea04e2db15876bd8673651d"]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="047b073794584993be96d086e3b9b5cb"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_047b073794584993be96d086e3b9b5cb"]/iframe')
        self.dr.switch_to.frame(iframe)
        time.sleep(1)

    def test01_转库单据_查询_转库单号(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'zkdj':'ZK0000001907178','wpbh':'','wpmc':'','start':'','end':'','czr':'','zklx':'转出库'}
        self.xdw_zkdj_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['zkdj'],1,6)

    def test02_转库单据_查询_物品编号(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'zkdj':'','wpbh':'00000019070058901','wpmc':'','start':'','end':'','czr':'','zklx':'转出库'}
        self.xdw_zkdj_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['wpbh'],2,6)

    def test03_转库单据_查询_物品名称(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'zkdj':'','wpbh':'','wpmc':'石榴','start':'','end':'','czr':'','zklx':'转出库'}
        self.xdw_zkdj_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['wpmc'],3,6)

    def test04_转库单据_查询_操作日期(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'zkdj':'','wpbh':'','wpmc':'','start':'2019-07-22','end':'2019-07-22','czr':'','zklx':'转出库'}
        self.xdw_zkdj_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['start'],5,6)

    def test05_转库单据_查询_操作人(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'zkdj':'','wpbh':'','wpmc':'','start':'','end':'','czr':'胡亮2','zklx':'转出库'}
        self.xdw_zkdj_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['start'],7,6)

    def test06_转库单据_查询_转库类型(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        zklxs=['转出库','转入库']
        for zklx in zklxs:
            search_value={'zkdj':'','wpbh':'','wpmc':'','start':'','end':'','czr':'','zklx':zklx}
            self.xdw_zkdj_search(search_value)
            search_num = self.dr.find_element_by_xpath(
                '/html/body/div[1]/div/div/div/div[1]/div/div[4]/div[1]/span[1]').text
            self.pagination_num(search_num,search_value['zklx'],8,6)

    def test07_转库单据_查询_组合查询(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'zkdj':'ZK0000001907178','wpbh':'00000019070058901','wpmc':'石榴','start':'2019-07-22','end':'2019-07-22','czr':'胡亮2','zklx':'转出库'}
        self.xdw_zkdj_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['zkdj'], 1, 6)
        self.pagination_num(search_num, search_value['wpbh'], 2, 6)
        self.pagination_num(search_num, search_value['wpmc'], 3, 6)
        self.pagination_num(search_num, search_value['start'], 5, 6)
        self.pagination_num(search_num, search_value['zklx'], 8, 6)

    def test08_转库单据_查询_打印(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'zkdj':'ZK0000001907178','wpbh':'00000019070058901','wpmc':'石榴','start':'2019-07-22','end':'2019-07-22','czr':'胡亮2','zklx':'转出库'}
        self.xdw_zkdj_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['zkdj'],1,6)
        self.pagination_num(search_num, search_value['wpbh'], 2, 6)
        self.pagination_num(search_num, search_value['wpmc'], 3, 6)
        self.pagination_num(search_num, search_value['start'], 5, 6)
        self.pagination_num(search_num, search_value['zklx'], 8, 6)
        self.xdw_zkdj_print(search_value)


if __name__ == '__main__':
    unittest.main()