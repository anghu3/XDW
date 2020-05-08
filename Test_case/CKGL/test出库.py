from Setting.setting_file import xdw_TestCase
from Setting.cycl import cycl_TestCase
import unittest
import time
from Setting.setting_file import login_name_user1,login_name_password1,login_name_user4,login_name_password4,setting_xls
import random
from Setting.menu import data


class xdwcy_TestCase(xdw_TestCase,cycl_TestCase):

    def Initialization(self):
        self.dr.find_element_by_xpath('//*[@id="'+data['仓库管理']+'"]/a/span').click()
        self.dr.find_element_by_xpath('//*[@id="'+data['出库']+'"]/a/span').click()
        iframe=self.dr.find_element_by_xpath('//*[@id="sub_'+data['出库']+'"]/iframe')
        self.dr.switch_to.frame(iframe)
        time.sleep(1)
        js = "window.scrollTo(0, document.body.scrollHeight)"
        self.dr.execute_script(js)
        time.sleep(2)
        self.dr.find_element_by_xpath(
            '/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[2]/span/button').click()
        self.dr.find_element_by_xpath(
            '/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[2]/span/ul/li[1]/a').click()
        time.sleep(1)

    def test01_出库_正常出库_查询_物品编号(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'00000019110004101','wpmc':'','startTime':'','endTime':'','clff':'--全部--','ckjglx':'--全部--'}
        self.xdw_ck_normal_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['wpbh'],2,0)

    def test02_出库_正常出库_查询_名称(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'','wpmc':'芒果','startTime':'','endTime':'','clff':'--全部--','ckjglx':'--全部--'}
        self.xdw_ck_normal_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['wpmc'],4,0)

    def test03_出库_正常出库_查询_入库时间(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'','wpmc':'','startTime':'2019-11-12','endTime':'2019-11-12','clff':'--全部--','ckjglx':'--全部--'}
        self.xdw_ck_normal_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['startTime'],10,0)

    def test04_出库_正常出库_查询_截获方法(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        clffs=['--全部--','销毁','截留']
        for clff in clffs:
            if clff =='--全部--':
                pass
            else:
                search_value={'wpbh':'','wpmc':'','startTime':'','endTime':'','clff':clff,'ckjglx':'--全部--'}
                self.xdw_ck_normal_search(search_value)
                search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
                self.pagination_num(search_num,search_value['clff'],7,0)

    def test05_出库_正常出库_查询_出库类型(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        ckjglxs=['--全部--','销毁','截留','放行','移交保护部门','实验室检疫']
        for ckjglx in ckjglxs:
            if ckjglx =='--全部--':
                pass
            else:
                search_value={'wpbh':'','wpmc':'','startTime':'','endTime':'','clff':'--全部--','ckjglx':ckjglx}
                self.xdw_ck_normal_search(search_value)
                search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
                if ckjglx=='移交保护部门':
                    self.pagination_num(search_num, '移交动物保护部门', 8, 0)
                elif ckjglx=='实验室检疫':
                    self.pagination_num(search_num, '送样', 8, 0)
                else:
                    self.pagination_num(search_num,search_value['ckjglx'],8,0)

    def test06_出库_送检出库_查询_物品编号(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'00000019110004101','wpmc':'','startTime':'','endTime':'','clff':'--全部--','ckjglx':'--全部--'}
        self.xdw_ck_Inspection_search()
        self.xdw_ck_normal_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['wpbh'],2,0)

    def test07_出库_送检出库_查询_名称(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'','wpmc':'芒果','startTime':'','endTime':'','clff':'--全部--','ckjglx':'--全部--'}
        self.xdw_ck_Inspection_search()
        self.xdw_ck_normal_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['wpmc'],4,0)

    def test08_出库_送检出库_查询_入库时间(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'','wpmc':'','startTime':'2019-11-12','endTime':'2019-11-12','clff':'--全部--','ckjglx':'--全部--'}
        self.xdw_ck_Inspection_search()
        self.xdw_ck_normal_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['startTime'],10,0)

    def test09_出库_送检出库_查询_截获方法(self):
        self.login_keyuan(login_name_user1, login_name_password1)
        self.Initialization()
        self.xdw_ck_Inspection_search()
        clffs=['--全部--','销毁','截留']
        for clff in clffs:
            if clff =='--全部--':
                pass
            else:
                search_value={'wpbh':'','wpmc':'','startTime':'','endTime':'','clff':clff,'ckjglx':'--全部--'}
                self.xdw_ck_normal_search(search_value)
                search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
                self.pagination_num(search_num,search_value['clff'],7,0)

    def test10_出库_送检出库_查询_出库类型(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        self.xdw_ck_Inspection_search()
        ckjglxs=['--全部--','销毁','截留','放行','移交保护部门','实验室检疫']
        for ckjglx in ckjglxs:
            if ckjglx =='--全部--':
                pass
            else:
                search_value={'wpbh':'','wpmc':'','startTime':'','endTime':'','clff':'--全部--','ckjglx':ckjglx}
                self.xdw_ck_normal_search(search_value)
                search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
                if ckjglx=='移交保护部门':
                    self.pagination_num(search_num, '移交动物保护部门', 8, 0)
                elif ckjglx=='实验室检疫':
                    self.pagination_num(search_num, '送样', 8, 0)
                else:
                    self.pagination_num(search_num,search_value['ckjglx'],8,0)

    def test11_出库_特殊出库_查询_物品编号(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'00000019110004101','wpmc':'','startTime':'','endTime':'','clff':'--全部--','ckjglx':'--全部--'}
        self.xdw_ck_special_search()
        self.xdw_ck_normal_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['wpbh'],2,0)

    def test12_出库_特殊出库_查询_名称(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'','wpmc':'芒果','startTime':'','endTime':'','clff':'--全部--','ckjglx':'--全部--'}
        self.xdw_ck_special_search()
        self.xdw_ck_normal_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['wpmc'],4,0)

    def test13_出库_特殊出库_查询_入库时间(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        search_value={'wpbh':'','wpmc':'','startTime':'2019-11-12','endTime':'2019-11-12','clff':'--全部--','ckjglx':'--全部--'}
        self.xdw_ck_special_search()
        self.xdw_ck_normal_search(search_value)
        search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num,search_value['startTime'],10,0)

    def test14_出库_特殊出库_查询_截获方法(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        self.xdw_ck_special_search()
        clffs=['--全部--','销毁','截留']
        for clff in clffs:
            if clff =='--全部--':
                pass
            else:
                search_value={'wpbh':'','wpmc':'','startTime':'','endTime':'','clff':clff,'ckjglx':'--全部--'}
                self.xdw_ck_normal_search(search_value)
                search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
                self.pagination_num(search_num,search_value['clff'],7,0)

    def test15_出库_特殊出库_查询_出库类型(self):
        self.login_keyuan(login_name_user1,login_name_password1)
        self.Initialization()
        self.xdw_ck_special_search()
        ckjglxs=['--全部--','销毁','截留','放行','移交保护部门','实验室检疫']
        for ckjglx in ckjglxs:
            if ckjglx =='--全部--':
                pass
            else:
                search_value={'wpbh':'','wpmc':'','startTime':'','endTime':'','clff':'--全部--','ckjglx':ckjglx}
                self.xdw_ck_normal_search(search_value)
                search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
                if ckjglx=='移交保护部门':
                    self.pagination_num(search_num, '移交动物保护部门', 8, 0)
                elif ckjglx=='实验室检疫':
                    self.pagination_num(search_num, '送样', 8, 0)
                else:
                    self.pagination_num(search_num,search_value['ckjglx'],8,0)


    # def test16_出库_销毁出库(self):
    #     self.login_keyuan(login_name_user1, login_name_password1)
    #     test_num = random.randint(1, 10)
    #     self.xdw_Inspection_addition(test_num, '销毁', '')
    #     id = self.dr.find_element_by_xpath('//*[@id="list"]/tbody[1]/tr/td[3]').text
    #     jld_id = self.dr.find_element_by_xpath('//*[@id="jldbh"]').get_attribute('value')
    #     self.dr.switch_to.default_content()
    #     self.dr.find_element_by_xpath('//*[@id="f683e4f46b094a8ba68ad201a6e5b7bf"]/a/span').click()
    #     iframe = self.dr.find_element_by_xpath('//*[@id="sub_f683e4f46b094a8ba68ad201a6e5b7bf"]/iframe')
    #     self.dr.switch_to.frame(iframe)
    #     search_value = {'startTime': '', 'endTime': '', 'wpbh': id, 'wpmc': '', 'wplb': '--全部--', 'clff': '--全部--'}
    #     self.xdw_Onsite_transfer_or_storage_search(search_value)
    #     search_num = self.dr.find_element_by_xpath('//*[@id="3lists"]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
    #     self.pagination_num(search_num, search_value['wpbh'], 2, 1)
    #     self.xdw_Onsite_transfer_or_storage_print()
    #     self.xdw_Onsite_transfer_or_storage_storage()
    #     self.dr.switch_to.default_content()
    #     self.Initialization()
    #     search_value={'wpbh':id,'wpmc':'','startTime':'','endTime':'','clff':'--全部--','ckjglx':'--全部--'}
    #     self.xdw_ck_normal_search(search_value)
    #     search_num=self.dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/span[1]').text
    #     self.pagination_num(search_num,search_value['wpbh'],2,0)
    #     self.xdw_ck_normal_xhck()
    #     self.dr.switch_to.default_content()
    #     self.dr.find_element_by_xpath('//*[@id="dcefdfba1ea04e2db15876bd8673651d"]/a/span').click()
    #     self.dr.find_element_by_xpath('//*[@id="2de3690e1692476caa343748aa27c5ec"]/a/span').click()
    #     iframe = self.dr.find_element_by_xpath('//*[@id="sub_2de3690e1692476caa343748aa27c5ec"]/iframe')
    #     self.dr.switch_to.frame(iframe)
    #     self.dr.find_element_by_xpath('//*[@id="form"]/div/div/div[2]/input').send_keys(id)
    #     self.dr.find_element_by_xpath('//*[@id="search"]/span').click()
    #     time.sleep(2)
    #     self.assertEqual(id, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[3]').text)

if __name__ == '__main__':
    unittest.main()