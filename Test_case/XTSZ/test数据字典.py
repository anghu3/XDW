import time
import unittest
from Setting.setting_file import xdw_TestCase
from Setting.setting_file import login_name_user1, login_name_password1
from Setting.xtsz import xtsz_TestCase


class xdwsjzd_TestCase(xdw_TestCase, xtsz_TestCase):

    # 进入数据字典页面
    def initialization(self):
        # 登录
        self.login_keyuan(login_name_user1, login_name_password1)
        # 点击 系统设置-仓库设置 菜单
        self.dr.find_element_by_xpath('//*[@id="2038c5adbb464175b53544582b3c72ef"]').click()
        self.dr.find_element_by_xpath('//*[@id="241ff49b810f4df2b5c31ebc810b9208"]').click()
        time.sleep(2)
        # 切换iframe
        iframe = self.dr.find_element_by_xpath('//*[@id="sub_241ff49b810f4df2b5c31ebc810b9208"]/iframe')
        self.dr.switch_to.frame(iframe)

    新增字典类别
    def test01_数据字典_新增字典类别(self):
        self.initialization()
        content_add = {'lxdm': 'test', 'lxmc': '测试', 'bz': '哈哈'}
        self.sjzd_category_add(content_add, '操作成功')

    # 新增字典类别_已存在相同的类型代码
    def test02_数据字典_新增字典类别_已存在相同的类型代码(self):
        self.initialization()
        content_add = {'lxdm': 'test', 'lxmc': '测试ing', 'bz': '哈哈ing'}
        self.sjzd_category_add(content_add, '已存在相同的类型代码')

    # 编辑字典类别
    def test03_数据字典_编辑字典类别(self):
        self.initialization()
        content_edit = {'lxmc_old': '测试', 'lxmc_new': '测试ing', 'bz': '哈哈ing'}
        self.sjzd_category_edit(content_edit)

    # 添加字典子项
    def test04_数据字典_添加字典子项(self):
        self.initialization()
        self.enter_category('测试ing')
        content_add = {'zddm': 'AA', 'zdmc': '测试ing', 'syzt': '启用', 'sska': '武汉机场', 'bz': '哈哈ing'}
        self.sjzd_add(content_add, '操作成功')

    # 添加字典子项_已存在相同的字典代码
    def test05_数据字典_添加字典子项_已存在相同的字典代码(self):
        self.initialization()
        self.enter_category('测试ing')
        content_add = {'zddm': 'AA', 'zdmc': '测试ing', 'syzt': '启用', 'sska': '武汉机场', 'bz': '哈哈ing'}
        self.sjzd_add(content_add, '已存在相同的字典代码')

    # 按字典代码查询字典子项
    def test06_数据字典_查询字典子项_字典代码(self):
        self.initialization()
        self.enter_category('测试ing')
        search_value = {'zddm': 'AA', 'zdmc': '', 'bz': ''}
        self.sjzd_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['zddm'], 2, 4)

    # 按字典名称查询字典子项
    def test07_数据字典_查询字典子项_字典名称(self):
        self.initialization()
        self.enter_category('测试ing')
        search_value = {'zddm': '', 'zdmc': '测试ing', 'bz': ''}
        self.sjzd_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['zdmc'], 3, 4)

    # 按备注查询字典子项
    def test08_数据字典_查询字典子项_备注(self):
        self.initialization()
        self.enter_category('测试ing')
        search_value = {'zddm': '', 'zdmc': '', 'bz': '哈哈ing'}
        self.sjzd_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['bz'], 6, 4)

    # 查询字典子项_组合查询
    def test09_数据字典_查询字典子项_组合查询(self):
        self.initialization()
        self.enter_category('测试ing')
        search_value = {'zddm': 'AA', 'zdmc': '测试ing', 'bz': '哈哈ing'}
        self.sjzd_search(search_value)
        search_num = self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
        self.pagination_num(search_num, search_value['zddm'], 2, 4)
        self.pagination_num(search_num, search_value['zdmc'], 3, 4)
        self.pagination_num(search_num, search_value['bz'], 6, 4)

    # 编辑字典子项
    def test10_数据字典_编辑字典子项(self):
        self.initialization()
        self.enter_category('测试ing')
        self.sjzd_search({'zddm': 'AA', 'zdmc': '', 'bz': ''})
        content_edit = {'zddm': 'AA', 'zdmc': '测试AA', 'syzt': '禁用', 'sska': '岳阳机场', 'bz': '编辑'}
        self.sjzd_edit(content_edit)

    删除字典子项
    def test11_数据字典_删除字典子项(self):
        self.initialization()
        self.enter_category('测试ing')
        # 按字典代码查询
        self.sjzd_search({'zddm': 'AA', 'zdmc': '', 'bz': ''})
        # 删除
        self.sjzd_delete()

    # 批量删除字典子项
    def test12_数据字典_批量删除字典子项(self):
        self.initialization()
        self.enter_category('测试ing')
        content_add1 = {'zddm': 'BB', 'zdmc': '测试BB', 'syzt': '启用', 'sska': '武汉机场', 'bz': '哈哈'}
        self.sjzd_add(content_add1, '操作成功')
        time.sleep(1)
        content_add2 = {'zddm': 'CC', 'zdmc': '测试CC', 'syzt': '启用', 'sska': '武汉机场', 'bz': '哈哈'}
        self.sjzd_add(content_add2, '操作成功')
        time.sleep(1)
        content_add3 = {'zddm': 'DD', 'zdmc': '测试DD', 'syzt': '禁用', 'sska': '武汉机场', 'bz': '哈哈'}
        self.sjzd_add(content_add3, '操作成功')
        # content_delete = {'zddm': ['BB', 'DD']}
        # self.sjzd_delete(content_delete)
        # 按备注查询
        self.sjzd_search({'zddm': '', 'zdmc': '', 'bz': '哈哈'})
        # 批量删除
        self.sjzd_batchdelete()

    删除字典类别
    def test13_数据字典_删除字典类别(self):
        self.initialization()
        content_delete = {'lxmc': '测试ing'}
        self.sjzd_category_delete(content_delete)


if __name__ == '__main__':
    unittest.main()