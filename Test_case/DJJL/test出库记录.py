from Setting.setting_file import xdw_TestCase
from Setting.cycl import cycl_TestCase
import unittest
import time
from Setting.setting_file import login_name_user1,login_name_password1,login_name_user4,login_name_password4,setting_xls
import random
import xlrd

Testdata = xlrd.open_workbook(setting_xls)
sheet_passenger=Testdata.sheet_by_name('旅客信息')
sheet_goods=Testdata.sheet_by_name('物品信息')
sheet_goods_articles=Testdata.sheet_by_name('物品类别')

class xdwcy_TestCase(xdw_TestCase,cycl_TestCase):

    def Initialization(self):
        self.dr.find_element_by_xpath('//*[@id="dcefdfba1ea04e2db15876bd8673651d"]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="487efff4218945aca782559296990c47"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_487efff4218945aca782559296990c47"]/iframe')
        self.dr.switch_to.frame(iframe)
        time.sleep(1)

    def test01_出库记录_查询_物品编号(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'00000019070043101','wpmc':'','wplb':{'wpdl':'','wpxl':''},'startTime':'','endTime':'','ckjglx':'全部'}
        self.xdw_ckjl_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['wpbh'],1,7)

    def test02_出库记录_查询_物品名称(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'','wpmc':'苹果','wplb':{'wpdl':'','wpxl':''},'startTime':'','endTime':'','ckjglx':'全部'}
        self.xdw_ckjl_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['wpmc'],2,7)

    def test03_出库记录_查询_物品类别(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'','wpmc':'苹果','wplb':{'wpdl':'12','wpxl':'13'},'startTime':'','endTime':'','ckjglx':'全部'}
        self.xdw_ckjl_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,sheet_goods_articles.col_values(0,12,13)[0],3,7)

    def test04_出库记录_查询_出库时间(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'','wpmc':'','wplb':{'wpdl':'','wpxl':''},'startTime':'2019-07-22','endTime':'2019-07-22','ckjglx':'全部'}
        self.xdw_ckjl_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['startTime'],5,7)

    def test05_出库记录_查询_出库类型(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        ckjglxs=['全部','销毁','退回','放行','移交海关','移交保护部门','送样','展品']
        for ckjglx in ckjglxs:
            if ckjglx=='全部':
                pass
            else:
                search_value={'wpbh':'','wpmc':'芒果','wplb':{'wpdl':'','wpxl':''},'startTime':'','endTime':'','ckjglx':ckjglx}
                self.xdw_ckjl_search(search_value)
                search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
                self.pagination_num(search_num, search_value['ckjglx'], 6, 7)

    def test06_出库记录_查询_出库时间(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'00000019070043101','wpmc':'苹果','wplb':{'wpdl':'12','wpxl':'13'},'startTime':'2019-07-25','endTime':'2019-07-25','ckjglx':'送样'}
        self.xdw_ckjl_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['wpbh'], 1, 7)
        self.pagination_num(search_num, search_value['wpmc'], 2, 7)
        self.pagination_num(search_num, sheet_goods_articles.col_values(0, 12, 13)[0], 3, 7)
        self.pagination_num(search_num, search_value['startTime'], 5, 7)
        self.pagination_num(search_num, search_value['ckjglx'], 6, 7)

    def test06_出库记录_查询_导出(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'00000019070043101','wpmc':'苹果','wplb':{'wpdl':'12','wpxl':'13'},'startTime':'2019-07-25','endTime':'2019-07-25','ckjglx':'送样'}
        self.xdw_ckjl_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['wpbh'], 1, 7)
        self.pagination_num(search_num, search_value['wpmc'], 2, 7)
        self.pagination_num(search_num, sheet_goods_articles.col_values(0, 12, 13)[0], 3, 7)
        self.pagination_num(search_num, search_value['startTime'], 5, 7)
        self.pagination_num(search_num, search_value['ckjglx'], 6, 7)
        self.xdw_ckjl_export()
        self.xdw_ckjl_export()

if __name__ == '__main__':
    unittest.main()