import time
import unittest
from Setting.setting_file import xdw_TestCase
from Setting.setting_file import login_name_user1, login_name_password1
from Setting.xtsz import xtsz_TestCase


class xdwcywpfl_TestCase(xdw_TestCase, xtsz_TestCase):

    # 进入常用物品分类页面
    def initialization(self):
        # 登录
        self.login_keyuan(login_name_user1, login_name_password1)
        # 点击 系统设置-常用物品分类 菜单
        self.dr.find_element_by_xpath('//*[@id="3d35b5cf016a4e7fa1595194364b41a3"]').click()
        self.dr.find_element_by_xpath('//*[@id="6b1a6b979ced45188142988ecd4b77ce"]').click()
        time.sleep(2)
        # 切换iframe
        iframe = self.dr.find_element_by_xpath('//*[@id="sub_6b1a6b979ced45188142988ecd4b77ce"]/iframe')
        self.dr.switch_to.frame(iframe)

    # 新增常用物品分类
    def test01_常用物品分类_新增(self):
        self.initialization()
        content_add = {'fldm': 993, 'flmc': '子类c', 'sjflid': [27]}
        self.cywpfl_add(content_add, '操作成功')

    # 新增常用物品分类_已存在
    def test02_常用物品分类_新增_已存在(self):
        self.initialization()
        content_add = {'fldm': 993, 'flmc': '子类c', 'sjflid': [27]}
        self.cywpfl_add(content_add, '已存在相同的分类代码')

    # 编辑常用物品分类
    def test03_常用物品分类_编辑(self):
        self.initialization()
        content_edit = {'flmc': '子类cedit', 'flid': [99, 993]}
        self.cywpfl_edit(content_edit)

    # 删除常用物品分类
    def test04_常用物品分类_删除(self):
        self.initialization()
        idlist = [99, 993]
        self.cywpfl_delete(idlist)

    # 批量删除常用物品分类
    def test05_常用物品分类_批量删除(self):
        self.initialization()
        # 新增
        content_add1 = {'fldm': 9911, 'flmc': '子类AA', 'sjflid': [27, 28]}
        self.cywpfl_add(content_add1, '操作成功')
        time.sleep(0.5)
        content_add1 = {'fldm': 9912, 'flmc': '子类AB', 'sjflid': [27, 28]}
        self.cywpfl_add(content_add1, '操作成功')
        idlist = [[99, 991, 9911], [99, 991, 9912]]
        self.cywpfl_batchdelete(idlist)


if __name__ == '__main__':
    unittest.main()