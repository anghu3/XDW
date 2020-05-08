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
        self.dr.find_element_by_xpath('//*[@id="4d3ab789b33340a088ca82eef04076f0"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_4d3ab789b33340a088ca82eef04076f0"]/iframe')
        self.dr.switch_to.frame(iframe)
        time.sleep(2)

    def test01_仓库盘点_查询_物品编号(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'00000019070086101','wpmc':'','wpfl':'所有','clfs':'所有','minTime':'','maxTime':''}
        self.xdw_ckpd_search(search_value)
        self.assertEqual(search_value['wpbh'],self.dr.find_element_by_xpath('//*[@id="list1"]/tbody/tr/td[1]').text)

    def test02_仓库盘点_查询_物品名称(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'','wpmc':'酸奶','wpfl':'所有','clfs':'所有','minTime':'','maxTime':''}
        self.xdw_ckpd_search(search_value)
        self.assertEqual(search_value['wpmc'],self.dr.find_element_by_xpath('//*[@id="list1"]/tbody/tr/td[2]').text)

    def test03_仓库盘点_查询_物品类别(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        wpfls=['所有','动检','特殊物品','蛋及蛋制品','种子（苗）/苗木/其他具有繁殖能力的植物材料','宠物（犬、猫）','奶及奶制品','新鲜水果','燕窝','肉类及其制品','新鲜蔬菜','水生动物产品','植检']
        for wpfl in wpfls:
            if wpfl=='所有':
                pass
            else:
                search_value={'wpbh':'','wpmc':'','wpfl':wpfl,'clfs':'所有','minTime':'','maxTime':''}
                self.xdw_ckpd_search(search_value)
                self.assertEqual(search_value['wpfl'],self.dr.find_element_by_xpath('//*[@id="list1"]/tbody/tr/td[3]').text)

    def test04_仓库盘点_查询_处理方式(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        clfss=['所有','限期(退回)','销毁','移交法制部门(截留)','补办手续(截留)','隔离检疫','实验室检疫(截留)','风险评估(截留)']
        for clfs in clfss:
            if clfs=='所有':
                pass
            else:
                search_value={'wpbh':'','wpmc':'','wpfl':'所有','clfs':clfs,'minTime':'','maxTime':''}
                # self.xdw_ckpd_search(search_value)
                # self.assertEqual(search_value[clfs],self.dr.find_element_by_xpath('//*[@id="list1"]/tbody/tr/td[6]').text)

    def test05_仓库盘点_查询_入境时间(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'','wpmc':'','wpfl':'所有','clfs':'所有','minTime':'2019-07-22','maxTime':'2019-07-22'}
        self.xdw_ckpd_search(search_value)
        self.assertIn(search_value['minTime'],self.dr.find_element_by_xpath('//*[@id="list1"]/tbody/tr/td[7]').text)

    def test06_仓库盘点_查询_组合查询(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'00000019070086101','wpmc':'芒果','wpfl':'新鲜水果','clfs':'移交法制部门(截留)','minTime':'2019-07-26','maxTime':'2019-07-26'}
        self.xdw_ckpd_search(search_value)
        self.assertIn(search_value['minTime'],self.dr.find_element_by_xpath('//*[@id="list1"]/tbody/tr/td[7]').text)
        self.assertEqual(search_value['wpfl'], self.dr.find_element_by_xpath('//*[@id="list1"]/tbody/tr/td[3]').text)
        self.assertEqual(search_value['wpmc'], self.dr.find_element_by_xpath('//*[@id="list1"]/tbody/tr/td[2]').text)
        self.assertEqual(search_value['wpbh'], self.dr.find_element_by_xpath('//*[@id="list1"]/tbody/tr/td[1]').text)

    def test07_仓库盘点_导出(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'00000019070086101','wpmc':'芒果','wpfl':'新鲜水果','clfs':'移交法制部门(截留)','minTime':'2019-07-26','maxTime':'2019-07-26'}
        self.xdw_ckpd_search(search_value)
        self.assertIn(search_value['minTime'],self.dr.find_element_by_xpath('//*[@id="list1"]/tbody/tr/td[7]').text)
        self.assertEqual(search_value['wpfl'], self.dr.find_element_by_xpath('//*[@id="list1"]/tbody/tr/td[3]').text)
        self.assertEqual(search_value['wpmc'], self.dr.find_element_by_xpath('//*[@id="list1"]/tbody/tr/td[2]').text)
        self.assertEqual(search_value['wpbh'], self.dr.find_element_by_xpath('//*[@id="list1"]/tbody/tr/td[1]').text)
        self.xdw_ckpd_export()

    def test08_仓库盘点_仓库物品汇总_查询_物品分类(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        self.xdw_ckpd_ckwphz()
        wpfls = ['所有', '动检', '特殊物品', '蛋及蛋制品', '种子（苗）/苗木/其他具有繁殖能力的植物材料', '宠物（犬、猫）', '奶及奶制品', '新鲜水果', '燕窝', '肉类及其制品',
                 '新鲜蔬菜', '水生动物产品', '植检']
        for wpfl in wpfls:
            if wpfl=='所有':
                pass
            else:
                search_value={'wpfl':wpfl,'minTime2':'','maxTime2':''}
                self.xdw_ckpd_ckwphz_search(search_value)
                self.assertIn(search_value['wpfl'],self.dr.find_element_by_xpath('//*[@id="list2"]/tbody/tr[1]/td[1]').text)

    def test09_仓库盘点_仓库物品汇总_查询_入境时间(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        self.xdw_ckpd_ckwphz()
        search_value = {'wpfl':'所有', 'minTime2': now, 'maxTime2': now}
        self.xdw_ckpd_ckwphz_search(search_value)

    def test10_仓库盘点_仓库物品汇总_查询_组合查询(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        self.xdw_ckpd_ckwphz()
        search_value = {'wpfl':'新鲜水果', 'minTime2': now, 'maxTime2': now}
        self.xdw_ckpd_ckwphz_search(search_value)
        self.assertIn(search_value['wpfl'], self.dr.find_element_by_xpath('//*[@id="list2"]/tbody/tr[1]/td[1]').text)

    def test11_仓库盘点_仓库物品汇总_导出(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        self.xdw_ckpd_ckwphz()
        search_value = {'wpfl': '新鲜水果', 'minTime2': now, 'maxTime2': now}
        self.xdw_ckpd_ckwphz_search(search_value)
        self.assertIn(search_value['wpfl'], self.dr.find_element_by_xpath('//*[@id="list2"]/tbody/tr[1]/td[1]').text)
        self.xdw_ckpd_ckwphz_export()

if __name__ == '__main__':
    unittest.main()