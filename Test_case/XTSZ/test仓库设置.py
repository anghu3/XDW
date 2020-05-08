import time
import unittest
from Setting.setting_file import xdw_TestCase
from Setting.setting_file import login_name_user1, login_name_password1
from Setting.xtsz import xtsz_TestCase


class xdwcksz_TestCase(xdw_TestCase, xtsz_TestCase):

    # 进入仓库设置页面
    def initialization(self):
        # 登录
        self.login_keyuan(login_name_user1, login_name_password1)
        # 点击 系统设置-仓库设置 菜单
        self.dr.find_element_by_xpath('//*[@id="3d35b5cf016a4e7fa1595194364b41a3"]').click()
        self.dr.find_element_by_xpath('//*[@id="83b0feb8254f4ebd9f9df5b5b4d636fb"]').click()
        time.sleep(2)
        # 切换iframe
        iframe = self.dr.find_element_by_xpath('//*[@id="sub_83b0feb8254f4ebd9f9df5b5b4d636fb"]/iframe')
        self.dr.switch_to.frame(iframe)

    # 新增仓库设置
    def test01_仓库设置_新增(self):
        self.initialization()
        content_add = {'ckm': '淘宝仓库', 'js': '岳阳机场', 'ks': '一科'}
        self.cksz_add(content_add, '操作成功')

    # 新增仓库设置_已存在
    def test02_仓库设置_新增_已存在(self):
        self.initialization()
        content_add = {'ckm': '测试仓库', 'js': '武汉机场', 'ks': '综合科'}
        self.cksz_add(content_add, '该科室已经配置仓库')

    # 按仓库名查询仓库设置
    def test03_仓库设置_查询_仓库名(self):
        self.initialization()
        search_value = {'ckm': '淘宝仓库', 'js': '', 'ks': ''}
        self.cksz_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['ckm'], 2, 4)

    # 按局室查询仓库设置
    def test04_仓库设置_查询_局室(self):
        self.initialization()
        search_value = {'ckm': '', 'js': '岳阳机场', 'ks': ''}
        self.cksz_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['js'], 3, 4)

    # 按科室查询仓库设置
    def test05_仓库设置_查询_科室(self):
        self.initialization()
        search_value = {'ckm': '', 'js': '岳阳机场', 'ks': '一科'}
        self.cksz_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['ks'], 4, 4)

    # 组合查询仓库设置
    def test06_仓库设置_查询_组合查询(self):
        self.initialization()
        search_value = {'ckm': '淘宝仓库', 'js': '岳阳机场', 'ks': '一科'}
        self.cksz_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['ckm'], 2, 4)
        self.pagination_num(search_num, search_value['js'], 3, 4)
        self.pagination_num(search_num, search_value['ks'], 4, 4)

    # 编辑仓库设置
    def test07_仓库设置_编辑(self):
        self.initialization()
        # 查询仓库
        self.cksz_search({'ckm': '淘宝仓库', 'js': '', 'ks': ''})
        content_edit = {'ckm': '测试仓库', 'js': '', 'ks': '二科'}
        self.cksz_edit(content_edit)

    # 删除仓库设置
    def test08_仓库设置_删除(self):
        self.initialization()
        content_delete = {'ckm': '测试仓库', 'js': '', 'ks': ''}
        self.cksz_delete(content_delete)

    # 批量删除仓库设置
    def test09_仓库设置_批量删除(self):
        self.initialization()
        self.cksz_add({'ckm': '京东仓库A', 'js': '长沙机场', 'ks': '一科'}, '操作成功')
        time.sleep(0.5)
        self.cksz_add({'ckm': '京东仓库B', 'js': '长沙机场', 'ks': '二科'}, '操作成功')
        search_value = {'ckm': '', 'js': '长沙机场', 'ks': ''}
        self.cksz_search(search_value)
        self.cksz_batchdelete()


if __name__ == '__main__':
    unittest.main()