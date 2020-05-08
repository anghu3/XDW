import time
import unittest

from Setting.setting_file import login_name_user1, login_name_password1
from Setting.xtsz import xtsz_TestCase


class xdwyqgj_TestCase(xtsz_TestCase):

    # 进入疫情国家页面
    def initialization(self):
        # 登录
        self.login_keyuan(login_name_user1, login_name_password1)
        # 点击 系统设置-疫情国家 菜单
        self.dr.find_element_by_xpath('//*[@id="2038c5adbb464175b53544582b3c72ef"]').click()
        self.dr.find_element_by_xpath('//*[@id="a008b43499be43118118683cea2afeb7"]/a').click()

        time.sleep(2)
        # 切换iframe
        iframe = self.dr.find_element_by_xpath('//*[@id="sub_a008b43499be43118118683cea2afeb7"]/iframe')
        self.dr.switch_to.frame(iframe)

    def test01_疫情国家_新增(self):
        self.initialization()
        self.yqgj_add('肺鼠疫', '中国', '操作成功')

    def test02_疫情国家_新增_疫情名称已存在(self):
        self.initialization()
        self.yqgj_add('肺鼠疫', '中国', '疫情名称已存在')

    def test03_疫情国家_查询_疫情名称(self):
        self.initialization()
        self.yqgj_search('肺鼠疫', '')

    def test04_疫情国家_查询_疫情国家(self):
        self.initialization()
        self.yqgj_search('', '中国')

    def test05_疫情国家_查询_组合查询(self):
        self.initialization()
        self.yqgj_search('肺鼠疫', '中国')

    def test06_疫情国家_编辑(self):
        self.initialization()
        self.yqgj_edit()

    def test07_疫情国家_删除(self):
        self.initialization()
        self.yqgj_delete()

    def test08_疫情国家_批量删除(self):
        self.initialization()
        self.yqgj_batchdelete()


if __name__ == '__main__':
    unittest.main()