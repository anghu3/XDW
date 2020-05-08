import time
import unittest

from Setting.setting_file import login_name_user1, login_name_password1
from Setting.xtsz import xtsz_TestCase


class xdwcywp_TestCase(xtsz_TestCase):
    # 进入常用物品页面
    def initialization(self):
        # 登录
        self.login_keyuan(login_name_user1, login_name_password1)
        # 点击 系统设置-常用物品 菜单
        self.dr.find_element_by_xpath('//*[@id="3d35b5cf016a4e7fa1595194364b41a3"]').click()
        self.dr.find_element_by_xpath('//*[@id="f42e66a89a194ccfb14e039faa59db5d"]').click()
        time.sleep(2)
        # 切换iframe
        iframe = self.dr.find_element_by_xpath('//*[@id="sub_f42e66a89a194ccfb14e039faa59db5d"]/iframe')
        self.dr.switch_to.frame(iframe)

    # 新增物品
    def test01_常用物品_新增(self):
        self.initialization()
        self.cywp_add('测试物品', 11, 12, '操作成功')

    # 新增物品_已存在
    def test02_常用物品_新增_已存在(self):
        self.initialization()
        self.cywp_add('测试物品', 11, 12, '已存在相同的物品名称')

    # 按物品名称查询
    def test03_常用物品_查询_名称(self):
        self.initialization()
        self.cywp_search('测试物品', '', '', '')

    # 按物品拼音查询
    def test04_常用物品_查询_拼音(self):
        self.initialization()
        self.cywp_search('', 'ceshiwupin', '', '')

    # 按物品首字母查询
    def test05_常用物品_查询_首字母(self):
        self.initialization()
        self.cywp_search('', '', 'cswp', '')

    # 按物品分类查询
    def test06_常用物品_查询_物品分类(self):
        self.initialization()
        self.cywp_search('', '', '', '新鲜水果', 11, 12)

    # 组合查询
    def test07_常用物品_查询_组合查询(self):
        self.initialization()
        self.cywp_search('测试物品', 'ceshiwupin', 'cswp', '新鲜水果', 11, 12)

    # 编辑物品
    def test08_常用物品_编辑(self):
        self.initialization()
        self.cywp_edit()

    # 删除物品
    def test09_常用物品_删除(self):
        self.initialization()
        self.cywp_delete()

    # 批量删除物品
    def test10_常用物品_批量删除(self):
        self.initialization()
        self.cywp_batchdelete()


if __name__=='__main__':
    unittest.main()
