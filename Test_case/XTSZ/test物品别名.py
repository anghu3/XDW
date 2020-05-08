import time
import unittest
from Setting.setting_file import xdw_TestCase
from Setting.setting_file import login_name_user1, login_name_password1
from Setting.xtsz import xtsz_TestCase


class xdwwpbm_TestCase(xdw_TestCase, xtsz_TestCase):

    # 进入物品别名页面
    def initialization(self):
        # 登录
        self.login_keyuan(login_name_user1, login_name_password1)
        # 点击 系统设置-物品别名 菜单
        self.dr.find_element_by_xpath('//*[@id="3d35b5cf016a4e7fa1595194364b41a3"]').click()
        self.dr.find_element_by_xpath('//*[@id="36cb6815b6484001a160cb27706194b5"]').click()
        time.sleep(2)
        # 切换iframe
        iframe = self.dr.find_element_by_xpath('//*[@id="sub_36cb6815b6484001a160cb27706194b5"]/iframe')
        self.dr.switch_to.frame(iframe)

    # 新增物品别名
    # def test01_物品别名_新增(self):
    #     self.initialization()
    #     self.wpbm_add('树莓', '小树莓', '操作成功')
    #
    # # 新增物品别名_别名重复
    # def test02_物品别名_新增_别名重复(self):
    #     self.initialization()
    #     self.wpbm_add('树莓', '小树莓', '物品别名重复')
    #
    # # 按物品学名查询
    # def test03_物品别名_查询_物品学名(self):
    #     self.initialization()
    #     search_value = {'wpxm': '树莓', 'bm': '', 'zt': '', 'sfczcywp': ''}
    #     self.wpbm_search(search_value)
    #     search_num = self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
    #     self.pagination_num(search_num, search_value['wpxm'], 2, 4)
    #
    # # 按别名查询
    # def test04_物品别名_查询_别名(self):
    #     self.initialization()
    #     search_value = {'wpxm': '', 'bm': '小树莓', 'zt': '', 'sfczcywp': ''}
    #     self.wpbm_search(search_value)
    #     search_num = self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
    #     self.pagination_num(search_num, search_value['bm'], 3, 4)
    #
    # # 按状态查询
    # def test05_物品别名_查询_状态(self):
    #     self.initialization()
    #     search_value = {'wpxm': '', 'bm': '', 'zt': '确定', 'sfczcywp': ''}
    #     self.wpbm_search(search_value)
    #
    # # 按是否已存在常用物品中查询
    # def test06_物品别名_查询_是否已存在常用物品中(self):
    #     self.initialization()
    #     search_value = {'wpxm': '', 'bm': '', 'zt': '', 'sfczcywp': '是'}
    #     self.wpbm_search(search_value)
    #
    # # 组合查询
    # def test07_物品别名_查询_组合查询(self):
    #     self.initialization()
    #     search_value = {'wpxm': '树莓', 'bm': '小树莓', 'zt': '确定', 'sfczcywp': '是'}
    #     self.wpbm_search(search_value)
    #     search_num = self.dr.find_element_by_xpath('//*[@id="tbList"]/div/div[1]/div/div[4]/div[1]/span[1]').text
    #     self.pagination_num(search_num, search_value['wpxm'], 2, 4)
    #     self.pagination_num(search_num, search_value['bm'], 3, 4)
    #
    # # 编辑物品别名
    # def test08_物品别名_编辑(self):
    #     self.initialization()
    #     self.wpbm_edit()
    #
    # # 删除物品别名
    # def test09_物品别名_删除(self):
    #     self.initialization()
    #     self.wpbm_delete()
    #
    # # 批量删除物品别名
    # def test10_物品别名_批量删除(self):
    #     self.initialization()
    #     self.wpbm_batchdelete()

    # 合并物品别名
    def test11_物品别名_合并(self):
        self.initialization()
        self.wpbm_merge()



if __name__ == '__main__':
    unittest.main()