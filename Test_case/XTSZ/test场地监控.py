import time
import unittest
from Setting.setting_file import xdw_TestCase
from Setting.setting_file import login_name_user1, login_name_password1
from Setting.xtsz import xtsz_TestCase


class xdwcdjk_TestCase(xdw_TestCase, xtsz_TestCase):

    # 进入场地监控页面
    def initialization(self):
        # 登录
        self.login_keyuan(login_name_user1, login_name_password1)
        # 点击 系统设置-场地监控 菜单
        self.dr.find_element_by_xpath('//*[@id="3d35b5cf016a4e7fa1595194364b41a3"]').click()
        self.dr.find_element_by_xpath('//*[@id="c486d4d177dc4a02b6d997c5d9f4b20f"]').click()
        time.sleep(2)
        # 切换iframe
        iframe = self.dr.find_element_by_xpath('//*[@id="sub_c486d4d177dc4a02b6d997c5d9f4b20f"]/iframe')
        self.dr.switch_to.frame(iframe)

    # 新增场地监控
    def test01_场地监控_新增(self):
        self.initialization()
        content_add = {'cddm': 'CD1', 'cdmc': '入口1', 'sbid': [1, 3]}
        self.cdjk_add(content_add, '保存成功')

    # 新增场地监控_场地代码已存在
    def test02_场地监控_新增_场地代码已存在(self):
        self.initialization()
        content_add = {'cddm': 'CD1', 'cdmc': '入口1', 'sbid': [1]}
        self.cdjk_add(content_add, '该场地代码已存在')

    # 按场地代码查询场地监控
    def test03_场地监控_查询_场地代码(self):
        self.initialization()
        search_value = {'cddm': 'CD1', 'cdmc': ''}
        self.cdjk_search(search_value)
        search_num = self.dr.find_element_by_xpath('/html/body/div/div/div[3]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['cddm'], 2, 2)

    # 按场地名称查询场地监控
    def test04_场地监控_查询_场地名称(self):
        self.initialization()
        search_value = {'cddm': '', 'cdmc': '入口1'}
        self.cdjk_search(search_value)
        search_num = self.dr.find_element_by_xpath('/html/body/div/div/div[3]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['cdmc'], 3, 2)

    # 组合查询场地监控
    def test05_场地监控_查询_组合查询(self):
        self.initialization()
        search_value = {'cddm': 'CD1', 'cdmc': '入口1'}
        self.cdjk_search(search_value)
        search_num = self.dr.find_element_by_xpath('/html/body/div/div/div[3]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['cddm'], 2, 2)
        self.pagination_num(search_num, search_value['cdmc'], 3, 2)

    # 编辑场地监控
    def test06_场地监控_编辑(self):
        self.initialization()
        self.cdjk_search({'cddm': 'CD1', 'cdmc': ''})
        content_edit = {'cddm': 'CD1', 'cdmc': '入口test', 'sbid': [2, 4]}
        self.cdjk_edit(content_edit)

    # 删除场地监控
    def test07_场地监控_删除(self):
        self.initialization()
        self.cdjk_search({'cddm': 'CD1', 'cdmc': ''})
        self.cdjk_delete()

    # 批量删除场地监控
    def test08_场地监控_批量删除(self):
        self.initialization()
        content_add1 = {'cddm': 'CDtest1', 'cdmc': '出口', 'sbid': [4]}
        self.cdjk_add(content_add1, '保存成功')
        # 按钮位置变化
        # time.sleep(1)
        # content_add2 = {'cddm': 'CDtest2', 'cdmc': '出口', 'sbid': [1, 5]}
        # self.cdjk_add(content_add2, '保存成功')
        self.cdjk_search({'cddm': '', 'cdmc': '出口'})
        self.cdjk_batchdelete()


if __name__ == '__main__':
    unittest.main()