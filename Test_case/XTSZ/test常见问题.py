import time
import unittest
from Setting.setting_file import xdw_TestCase
from Setting.setting_file import login_name_user1, login_name_password1
from Setting.xtsz import xtsz_TestCase


class xdwcjwt_TestCase(xdw_TestCase, xtsz_TestCase):

    # 进入常见问题页面
    def initialization(self):
        # 登录
        self.login_keyuan(login_name_user1, login_name_password1)
        # 点击 系统设置-常见问题 菜单
        self.dr.find_element_by_xpath('//*[@id="navbar-container"]/div[2]/ul/li[1]/a').click()
        time.sleep(2)
        # 切换iframe
        iframe = self.dr.find_element_by_xpath('//*[@id="cjwt"]/iframe')
        self.dr.switch_to.frame(iframe)

    # 新增常见问题
    def test01_常见问题_新增(self):
        self.initialization()
        content_add = {'lx': '系统操作问题', 'wt': '系统如何使用', 'jd': '请查看操作手册'}
        self.cjwt_add(content_add)

    # 按类型查询常见问题
    def test02_常见问题_查询_类型(self):
        self.initialization()
        types = [' 全部', '设备问题', '系统操作问题']
        for type in types:
            search_value = {'lx': type, 'wt': '', 'jd': ''}
            self.cjwt_search(search_value)
            if type == ' 全部':
                pass
            else:
                search_num = self.dr.find_element_by_xpath('//*[@id="pagetiptable"]/h6').text
                # //*[@id="pageControltable"]/li[5]/a
                self.pagination_num(search_num, search_value['lx'], 1, 10)

    # 按问题查询常见问题
    def test03_常见问题_查询_问题(self):
        self.initialization()
        search_value = {'lx': '', 'wt': '系统如何使用', 'jd': ''}
        self.cjwt_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="pagetiptable"]/h6').text
        self.pagination_num(search_num, search_value['wt'], 2, 10)

    # 按解答查询常见问题
    def test04_常见问题_查询_解答(self):
        self.initialization()
        search_value = {'lx': '', 'wt': '', 'jd': '请查看操作手册'}
        self.cjwt_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="pagetiptable"]/h6').text
        self.pagination_num(search_num, search_value['jd'], 3, 10)

    # 组合查询常见问题
    def test05_常见问题_查询_组合查询(self):
        self.initialization()
        search_value = {'lx': '系统操作问题', 'wt': '系统如何使用', 'jd': '请查看操作手册'}
        self.cjwt_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="pagetiptable"]/h6').text
        print(search_num)
        self.pagination_num(search_num, search_value['lx'], 1, 10)
        self.pagination_num(search_num, search_value['wt'], 2, 10)
        self.pagination_num(search_num, search_value['jd'], 3, 10)

    # 常见问题详情
    def test06_常见问题_查看详情(self):
        self.initialization()
        search_value = {'lx': '系统操作问题', 'wt': '系统如何使用', 'jd': '请查看操作手册'}
        self.cjwt_search(search_value)
        self.cjwt_detail(search_value)

    # 编辑常见问题
    def test07_常见问题_编辑(self):
        self.initialization()
        search_value = {'lx': '', 'wt': '系统如何使用', 'jd': ''}
        self.cjwt_search(search_value)
        content_edit = {'lx': '设备问题', 'wt': '通道设备报警', 'jd': '有闯入情况'}
        self.cjwt_edit(content_edit)

    # 删除常见问题
    def test08_常见问题_删除(self):
        self.initialization()
        search_value = {'lx': '', 'wt': '通道设备报警', 'jd': ''}
        self.cjwt_search(search_value)
        self.cjwt_delete()

    # 批量删除常见问题
    def test09_常见问题_批量删除(self):
        self.initialization()
        content_add1 = {'lx': '设备问题', 'wt': '常见问题测试', 'jd': '常见问题解答11'}
        self.cjwt_add(content_add1)
        time.sleep(1)
        content_add2 = {'lx': '系统操作问题', 'wt': '常见问题测试', 'jd': '常见问题解答22'}
        self.cjwt_add(content_add2)
        search_value = {'lx': '', 'wt': '常见问题测试', 'jd': ''}
        self.cjwt_search(search_value)
        self.cjwt_batchdelete()


if __name__ == '__main__':
    unittest.main()