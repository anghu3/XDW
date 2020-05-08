import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

from Setting.setting_file import url


class xtsz_TestCase(unittest.TestCase):
    def setUp(self):
        # 打开Chrome浏览器
        self.dr = webdriver.Chrome()
        # 最大化google浏览器窗口
        self.dr.maximize_window()

    def tearDown(self):
        # 关闭浏览器
        self.dr.quit()

    # @classmethod
    # def setUpClass(cls):
    #     # cls.dr=webdriver.Ie()
    #     cls.dr=webdriver.Chrome()
    #     cls.dr.maximize_window()
    #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.dr.quit()

    def login_keyuan(self, user, password):
        # 跳转到指定的链接
        self.dr.get(url)
        # 输入用户名
        self.dr.find_element_by_xpath('//*[@id="username"]').send_keys(user)
        # 输入密码
        self.dr.find_element_by_xpath('//*[@id="password"]').send_keys(password)
        # 登陆
        self.dr.find_element_by_xpath('//*[@id="tijiao"]').click()
        time.sleep(2)
        # 校验同组人员弹框来判断登陆是否正常和员工登陆时选择同组人员弹框是否会自动弹出
        self.assertEqual('选择同组人员',self.dr.find_element_by_xpath('//*[@id="selectTzry"]').text)
        # self.dr.find_element_by_xpath('//*[@id="selectTzry"]').click()
        time.sleep(1)
        Select(self.dr.find_element_by_xpath('//*[@id="tzryms2side__sx"]')).select_by_value('koujun')
        self.dr.find_element_by_xpath('//*[@id="tzryForm"]/div[1]/div/div[2]/p[1]').click()
        self.dr.find_element_by_xpath('/html/body/div[9]/div[3]/div/button[2]').click()
        time.sleep(2)
        self.assertIn('同组人员', self.dr.find_element_by_xpath('//*[@id="navSearch"]').text)

    # 系统设置-常用物品页面，添加常用物品
    def cywp_add(self, wpmc, wpfl_p_id, wpfl_l_id, msg):
        # 打开添加框
        self.dr.find_element_by_xpath('//*[@id="add"]').click()
        time.sleep(0.5)
        # 填入物品名称
        self.dr.find_element_by_xpath('//*[@id="mc"]').send_keys(wpmc)
        # 选择物品分类，先点击树的一级节点，再点击二级节点
        self.dr.find_element_by_xpath('//*[@id="pname"]').click()
        self.dr.find_element_by_xpath('//*[@id="treeSelect_' + str(wpfl_p_id) + '_switch"]').click()
        self.dr.find_element_by_xpath('//*[@id="treeSelect_' + str(wpfl_l_id) + '_a"]').click()
        # 点击确定按钮
        # time.sleep(0.5)
        self.dr.execute_script("arguments[0].click();",
                               self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]'))
        # self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]').click()
        # 验证添加成功
        # time.sleep(0.5)
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        # 验证添加成功
        self.assertIn(msg, self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 系统设置-常用物品页面，常用物品查询
    def cywp_search(self, mc, py, szm, wpfl, wpfl_p_id=0, wpfl_l_id=0):
        # 输入物品名称
        self.dr.find_element_by_xpath('//*[@id="form"]/div/div[1]/input').send_keys(mc)
        # 输入物品拼音
        self.dr.find_element_by_xpath('//*[@id="form"]/div/div[2]/input').send_keys(py)
        # 输入物品首字母
        self.dr.find_element_by_xpath('//*[@id="form"]/div/div[3]/input').send_keys(szm)
        if wpfl != '' and wpfl_p_id != 0 and wpfl_l_id != 0:
            # 选择物品分类
            self.dr.find_element_by_xpath('//*[@id="name"]').click()

            self.dr.find_element_by_xpath('//*[@id="indexTreeSelect_' + str(wpfl_p_id) + '_switch"]').click()
            self.dr.find_element_by_xpath('//*[@id="indexTreeSelect_' + str(wpfl_l_id) + '_a"]').click()
        # 点击搜索按钮
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(1)
        # 验证查询成功
        if mc != '':
            self.assertIn(mc, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[2]').text)
        if py != '':
            self.assertIn(py, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text)
        if szm != '':
            self.assertIn(szm, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]').text)
        if wpfl != '' and wpfl_p_id != 0 and wpfl_l_id != 0:
            self.assertIn(wpfl, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[5]').text)

    # 系统设置-常用物品页面，编辑常用物品
    def cywp_edit(self):
        self.cywp_search('测试物品', '', '', '')
        # 点击编辑按钮
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[7]/div/button[2]').click()
        time.sleep(1)
        # 修改物品名称
        self.dr.find_element_by_xpath('//*[@id="mc"]').send_keys('测试')
        # 修改物品分类
        self.dr.find_element_by_xpath('//*[@id="pname"]').click()
        # self.dr.find_element_by_xpath('//*[@id="treeSelect_1_switch"]').click()
        self.dr.find_element_by_xpath('//*[@id="treeSelect_1_a"]').click()
        time.sleep(0.2)
        # 点击确定按钮
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]').click()
        # 验证编辑成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        tipEle = self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p')
        self.assertIn('操作成功', tipEle.text)

    # 系统设置-常用物品页面，删除单个常用物品
    def cywp_delete(self):
        self.cywp_search('测试物品', '', '', '')
        # 点击删除按钮
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[7]/div/button[1]').click()
        self.dr.find_element_by_xpath('/html/body/div[4]/div[3]/div/button[2]').click()

        # 验证删除成功
        # time.sleep(0.5)
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        tipEle = self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p')
        self.assertIn('删除成功', tipEle.text)

    # 系统设置-常用物品页面，批量删除多个常用物品
    def cywp_batchdelete(self):
        self.cywp_add('测试物品1', 11, 12, '操作成功')
        time.sleep(0.5)
        self.cywp_add('测试物品2', 11, 12, '操作成功')
        self.cywp_search('', '', '', '新鲜水果', 11, 12)
        time.sleep(1)
        # 勾选全选
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        # 点击批量删除按钮
        self.dr.find_element_by_xpath('//*[@id="delete"]').click()
        # BUG
        # self.dr.find_element_by_xpath('/html/body/div[4]/div[3]/div/button[2]').click()
        #
        # # 验证删除成功
        # # time.sleep(0.5)
        # WebDriverWait(self.dr, 5, 0.2).until(
        #     expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        # tipEle = self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p')
        # self.assertIn('删除成功', tipEle.text)

    # 系统设置-疫情国家页面，添加疫情国家
    def yqgj_add(self, yqmc, yqgj, msg):
        # 点击添加按钮
        self.dr.find_element_by_xpath('//*[@id="btnAdd"]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'yqgjms2side__sx')))
        # 输入疫情名称
        self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[1]/td/input').send_keys(yqmc)
        # 输入待选区国家进行搜索
        self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[2]/td/div/div[1]/div/input').send_keys(yqgj)
        time.sleep(0.5)
        # 验证搜索
        optionEles = self.dr.find_elements_by_xpath('//*[@id="yqgjms2side__sx"]/option')
        for oe in optionEles:
            self.assertNotEqual(oe.text.find(yqgj), -1)
        # 将待选区添加到已选区
        self.dr.find_element_by_xpath('//*[@id="yqgjms2side__sx"]/option[1]').click()
        self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[2]/td/div/div[2]/p[1]').click()
        # 点击确定按钮
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]').click()
        # 验证添加成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn(msg, self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 系统设置-疫情国家页面，查询疫情国家
    def yqgj_search(self, yqmc, yqgj):
        # 输入疫情名称
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/input').send_keys(yqmc)
        # 输入疫情国家
        self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/input').send_keys(yqgj)
        # 点击搜索按钮
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(1)
        # 验证查询成功
        self.assertIn(yqmc, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[2]').text)
        self.assertIn(yqgj, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text)

    # 系统设置-疫情国家页面，编辑疫情国家
    def yqgj_edit(self):
        # 查询
        self.yqgj_search('肺鼠疫', '')
        # 点击编辑按钮
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]/div/button[2]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'yqgjms2side__sx')))
        # time.sleep(0.2)
        # 修改疫情名称、国家
        self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[1]/td/input').send_keys('测试')
        self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[2]/td/div/div[1]/div/input').send_keys('毛里求斯')
        time.sleep(0.5)
        # 验证搜索
        optionEles = self.dr.find_elements_by_xpath('//*[@id="yqgjms2side__sx"]/option')
        for oe in optionEles:
            self.assertNotEqual(oe.text.find('毛里求斯'), -1)
        # 将待选区添加到已选区
        self.dr.find_element_by_xpath('//*[@id="yqgjms2side__sx"]/option[1]').click()
        self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[2]/td/div/div[2]/p[1]').click()
        # 点击确定按钮
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]').click()
        # 验证编辑成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn('操作成功',
                         self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 系统设置-疫情国家页面，删除单个疫情国家
    def yqgj_delete(self):
        # 查询
        self.yqgj_search('肺鼠疫', '')
        # 点击删除按钮
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]/div/button[1]').click()
        self.dr.find_element_by_xpath('/html/body/div[4]/div[3]/div/button[2]').click()
        # 验证删除成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn('删除成功',
                         self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 系统设置-疫情国家页面，批量删除多个疫情国家
    def yqgj_batchdelete(self):
        # 新增
        self.yqgj_add('疫情1', '韩国', '操作成功')
        time.sleep(0.5)
        self.yqgj_add('疫情2', '日本', '操作成功')
        # 查询
        self.yqgj_search('疫情', '')
        time.sleep(1)
        # 点击全选按钮
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        # 点击删除按钮
        self.dr.find_element_by_xpath('//*[@id="btnDelete"]').click()
        self.dr.find_element_by_xpath('/html/body/div[4]/div[3]/div/button[2]').click()
        # 验证删除成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn('删除成功',
                         self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 系统设置-物品别名页面，添加物品别名
    def wpbm_add(self, wpxm, bm, msg):
        # 点击新增按钮
        self.dr.find_element_by_xpath('//*[@id="btnAdd"]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'chosen_chosen')))
        # 点击物品学名框
        self.dr.find_element_by_xpath('//*[@id="chosen_chosen"]').click()
        # 搜索物品学名
        self.dr.find_element_by_xpath('//*[@id="chosen_chosen"]/div/div/input').send_keys(wpxm)
        # 验证搜索正确
        wpxmEle = self.dr.find_element_by_xpath('//*[@id="chosen_chosen"]/div/ul/li/em')
        self.assertEqual(wpxm, wpxmEle.text)
        # 点击搜索结果
        wpxmEle.click()
        # 输入别名
        self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[2]/td/input').send_keys(bm)
        time.sleep(0.2)
        # 点击确定按钮
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]').click()
        # 验证添加成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn(msg,
                      self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 系统设置-物品别名页面，查询物品别名
    def wpbm_search(self, search_value):
        # 输入查询条件
        self.dr.find_element_by_xpath('//*[@id="gfmc"]').clear()
        self.dr.find_element_by_xpath('//*[@id="gfmc"]').send_keys(search_value['wpxm'])
        self.dr.find_element_by_xpath('//*[@id="bm"]').clear()
        self.dr.find_element_by_xpath('//*[@id="bm"]').send_keys(search_value['bm'])
        if search_value['zt'] != '':
            Select(self.dr.find_element_by_xpath('//*[@id="zt"]')).select_by_visible_text(search_value['zt'])
        if search_value['sfczcywp'] != '':
            Select(self.dr.find_element_by_xpath('//*[@id="mc"]')).select_by_visible_text(search_value['sfczcywp'])
        # 点击搜索按钮
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(0.5)

    # 系统设置-物品别名页面，编辑物品别名
    def wpbm_edit(self):
        # 按物品学名查询
        self.wpbm_search({'wpxm': '树莓', 'bm': '', 'zt': '', 'sfczcywp': ''})
        # 点击编辑按钮
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]/div/button[2]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'chosen_chosen')))
        # 修改物品学名
        self.dr.find_element_by_xpath('//*[@id="chosen_chosen"]').click()
        self.dr.find_element_by_xpath('//*[@id="chosen_chosen"]/div/div/input').send_keys('车厘子')
        wpxmEle = self.dr.find_element_by_xpath('//*[@id="chosen_chosen"]/div/ul/li/em')
        self.assertEqual('车厘子', wpxmEle.text)
        wpxmEle.click()
        # 点击确定按钮
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]').click()
        # 验证编辑成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn('操作成功',
                      self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 系统设置-物品别名页面，删除物品别名
    def wpbm_delete(self,):
        # 按物品学名查询
        self.wpbm_search({'wpxm': '车厘子', 'bm': '', 'zt': '', 'sfczcywp': ''})
        # 点击删除按钮
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]/div/button[1]').click()
        # 点击确定按钮
        self.dr.find_element_by_xpath('/html/body/div[4]/div[3]/div/button[2]').click()
        # 验证删除成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn('删除成功',
                      self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 系统设置-物品别名页面，批量删除物品别名
    def wpbm_batchdelete(self):
        # 新增
        self.wpbm_add('樱桃A', '车厘子A', '操作成功')
        time.sleep(2)
        self.wpbm_add('樱桃B', '车厘子B', '操作成功')
        # 按学名查询
        self.wpbm_search({'wpxm': '樱桃', 'bm': '', 'zt': '', 'sfczcywp': ''})
        # 勾选物品
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[1]/input').click()
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[2]/td[1]/input').click()
        # 点击删除按钮
        self.dr.find_element_by_xpath('//*[@id="btnDelete"]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[3]/div/button[2]')))
        # 点击确定按钮
        self.dr.find_element_by_xpath('/html/body/div[4]/div[3]/div/button[2]').click()
        # 验证删除成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn('删除成功',
                      self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 系统设置-物品别名页面，合并物品别名
    def wpbm_merge(self):
        # 新增
        self.wpbm_add('圣女果A', '小番茄A', '操作成功')
        time.sleep(2)
        self.wpbm_add('圣女果B', '小番茄B', '操作成功')
        # 按学名查询
        self.wpbm_search({'wpxm': '圣女果', 'bm': '', 'zt': '', 'sfczcywp': ''})
        # 勾选物品
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[1]/input').click()
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[2]/td[1]/input').click()
        bm1 = self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text
        bm2 = self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[2]/td[3]').text
        bm_merge = bm1 + ',' + bm2
        # 点击合并按钮
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/button').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'chosen_chosen')))
        # 选择合并后的物品学名
        self.dr.find_element_by_xpath('//*[@id="chosen_chosen"]').click()
        self.dr.find_element_by_xpath('//*[@id="chosen_chosen"]/div/div/input').send_keys('圣女果B')
        # 验证搜索正确
        wpxmEle = self.dr.find_element_by_xpath('//*[@id="chosen_chosen"]/div/ul/li/em')
        self.assertEqual('圣女果B', wpxmEle.text)
        # 点击搜索结果
        wpxmEle.click()
        # 点击确定按钮
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]').click()
        self.dr.find_element_by_xpath('/html/body/div[5]/div[3]/div/button[2]').click()
        # 点击搜索按钮
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(0.5)
        # 验证合并成功
        self.assertEqual('圣女果B', self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[2]').text)
        self.assertEqual(bm_merge, self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[3]').text)

        # 删除合并后的别名
        self.wpbm_search({'wpxm': '圣女果B', 'bm': '', 'zt': '', 'sfczcywp': ''})
        # 点击删除按钮
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[4]/div/button[1]').click()
        # 点击确定按钮
        self.dr.find_element_by_xpath('/html/body/div[4]/div[3]/div/button[2]').click()
        # 验证删除成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn('删除成功',
                      self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    def dialog_select_treenode(self, idlist):
        self.dr.find_element_by_xpath('//*[@id="pname"]').click()
        for id in idlist:
            if id == idlist[-1]:
                self.dr.find_element_by_xpath('//*[@id="treeSelect_' + str(id) + '_a"]').click()
            else:
                self.dr.find_element_by_xpath('//*[@id="treeSelect_' + str(id) + '_switch"]').click()

    def list_select_treenode_single(self, idlist):
        for id in idlist:
            if id == idlist[-1]:
                self.dr.find_element_by_xpath('//*[@id="tr_' + str(id) + '"]/td[1]/input').click()
            else:
                self.dr.find_element_by_xpath('//*[@id="tr_' + str(id) + '"]/td[1]/span/a').click()

    def list_select_treenode_batch(self, ids):
        for idlist in ids:
            for id in idlist:
                if id == idlist[-1]:
                    self.dr.find_element_by_xpath('//*[@id="tr_' + str(id) + '"]/td[1]/input').click()
                else:
                    ele = self.dr.find_element_by_xpath('//*[@id="tr_' + str(id) + '"]')
                    is_collapsed = 'collapsed' in ele.get_attribute('class')
                    if is_collapsed:
                        self.dr.find_element_by_xpath('//*[@id="tr_' + str(id) + '"]/td[1]/span/a').click()

    # 系统设置-常用物品分类页面，添加分类
    def cywpfl_add(self, content, msg):
        # 点击添加按钮
        self.dr.find_element_by_xpath('//*[@id="add"]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'fldm')))
        # 填入内容
        self.dr.find_element_by_xpath('//*[@id="fldm"]').send_keys(content['fldm'])
        self.dr.find_element_by_xpath('//*[@id="flmc"]').send_keys(content['flmc'])
        self.dialog_select_treenode(content['sjflid'])
        time.sleep(0.2)
        # 点击确定按钮
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]').click()
        # 验证添加成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn(msg, self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 系统设置-常用物品分类页面，编辑分类
    def cywpfl_edit(self, content):
        # 勾选要编辑的分类
        self.list_select_treenode_single(content['flid'])
        # 点击编辑按钮
        self.dr.find_element_by_xpath('//*[@id="tr_' + str(content['flid'][-1]) + '"]/td[4]/div/button[2]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'flmc')))
        # 修改分类名称
        self.dr.find_element_by_xpath('//*[@id="flmc"]').clear()
        self.dr.find_element_by_xpath('//*[@id="flmc"]').send_keys(content['flmc'])
        # 点击确定按钮
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]').click()
        # 验证修改成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn('操作成功', self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 系统设置-常用物品分类页面，删除分类
    def cywpfl_delete(self, idlist):
        # 勾选要删除的分类
        self.list_select_treenode_single(idlist)
        # 点击删除按钮
        self.dr.find_element_by_xpath('//*[@id="tr_' + str(idlist[-1]) + '"]/td[4]/div/button[1]').click()
        # 点击确定按钮
        self.dr.find_element_by_xpath('/html/body/div[4]/div[3]/div/button[2]').click()
        # 验证删除成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn('删除成功',
                      self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 系统设置-常用物品分类页面，批量删除分类
    def cywpfl_batchdelete(self, ids):
        # 勾选分类
        self.list_select_treenode_batch(ids)
        # 点击删除按钮
        self.dr.find_element_by_xpath('//*[@id="delete"]').click()
        # 点击确定按钮
        self.dr.find_element_by_xpath('/html/body/div[4]/div[3]/div/button[2]').click()
        # 验证删除成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn('删除成功',
                      self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 系统设置-仓库设置页面，新增仓库
    def cksz_add(self, content, msg):
        # 点击添加按钮
        self.dr.find_element_by_xpath('//*[@id="add"]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="editForm"]/table/tbody/tr[1]/td/input')))
        # 填入内容
        self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[1]/td/input').send_keys(content['ckm'])
        Select(self.dr.find_element_by_xpath('//*[@id="sel_kadm"]')).select_by_visible_text(content['js'])
        Select(self.dr.find_element_by_xpath('//*[@id="sel_ksdm"]')).select_by_visible_text(content['ks'])
        time.sleep(0.5)
        # 点击确定按钮
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]').click()
        # 验证添加成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn(msg, self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 系统设置-仓库设置页面，查询仓库
    def cksz_search(self, search_value):
        # 填入查询条件
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/input').send_keys(search_value['ckm'])
        if search_value['js'] != '':
            Select(self.dr.find_element_by_xpath('//*[@id="kadm"]')).select_by_visible_text(search_value['js'])
        if search_value['ks'] != '':
            Select(self.dr.find_element_by_xpath('//*[@id="ksdm"]')).select_by_visible_text(search_value['ks'])
        # 点击搜索按钮
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(0.5)

    # 系统设置-仓库设置页面，编辑仓库
    def cksz_edit(self, content):
        # 点击编辑按钮
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[5]/div/button[2]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="editForm"]/table/tbody/tr[1]/td/input')))
        # 填入内容
        self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[1]/td/input').clear()
        self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[1]/td/input').send_keys(content['ckm'])
        if content['js'] != '':
            Select(self.dr.find_element_by_xpath('//*[@id="sel_kadm"]')).select_by_visible_text(content['js'])
        if content['ks'] != '':
            Select(self.dr.find_element_by_xpath('//*[@id="sel_ksdm"]')).select_by_visible_text(content['ks'])
        # 点击确定按钮
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]').click()
        # 验证编辑成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn('操作成功', self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 系统设置-仓库设置页面，删除仓库
    def cksz_delete(self, content):
        # 查询仓库设置
        self.cksz_search(content)
        # 点击删除按钮
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[5]/div/button[1]').click()
        # 点击确定按钮
        self.dr.find_element_by_xpath('/html/body/div[4]/div[3]/div/button[2]').click()
        # 验证删除成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn('删除成功',
                      self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 系统设置-仓库设置页面，批量删除仓库
    def cksz_batchdelete(self):
        # 勾选要删除的仓库设置
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        # 点击批量删除按钮
        self.dr.find_element_by_xpath('//*[@id="btn_delete"]').click()
        time.sleep(0.5)
        # 点击确定按钮
        self.dr.find_element_by_xpath('/html/body/div[4]/div[3]/div/button[2]').click()
        # 验证删除成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn('删除成功',
                      self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 系统设置-数据字典页面，新增字典类别
    def sjzd_category_add(self, content, msg):
        # 点击新增按钮
        self.dr.find_element_by_xpath('//*[@id="add"]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="editForm"]/table/tbody/tr[1]/td/input')))
        # 填入内容
        self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[1]/td/input').send_keys(content['lxdm'])
        self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[2]/td/input').send_keys(content['lxmc'])
        if content['bz'] != '':
            self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[3]/td/textarea').send_keys(content['bz'])
        # 点击确定按钮
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]').click()
        # 验证添加成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn(msg, self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 系统设置-数据字典页面，编辑字典类别
    def sjzd_category_edit(self, content):
        # 右键点击要编辑的字典类别
        ele = self.dr.find_element_by_xpath('//*[@title="' + content['lxmc_old'] + '"]')
        ActionChains(self.dr).context_click(ele).perform()
        # 点击编辑按钮
        self.dr.find_element_by_xpath('//*[@id="sjzdMn"]/li/a').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="editForm"]/table/tbody/tr[2]/td/input')))
        # 填入内容
        self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[2]/td/input').clear()
        self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[2]/td/input').send_keys(content['lxmc_new'])
        if content['bz'] != '':
            self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[3]/td/textarea').clear()
            self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[3]/td/textarea').send_keys(
                content['bz'])
        # 点击确定按钮
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]').click()
        # 验证编辑成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn('操作成功',
                      self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 系统设置-数据字典页面，删除字典类别
    def sjzd_category_delete(self, content):
        # 勾选要删除的字典类别
        self.dr.find_element_by_xpath('//*[@title="' + content['lxmc'] + '"]/../span[2]').click()
        # 点击删除按钮
        self.dr.find_element_by_xpath('//*[@id="delete"]').click()
        # 点击确定按钮
        self.dr.find_element_by_xpath('/html/body/div[4]/div[3]/div/button[2]').click()
        # 验证删除成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn('删除成功',
                      self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 进入数据字典类别页面
    def enter_category(self, category):
        ele = self.dr.find_element_by_xpath('//*[@title="' + category + '"]')
        ActionChains(self.dr).double_click(ele).perform()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'addChildren')))

    # 系统设置-数据字典页面，字典类别，添加子项
    def sjzd_add(self, content, msg):
        # 点击添加按钮
        self.dr.find_element_by_xpath('//*[@id="addChildren"]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'zddm')))
        # 填入内容
        self.dr.find_element_by_xpath('//*[@id="zddm"]').send_keys(content['zddm'])
        if content['zdmc'] != '':
            self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[2]/td/input').send_keys(content['zdmc'])
        if content['syzt'] != '':
            Select(self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[3]/td/select')).select_by_visible_text(content['syzt'])
        if content['sska'] != '':
            Select(self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[5]/td/select')).select_by_visible_text(content['sska'])
        if content['bz'] != '':
            self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[6]/td/textarea').send_keys(content['bz'])
        # 点击确定按钮
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]').click()
        # 验证添加成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn(msg, self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 系统设置-数据字典页面，字典类别，查询子项
    def sjzd_search(self, search_value):
        if search_value['zddm'] != '':
            self.dr.find_element_by_xpath('//*[@id="form"]/div/div[1]/input').send_keys(search_value['zddm'])
        if search_value['zdmc'] != '':
            self.dr.find_element_by_xpath('//*[@id="form"]/div/div[2]/input').send_keys(search_value['zdmc'])
        if search_value['bz'] != '':
            self.dr.find_element_by_xpath('//*[@id="form"]/div/div[3]/input').send_keys(search_value['bz'])
        # 点击搜索按钮
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(0.5)

    # 系统设置-数据字典页面，字典类别，编辑子项
    def sjzd_edit(self, content):
        # 点击编辑按钮
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[8]/div/button[2]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'zddm')))
        # 修改内容
        if content['zdmc'] != '':
            self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[2]/td/input').clear()
            self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[2]/td/input').send_keys(content['zdmc'])
        if content['syzt'] != '':
            Select(self.dr.find_element_by_xpath(
                '//*[@id="editForm"]/table/tbody/tr[3]/td/select')).select_by_visible_text(content['syzt'])
        if content['sska'] != '':
            Select(self.dr.find_element_by_xpath(
                '//*[@id="editForm"]/table/tbody/tr[5]/td/select')).select_by_visible_text(content['sska'])
        if content['bz'] != '':
            self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[6]/td/textarea').clear()
            self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[6]/td/textarea').send_keys(content['bz'])
        # 点击确定按钮
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]').click()
        # 验证添加成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn('操作成功', self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 系统设置-数据字典页面，字典类别，删除子项
    def sjzd_delete(self):
        # 点击删除按钮
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[8]/div/button[1]').click()
        # 点击确定按钮
        self.dr.find_element_by_xpath('/html/body/div[4]/div[3]/div/button[2]').click()
        # 验证删除成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn('删除成功',
                      self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 系统设置-数据字典页面，字典类别，批量删除子项
    def sjzd_batchdelete(self):
        # 点击全选按钮
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        # 点击删除按钮
        self.dr.find_element_by_xpath('//*[@id="deleteChildren"]') .click()
        time.sleep(0.5)
        # 点击确定按钮
        self.dr.find_element_by_xpath('/html/body/div[4]/div[3]/div/button[2]').click()
        # 验证删除成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn('删除成功',
                      self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 系统设置-场地监控页面，新增场地监控
    def cdjk_add(self, content, msg):
        # 点击添加按钮
        self.dr.find_element_by_xpath('//*[@id="btnadd"]').click()
        self.dr.switch_to.default_content()
        WebDriverWait(self.dr, 5, 0.2).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="editForm"]/table/tbody/tr[1]/td/input')))
        # 输入内容
        self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[1]/td/input').send_keys(content['cddm'])
        self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[2]/td/input').send_keys(content['cdmc'])
        for i in content['sbid']:
            self.dr.find_element_by_xpath('//*[@id="sbid_chosen"]/ul').click()
            self.dr.find_element_by_xpath('//*[@id="sbid_chosen"]/div/ul/li[' + str(i) + ']').click()
        # 点击确定按钮
        # self.dr.find_element_by_xpath('/html/body/div[9]/div[11]/div/button[1]').click()
        self.dr.find_element_by_xpath('/html/body/div[9]/div[3]/div/button[1]').click()
        iframe = self.dr.find_element_by_xpath('//*[@id="sub_c486d4d177dc4a02b6d997c5d9f4b20f"]/iframe')
        self.dr.switch_to.frame(iframe)
        # 验证添加成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn(msg, self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 系统设置-场地监控页面，查询场地监控
    def cdjk_search(self, search_value):
        # 输入查询条件
        self.dr.find_element_by_xpath('//*[@id="cddm"]').send_keys(search_value['cddm'])
        self.dr.find_element_by_xpath('//*[@id="cdmc"]').send_keys(search_value['cdmc'])
        # 点击搜索按钮
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(0.5)

    # 系统设置-场地监控页面，编辑场地监控
    def cdjk_edit(self, content):
        # 点击编辑按钮
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[5]/div/button[2]').click()
        self.dr.switch_to.default_content()
        WebDriverWait(self.dr, 5, 0.2).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="editForm"]/table/tbody/tr[1]/td/input')))
        # 修改内容
        self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[2]/td/input').clear()
        self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[2]/td/input').send_keys(content['cdmc'])
        eles = self.dr.find_elements_by_xpath('//*[@id="sbid_chosen"]/ul/li/a')
        for ele in eles:
            ele.click()
            time.sleep(5)
        if content['sbid'] != '':
            for i in content['sbid']:
                self.dr.find_element_by_xpath('//*[@id="sbid_chosen"]/ul').click()
                self.dr.find_element_by_xpath('//*[@id="sbid_chosen"]/div/ul/li[' + str(i) + ']').click()
        # 点击确定按钮
        self.dr.find_element_by_xpath('/html/body/div[9]/div[3]/div/button[1]').click()
        iframe = self.dr.find_element_by_xpath('//*[@id="sub_c486d4d177dc4a02b6d997c5d9f4b20f"]/iframe')
        self.dr.switch_to.frame(iframe)
        # 验证编辑成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn('保存成功',
                      self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 系统设置-场地监控页面，删除场地监控
    def cdjk_delete(self):
        # 点击删除按钮
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[5]/div/button[1]').click()
        # time.sleep(0.5)
        # 点击确定按钮
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]').click()
        # 验证删除成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn('删除成功',
                      self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 系统设置-场地监控页面，批量删除场地监控
    def cdjk_batchdelete(self):
        # 点击全选按钮
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        # 点击删除按钮
        self.dr.find_element_by_xpath('//*[@id="btnDel"]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[3]/div/button[2]')))
        # 点击确定按钮
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]').click()
        # 验证删除成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn('删除成功',
                      self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 系统设置-常见问题页面，新增常见问题
    def cjwt_add(self, content):
        # 点击添加按钮
        self.dr.find_element_by_xpath('//*[@id="add"]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="editForm"]/table/tbody/tr[1]/td/select')))
        # 填入内容
        # Select(self.dr.find_element_by_xpath('//*[@id="type"]')).select_by_visible_text(content['lx'])
        Select(self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[1]/td/select')).select_by_visible_text(content['lx'])
        # self.dr.find_element_by_xpath('').click()   # 发布日期
        self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[3]/td/input').send_keys(content['wt'])
        self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[4]/td/textarea').send_keys(content['jd'])
        # self.dr.find_element_by_xpath('').send_keys()   # 附件
        # 点击确定按钮
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]').click()
        # 验证添加成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn('操作成功', self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 系统设置-常见问题页面，查询常见问题
    def cjwt_search(self, search_value):
        # 输入查询条件
        if search_value['lx'] != '':
            Select(self.dr.find_element_by_xpath('//*[@id="type"]')).select_by_visible_text(search_value['lx'])
        if search_value['wt'] != '':
            self.dr.find_element_by_xpath('//*[@id="question"]').send_keys(search_value['wt'])
        if search_value['jd'] != '':
            self.dr.find_element_by_xpath('//*[@id="answer"]').send_keys(search_value['jd'])
        # 点击搜索按钮
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(0.5)

    # 系统设置-常见问题页面，查看常见问题详情
    def cjwt_detail(self, content):
        # 点击查看详情按钮
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody[1]/tr[1]/td[6]/div/button[1]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="law_detail"]/div[1]/div[2]/span')))
        # 验证详情正确
        wt = self.dr.find_element_by_xpath('//*[@id="law_detail"]/div[1]/div[2]/span').text
        lx = self.dr.find_element_by_xpath('//*[@id="law_detail"]/div[2]/div[2]/span').text
        jd = self.dr.find_element_by_xpath('//*[@id="law_detail"]/div[4]/div[2]/span').text
        self.assertEqual(wt, content['wt'])
        self.assertEqual(lx, content['lx'])
        self.assertEqual(jd, content['jd'])

    # 系统设置-常见问题页面，编辑常见问题
    def cjwt_edit(self, content):
        # 点击编辑按钮
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody[1]/tr[1]/td[6]/div/button[3]').click()
        WebDriverWait(self.dr, 5, 0.2).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="editForm"]/table/tbody/tr[1]/td/select')))
        # 修改内容
        # Select(self.dr.find_element_by_xpath('//*[@id="type"]')).select_by_visible_text(content['lx'])
        Select(self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[1]/td/select')).select_by_visible_text(content['lx'])
        self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[3]/td/input').clear()
        self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[3]/td/input').send_keys(content['wt'])
        self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[4]/td/textarea').clear()
        self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[4]/td/textarea').send_keys(content['jd'])
        # 点击确定按钮 /html/body/div[4]/div[3]/div/button[2]
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]').click()
        # 验证编辑成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn('操作成功',
                      self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 系统设置-常见问题页面，删除常见问题
    def cjwt_delete(self):
        # 点击删除按钮
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody[1]/tr[1]/td[6]/div/button[2]').click()
        time.sleep(0.5)
        # 点击确定按钮 /html/body/div[9]/div[3]/div/button[2]
        self.dr.find_element_by_xpath('/html/body/div[4]/div[3]/div/button[2]').click()
        # 验证删除成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn('删除成功',
                      self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)

    # 系统设置-常见问题页面，批量删除常见问题
    def cjwt_batchdelete(self):
        # 勾选全选
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/label/input').click()
        # 点击删除按钮
        self.dr.find_element_by_xpath('//*[@id="delete"]').click()
        time.sleep(0.5)
        # 点击确定按钮 /html/body/div[9]/div[3]/div/button[2]
        self.dr.find_element_by_xpath('/html/body/div[6]/div[3]/div/button[2]').click()
        # 验证删除成功
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        self.assertIn('删除成功',
                      self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p').text)


if __name__ == '__main__':
    unittest.main()