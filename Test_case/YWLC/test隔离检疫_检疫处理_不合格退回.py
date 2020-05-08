from Setting.setting_file import xdw_TestCase
from Setting.cycl import cycl_TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from Setting.setting_file import login_name_user1,login_name_password1,login_name_user2,login_name_password2,setting_xls
import xlrd
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class xdwcy_TestCase(xdw_TestCase,cycl_TestCase):

    def test01_隔离检疫_录单(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.dr.switch_to.default_content()
        time.sleep(2)
        iframe = self.dr.find_element_by_tag_name("iframe")
        self.dr.switch_to.frame(iframe)
        self.dr.find_element_by_xpath('//*[@id="lkxm"]').send_keys('liulin')
        Select(self.dr.find_element_by_xpath('//*[@id="xb"]')).select_by_value('女')
        self.dr.find_element_by_xpath('//*[@id="lkbz"]').send_keys('测试数据')
        # 点击国籍输入框
        self.dr.find_element_by_xpath('//*[@id="gj"]').click()
        # 选择序号为43的国籍
        self.dr.find_element_by_xpath('//*[@id="comefromContainer"]/ul/li[43]').click()
        self.dr.find_element_by_xpath('//*[@id="csrq"]').send_keys('19920216')
        self.dr.find_element_by_xpath('//*[@id="btnZjlx"]').click()
        all = self.dr.window_handles
        self.dr.switch_to.window(all[-1])
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="certSelect"]/li[1]').click()
        # all=self.dr.window_handles
        self.dr.switch_to.window(all[0])
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame(iframe)
        self.dr.find_element_by_xpath('//*[@id="lkForm"]/div[1]/div[1]/div[2]/div[3]/div[2]/div/input').clear()
        self.dr.find_element_by_xpath('//*[@id="lkForm"]/div[1]/div[1]/div[2]/div[3]/div[2]/div/input').send_keys('HB3')
        self.dr.find_element_by_xpath('//*[@id="zjh"]').send_keys('216546454')
        self.dr.find_element_by_xpath('//*[@id="lxdz"]').clear()
        self.dr.find_element_by_xpath('//*[@id="lxdz"]').send_keys('湖北省武汉市洪山区')
        self.dr.find_element_by_xpath('//*[@id="lz"]').click()
        self.dr.find_element_by_xpath('//*[@id="countryContainer"]/ul/li[42]').click()
        self.dr.find_element_by_xpath('//*[@id="lkForm"]/div[1]/div[1]/div[2]/div[5]/div[2]/input').clear()
        self.dr.find_element_by_xpath('//*[@id="lkForm"]/div[1]/div[1]/div[2]/div[5]/div[2]/input').send_keys(
            '15263524152')
        # 物品信息
        self.dr.find_element_by_xpath('//*[@id="btnWpfl"]').click()
        all = self.dr.window_handles
        self.dr.switch_to.window(all[-1])
        self.dr.find_element_by_xpath('//*[@id="wpflSelect_1_switch"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="wpflSelect_2_span"]').click()
        time.sleep(2)
        all = self.dr.window_handles
        self.dr.switch_to.window(all[0])
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame(iframe)
        self.dr.find_element_by_xpath('//*[@id="zl"]').send_keys('10')
        self.dr.find_element_by_xpath('//*[@id="wpmc"]').send_keys('腊肠')
        self.dr.find_element_by_xpath('//*[@id="bz"]').send_keys('测试数据')
        self.dr.find_element_by_xpath('//*[@id="gldz"]').send_keys('宠物隔离中心')
        self.dr.find_element_by_xpath('//*[@id="cwbh"]').send_keys('654644')
        self.dr.find_element_by_xpath('//*[@id="jyzsh"]').send_keys('2654654')
        self.dr.find_element_by_xpath('//*[@id="ymzsh"]').send_keys('15646546')
        Select(self.dr.find_element_by_xpath('//*[@id="yt"]')).select_by_value('其他')
        time.sleep(2)
        files = r'E:\workspace\webcase\携带物2.0\images\宠物狗.jpg'
        file_owe=r'E:\workspace\webcase\携带物2.0\images\宠物运载工具消毒证.jpg'
        file_zyxlzm=r'E:\workspace\webcase\携带物2.0\images\宠物出入境备案.jpg'
        file_kqbbg=r'E:\workspace\webcase\携带物2.0\images\宠物检疫合格证.jpg'
        self.dr.find_element_by_xpath('//*[@id="wptp"]').send_keys(files)
        self.dr.find_element_by_xpath('//*[@id="syzzm"]').send_keys(file_owe)
        self.dr.find_element_by_xpath('//*[@id="zyxlzm"]').send_keys(file_kqbbg)
        self.dr.find_element_by_xpath('//*[@id="kqbkt"]').send_keys(file_zyxlzm)
        time.sleep(5)
        self.dr.find_element_by_xpath('//*[@id="btnGtj"]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="btnSave"]/span').click()
        # 确认操作提示框
        self.dr.find_element_by_xpath('/html/body/div[9]/div[3]/div/button[2]').click()
        self.dr.find_element_by_xpath('//*[@id="qtForm"]/table/tbody/tr[4]/td/div[2]/label[2]/input').click()
        self.dr.find_element_by_xpath('//*[@id="qtForm"]/table/tbody/tr[4]/td/div[2]/label[4]/input').click()
        self.dr.find_element_by_xpath('//*[@id="qtForm"]/table/tbody/tr[4]/td/div[2]/label[3]/input').click()
        self.dr.switch_to.default_content()
        time.sleep(2)
        self.dr.switch_to.frame(iframe)
        self.assertEqual('截留物单据打印', self.dr.find_element_by_xpath('/html/body/div/div/h3/span').text)
        global id,jld_id
        id = self.dr.find_element_by_xpath('//*[@id="list"]/tbody[1]/tr/td[3]').text
        jld_id=self.dr.find_element_by_xpath('//*[@id="jldbh"]').get_attribute('value')

    def test02_隔离检疫_处理_不合格退回(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.dr.find_element_by_xpath('//*[@id="964f6417a71c47728cfa785a96b5b6ca"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_964f6417a71c47728cfa785a96b5b6ca"]/iframe')
        self.dr.switch_to.frame(iframe)
        time.sleep(2)
        self.xdw_Isolation_and_Quarantine_Handle_Unqualified({'clfs':'退回'})

    def test03_隔离检疫_处理_不合格退回_审核(self):
        self.login_keyuan(login_name_user2,login_name_password2)
        self.dr.find_element_by_xpath('//*[@id="964f6417a71c47728cfa785a96b5b6ca"]/a/span').click()
        iframe = self.dr.find_element_by_xpath('//*[@id="sub_964f6417a71c47728cfa785a96b5b6ca"]/iframe')
        self.dr.switch_to.frame(iframe)
        self.xdw_Isolation_and_Quarantine_search({'status':'待审核'})
        self.xdw_Isolation_and_Quarantine_Handle_examine()

if __name__ == '__main__':
    unittest.main()