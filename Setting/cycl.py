import unittest
import re
import time
import xlrd
import os
# from Setting.setting_file import url,login_name_user1,login_name_password1
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from Setting.setting_file import setting_xls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from Setting.menu import data

from selenium.webdriver.chrome.options import Options

Testdata = xlrd.open_workbook(setting_xls)
sheet_passenger=Testdata.sheet_by_name('旅客信息')
sheet_goods=Testdata.sheet_by_name('物品信息')

class cycl_TestCase(unittest.TestCase):

    def setUp(self):
        #打开Chrome浏览器
        self.dr=webdriver.Chrome()
        #最大化google浏览器窗口
        self.dr.maximize_window()

    def tearDown(self):
        #关闭浏览器
        self.dr.quit()

    # 出入境携带物查验-录单
    def xdw_Inspection_addition(self,test_num,cllx,clffmx):
        iframe = self.dr.find_element_by_tag_name("iframe")
        self.dr.switch_to.frame(iframe)
        # 姓名
        self.dr.find_element_by_xpath('//*[@id="lkxm"]').send_keys(sheet_passenger.col_values(test_num, 1, 2)[0])
        # 性别
        Select(self.dr.find_element_by_xpath('//*[@id="xb"]')).select_by_value(
            sheet_passenger.col_values(test_num, 2, 3)[0])
        # 备注信息
        self.dr.find_element_by_xpath('//*[@id="lkbz"]').send_keys(sheet_passenger.col_values(test_num, 11, 12)[0])
        # 点击国籍输入框
        self.dr.find_element_by_xpath('//*[@id="gj"]').click()
        # 国籍
        self.dr.find_element_by_xpath(
            '//*[@id="comefromContainer"]/ul/li[' + str(sheet_passenger.col_values(test_num, 3, 4)[0]) + ']').click()
        # 出生日期
        self.dr.find_element_by_xpath('//*[@id="csrq"]').send_keys(int(sheet_passenger.col_values(test_num, 4, 5)[0]))
        # 证件类别
        self.dr.find_element_by_xpath('//*[@id="btnZjlx"]').click()
        all = self.dr.window_handles
        self.dr.switch_to.window(all[-1])
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="certSelect"]/li[1]').click()
        self.dr.switch_to.window(all[0])
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame(iframe)
        # 航班号
        self.dr.find_element_by_xpath('//*[@id="lkForm"]/div[1]/div[1]/div[2]/div[3]/div[2]/div/input').clear()
        self.dr.find_element_by_xpath('//*[@id="lkForm"]/div[1]/div[1]/div[2]/div[3]/div[2]/div/input').send_keys(
            sheet_passenger.col_values(test_num, 6, 7)[0])
        # 证件号码
        self.dr.find_element_by_xpath('//*[@id="zjh"]').send_keys(int(sheet_passenger.col_values(test_num, 7, 8)[0]))
        # 联系地址
        self.dr.find_element_by_xpath('//*[@id="lxdz"]').clear()
        self.dr.find_element_by_xpath('//*[@id="lxdz"]').send_keys('湖北省武汉市洪山区')
        # 来源国
        self.dr.find_element_by_xpath('//*[@id="lz"]').click()
        self.dr.find_element_by_xpath(
            '//*[@id="countryContainer"]/ul/li[' + str(sheet_passenger.col_values(test_num, 9, 10)[0]) + ']').click()
        # 联系方式
        self.dr.find_element_by_xpath('//*[@id="lkForm"]/div[1]/div[1]/div[2]/div[5]/div[2]/input').clear()
        self.dr.find_element_by_xpath('//*[@id="lkForm"]/div[1]/div[1]/div[2]/div[5]/div[2]/input').send_keys(
            int(sheet_passenger.col_values(test_num, 10, 11)[0]))
        # 物品名称
        self.dr.find_element_by_xpath('//*[@id="btnWpcd"]').click()
        all = self.dr.window_handles
        self.dr.switch_to.window(all[-1])
        self.dr.find_element_by_xpath(
            '//*[@id="wpcdSelect"]/li[' + str(sheet_goods.col_values(test_num, 2, 3)[0]) + ']').click()
        time.sleep(2)
        all = self.dr.window_handles
        self.dr.switch_to.window(all[0])
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame(iframe)
        # 数量
        self.dr.find_element_by_xpath('//*[@id="sl"]').clear()
        self.dr.find_element_by_xpath('//*[@id="sl"]').send_keys(int(sheet_goods.col_values(test_num, 3, 4)[0]))
        # 重量
        self.dr.find_element_by_xpath('//*[@id="zl"]').send_keys(int(sheet_goods.col_values(test_num, 4, 5)[0]))
        Select(self.dr.find_element_by_xpath('//*[@id="cllx"]')).select_by_visible_text(cllx)
        if cllx=='退回':
            Select(self.dr.find_element_by_xpath('//*[@id="clffmx_1"]')).select_by_value(clffmx)
        elif cllx=='截留':
            Select(self.dr.find_element_by_xpath('//*[@id="clffmx_2"]')).select_by_value(clffmx)
        else:
            pass
        self.dr.find_element_by_xpath('//*[@id="bz"]').send_keys(sheet_goods.col_values(test_num, 12, 13)[0])
        time.sleep(2)
        files = r'E:\胡亮\项目工作安排\测试文件svn\web自动化\携带物2.0\images\\' + sheet_goods.col_values(test_num, 14, 15)[0]
        self.dr.find_element_by_xpath('//*[@id="wptp"]').send_keys(files)
        time.sleep(5)
        self.dr.find_element_by_xpath('//*[@id="btnGtj"]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="btnSave"]/span').click()
        # 确认操作提示框
        self.dr.find_element_by_xpath('/html/body/div[9]/div[3]/div/button[2]').click()
        WebDriverWait(self.dr,5,0.2).until(expected_conditions.visibility_of_element_located((By.ID,'gritter-notice-wrapper')))
        self.dr.switch_to.default_content()
        time.sleep(3)
        self.dr.switch_to.frame(iframe)
        self.assertEqual('截留物单据打印', self.dr.find_element_by_xpath('/html/body/div/div/h3/span').text)
        global id, jld_id
        id = self.dr.find_element_by_xpath('//*[@id="list"]/tbody[1]/tr/td[3]').text
        jld_id = self.dr.find_element_by_xpath('//*[@id="jldbh"]').get_attribute('value')
        return id,jld_id


    #携带物打印-查询功能--huliang-20190719
    def xdw_Print_search(self,search_value={'jldbh':'','wpmc':'','startTime':'','endTime':'','dyzt':'','ysbh':''}):
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/input').clear()
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/input').send_keys(search_value['jldbh'])
        self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/input').clear()
        self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/input').send_keys(search_value['wpmc'])
        self.dr.find_element_by_xpath('//*[@id="startTime"]').clear()
        self.dr.find_element_by_xpath('//*[@id="startTime"]').send_keys(search_value['startTime'])
        self.dr.find_element_by_xpath('//*[@id="endTime"]').clear()
        self.dr.find_element_by_xpath('//*[@id="endTime"]').send_keys(search_value['endTime'])
        Select(self.dr.find_element_by_xpath('//*[@id="form"]/div[4]/select')).select_by_visible_text(search_value['dyzt'])
        self.dr.find_element_by_xpath('//*[@id="form"]/div[5]/input').send_keys(search_value['ysbh'])
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(2)

    #现场转库或入库查询功能
    def xdw_Onsite_transfer_or_storage_search(self,search_value={'startTime':'','endTime':'','wpbh':'','wpmc':'','wplb':'','clff':''}):
        #下滑滚动条到
        # js = "window.scrollTo(0, document.body.scrollHeight)"
        # js = "window.scrollTo(0, 500)"
        # self.dr.execute_script(js)
        # target = self.dr.find_element_by_xpath('//*[@id="3lists"]/div[2]/div[1]/div/div[4]/div[1]/span[2]/span/button')
        # self.dr.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去
        # time.sleep(3)
        # 切换每页显示记录数，方便后续校验
        # self.dr.find_element_by_xpath('//*[@id="3lists"]/div[2]/div[1]/div/div[4]/div[1]/span[2]/span/button').click()
        # self.dr.find_element_by_xpath('//*[@id="3lists"]/div[2]/div[1]/div/div[4]/div[1]/span[2]/span/ul/li[1]/a').click()
        # self.dr.implicitly_wait(3)
        #输入查询条件
        self.dr.find_element_by_xpath('//*[@id="startTime"]').send_keys(search_value['startTime'])
        self.dr.find_element_by_xpath('//*[@id="endTime"]').send_keys(search_value['endTime'])
        self.dr.find_element_by_xpath('//*[@id="wpbh"]').send_keys(search_value['wpbh'])
        self.dr.find_element_by_xpath('//*[@id="wpmc"]').send_keys(search_value['wpmc'])
        # self.dr.find_element_by_xpath('//*[@id="wplb"]').click()
        Select(self.dr.find_element_by_xpath('//*[@id="wplb"]')).select_by_visible_text(search_value['wplb'])
        Select(self.dr.find_element_by_xpath('//*[@id="clff"]')).select_by_visible_text(search_value['clff'])
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(3)

    #现场转库或入库导出功能，目前没有找到验证exexl数据正确性方法，暂时没有使用--hl
    def xdw_Onsite_transfer_or_storage_export(self):
        self.dr.find_element_by_xpath('//*[@id="export2"]').click()
        time.sleep(3)

    # 现场转库或入库-打印
    def xdw_Onsite_transfer_or_storage_print(self):
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[10]/div/button').click()

    # 现场转库或入库-转库操作
    def xdw_Onsite_transfer_or_storage_transfer(self):
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="transferBtn"]').click()
        time.sleep(2)
        Select(self.dr.find_element_by_xpath('//*[@id="selCkid"]')).select_by_visible_text('仓库2')
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[5]/div[3]/div/button[2]').click()

    ##现场转库或入库-入库操作
    def xdw_Onsite_transfer_or_storage_storage(self):
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="inStorageBtn"]').click()
        self.dr.find_element_by_xpath('/html/body/div[6]/div[3]/div/button[2]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        tipEle = self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p')
        self.assertIn('操作成功', tipEle.text)

    #异常单据处理-查询操作
    def xdw_Abnormal_Document_Processing_search(self,search_value={'Jldbh':'','Wpmc':'','startTime':'','endTime':'','shzt':''}):
        self.dr.find_element_by_xpath('//*[@id="condJldbh"]').clear()
        self.dr.find_element_by_xpath('//*[@id="condJldbh"]').send_keys(search_value['Jldbh'])
        self.dr.find_element_by_xpath('//*[@id="condWpmc"]').clear()
        self.dr.find_element_by_xpath('//*[@id="condWpmc"]').send_keys(search_value['Wpmc'])
        self.dr.find_element_by_xpath('//*[@id="startTime"]').clear()
        self.dr.find_element_by_xpath('//*[@id="startTime"]').send_keys(search_value['startTime'])
        self.dr.find_element_by_xpath('//*[@id="endTime"]').clear()
        self.dr.find_element_by_xpath('//*[@id="endTime"]').send_keys(search_value['endTime'])
        Select(self.dr.find_element_by_xpath('//*[@id="form"]/div[4]/select')).select_by_visible_text(search_value['shzt'])
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(2)

    #移交法制部门截留物处理-查询
    def xdw_yjfzbm_jlwcl_search(self,search_value):
        # self.dr.find_element_by_xpath('//*[@id="ksmc"]').clear()
        # self.dr.find_element_by_xpath('//*[@id="ksmc"]').send_keys(search_value['ks'])
        self.dr.find_element_by_xpath('//*[@id="form"]/div/div[2]/input').clear()
        self.dr.find_element_by_xpath('//*[@id="form"]/div/div[2]/input').send_keys(search_value['jldbh'])
        self.dr.find_element_by_xpath('//*[@id="form"]/div/div[3]/input').clear()
        self.dr.find_element_by_xpath('//*[@id="form"]/div/div[3]/input').send_keys(search_value['wpmc'])
        Select(self.dr.find_element_by_xpath('//*[@id="form"]/div/div[4]/select')).select_by_visible_text(search_value['state'])
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(2)

    # 移交法制部门截留物处理-案件结果录入
    def xdw_yjfzbm_jlwcl_Handle(self,search_value={'jlwpjglx':'','ajjg':'','jasj':''}):
        self.assertIsNotNone(self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[13]/div/button'))
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[13]/div').click()
        time.sleep(1)
        WebDriverWait(self.dr,5,0.2).until(expected_conditions.visibility_of_element_located((By.ID,'dialog-edit')))
        Select(self.dr.find_element_by_xpath('//*[@id="jlwpjglx"]')).select_by_visible_text(search_value['jlwpjglx'])
        self.dr.find_element_by_xpath('//*[@id="ajjg"]').send_keys(search_value['ajjg'])
        self.dr.find_element_by_xpath('//*[@id="jasj"]').send_keys(search_value['jasj'])
        self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[1]/td[1]').click()
        self.dr.find_element_by_xpath('/html/body/div[4]/div[3]/div/button[2]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        tipEle = self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p')
        self.assertIn('操作成功', tipEle.text)


    #其他携带物处理-查询
    def xdw_Other_Interception_Processing_search(self,search_value={'ks':'','wpbh':'','wpmc':'','clffmx':'','clzt':''}):
        # self.dr.find_element_by_xpath('//*[@id="ksmc"]').click()
        self.dr.find_element_by_xpath('//*[@id="form"]/div/div[2]/input').clear()
        self.dr.find_element_by_xpath('//*[@id="form"]/div/div[2]/input').send_keys(search_value['wpbh'])
        self.dr.find_element_by_xpath('//*[@id="form"]/div/div[3]/input').clear()
        self.dr.find_element_by_xpath('//*[@id="form"]/div/div[3]/input').send_keys(search_value['wpmc'])
        Select(self.dr.find_element_by_xpath('//*[@id="form"]/div/div[4]/select')).select_by_visible_text(search_value['clffmx'])
        Select(self.dr.find_element_by_xpath('//*[@id="form"]/div/div[5]/select')).select_by_visible_text(search_value['clzt'])
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(1)

    #其他携带物处理-截留物处理
    def xdw_Other_Interception_Processing_Handle(self,Handle={'jlcljg':'','jlwpjg':''}):
        self.assertIsNotNone(self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[9]/div/button'))
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[9]/div/button').click()
        time.sleep(2)
        Select(self.dr.find_element_by_xpath('//*[@id="jlcljg"]')).select_by_visible_text(Handle['jlcljg'])
        Select(self.dr.find_element_by_xpath('//*[@id="jlwpjg"]')).select_by_visible_text(Handle['jlwpjg'])
        time.sleep(1)
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        tipEle = self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p')
        self.assertIn('操作成功', tipEle.text)

    #送样结果录入-查询
    def xdw_Sampling_result_input_search(self,search_value={'wpbh':'','mc':'','start':'','end':'','zt':''}):
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/input').clear()
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/input').send_keys(search_value['wpbh'])
        self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/input').clear()
        self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/input').send_keys(search_value['mc'])
        self.dr.find_element_by_xpath('//*[@id="start"]').clear()
        self.dr.find_element_by_xpath('//*[@id="start"]').send_keys(search_value['start'])
        self.dr.find_element_by_xpath('//*[@id="end"]').clear()
        self.dr.find_element_by_xpath('//*[@id="end"]').send_keys(search_value['end'])
        Select(self.dr.find_element_by_xpath('//*[@id="form"]/div[5]/select')).select_by_visible_text(search_value['zt'])
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(1)

    # 送样结果录入-送样结果录入
    def xdw_Sampling_result_input_input(self,sjid):
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[11]/div/div[1]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="jgForm"]/div/div/div/div[1]/div[2]/input').send_keys(sjid)
        self.dr.find_element_by_xpath('//*[@id="bh_chosen"]/ul').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="bh_chosen"]/div/ul/li[1]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//*[@id="btnSave"]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        tipEle = self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p')
        self.assertIn('保存成功', tipEle.text)

    #隔离检疫-查询操作
    def xdw_Isolation_and_Quarantine_search(self,search_value={'status':''}):
        Select(self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/select')).select_by_visible_text(search_value['status'])
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(2)

    #隔离检疫-合格-通行
    def xdw_Isolation_and_Quarantine_Handle_qualified(self):
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[14]/div/button[2]').click()
        time.sleep(2)
        self.assertEqual('确定合格吗？', self.dr.find_element_by_xpath('//*[@id="dialog-tips"]/div').text)
        self.dr.find_element_by_xpath('/html/body/div[4]/div[3]/div/button[2]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        tipEle = self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p')
        self.assertIn('操作成功', tipEle.text)

    # 隔离检疫-不合格
    def xdw_Isolation_and_Quarantine_Handle_Unqualified(self,search_value={'clfs':''}):
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[14]/div/button[3]').click()
        WebDriverWait(self.dr,5,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'editForm')))
        Select(self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[1]/td[2]/select')).select_by_visible_text(search_value['clfs'])
        self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[2]/td[2]/textarea').send_keys('不合格')
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        tipEle = self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p')
        self.assertIn('操作成功', tipEle.text)

    # 隔离检疫-审核
    def xdw_Isolation_and_Quarantine_Handle_examine(self):
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[14]/div/button[2]').click()
        time.sleep(2)
        WebDriverWait(self.dr,5,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'dialog-edit')))
        self.dr.find_element_by_xpath('//*[@id="editForm"]/table/tbody/tr[7]/td/textarea').send_keys('隔离检疫')
        self.dr.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        tipEle = self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p')
        self.assertIn('操作成功', tipEle.text)

    # 转库接收确认-查询
    def xdw_Transfer_confirmation_receipt_search(self,
                                                 search_value={'wpbh': '', 'wpmc': '', 'start': '', 'end': ''}):
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/input').clear()
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/input').send_keys(search_value['wpbh'])
        self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/input').clear()
        self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/input').send_keys(search_value['wpmc'])
        self.dr.find_element_by_xpath('//*[@id="start"]').clear()
        self.dr.find_element_by_xpath('//*[@id="start"]').send_keys(search_value['start'])
        self.dr.find_element_by_xpath('//*[@id="end"]').clear()
        self.dr.find_element_by_xpath('//*[@id="end"]').send_keys(search_value['end'])
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(2)

    # 转库接收确认-接收确认
    def xdw_Transfer_confirmation_receipt(self):
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('//*[@id="btnJs"]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        tipEle = self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p')
        self.assertIn('操作成功', tipEle.text)

    # 转库-查询
    def xdw_Transfer_search(self,search_value={'wpbh':'','wpmc':'','rkr':'','start':'','end':''}):
        self.dr.find_element_by_xpath('//*[@id="ckid"]').clear()
        self.dr.find_element_by_xpath('//*[@id="ckid"]').send_keys(search_value['wpbh'])
        self.dr.find_element_by_xpath('//*[@id="wpmc"]').clear()
        self.dr.find_element_by_xpath('//*[@id="wpmc"]').send_keys(search_value['wpmc'])
        self.dr.find_element_by_xpath('//*[@id="rkr"]').clear()
        self.dr.find_element_by_xpath('//*[@id="rkr"]').send_keys(search_value['rkr'])
        self.dr.find_element_by_xpath('//*[@id="start"]').clear()
        self.dr.find_element_by_xpath('//*[@id="start"]').send_keys(search_value['start'])
        self.dr.find_element_by_xpath('//*[@id="end"]').clear()
        self.dr.find_element_by_xpath('//*[@id="end"]').send_keys(search_value['end'])
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(2)

    #转库_确认转库
    def xdw_Transfer_Transfer(self):
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('//*[@id="btnZk"]').click()
        time.sleep(2)
        WebDriverWait(self.dr,5,0.2).until(expected_conditions.visibility_of_element_located((By.ID,'dialog-edit')))
        Select(self.dr.find_element_by_xpath('//*[@id="selck"]')).select_by_visible_text('仓库1')
        time.sleep(1)
        self.dr.find_element_by_xpath('/html/body/div[5]/div[3]/div/button[2]').click()

    #出库_正常出库_查询
    def xdw_ck_normal_search(self,search_value={'wpbh':'','wpmc':'','startTime':'','endTime':'','clff':'','ckjglx':''}):
        self.dr.find_element_by_xpath('//*[@id="wpbh"]').clear()
        self.dr.find_element_by_xpath('//*[@id="wpbh"]').send_keys(search_value['wpbh'])
        self.dr.find_element_by_xpath('//*[@id="wpmc"]').clear()
        self.dr.find_element_by_xpath('//*[@id="wpmc"]').send_keys(search_value['wpmc'])
        self.dr.find_element_by_xpath('//*[@id="startTime"]').clear()
        self.dr.find_element_by_xpath('//*[@id="startTime"]').send_keys(search_value['startTime'])
        self.dr.find_element_by_xpath('//*[@id="endTime"]').clear()
        self.dr.find_element_by_xpath('//*[@id="endTime"]').send_keys(search_value['endTime'])
        Select(self.dr.find_element_by_xpath('//*[@id="clff"]')).select_by_visible_text(search_value['clff'])
        Select(self.dr.find_element_by_xpath('//*[@id="ckjglx"]')).select_by_visible_text(search_value['ckjglx'])
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(2)

    #出库_送检出库_查询
    def xdw_ck_Inspection_search(self):
        self.dr.find_element_by_xpath('//*[@id="sj"]/span').click()
        time.sleep(1)

    #出库_特殊出库_查询
    def xdw_ck_special_search(self):
        self.dr.find_element_by_xpath('//*[@id="ts"]/span').click()
        time.sleep(1)

    #出库_正常出库_销毁出库
    def xdw_ck_normal_xhck(self):
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('//*[@id="ckBtn"]').click()
        WebDriverWait(self.dr,5,0.2).until(expected_conditions.visibility_of_element_located((By.ID,'dialog-tips')))
        time.sleep(2)
        self.dr.find_element_by_xpath('/html/body/div[6]/div[3]/div/button[2]').click()
        time.sleep(3)
        self.dr.find_element_by_xpath('//*[@id="xhdd"]').click()
        self.dr.find_element_by_xpath('//*[@id="comefromContainer"]/ul/li').click()
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody[1]/tr[2]/td[2]/input').send_keys('销毁出库')
        self.dr.find_element_by_xpath('//*[@id="xhfs"]').click()
        self.dr.find_element_by_xpath('//*[@id="comefromContainer1"]/ul/li[1]').click()
        self.dr.find_element_by_xpath('/html/body/div[6]/div[3]/div/button[2]').click()
        time.sleep(2)
        handles = self.dr.window_handles
        self.assertEqual(3, len(handles))

    # 出库_正常出库_放行出库
    def xdw_ck_normal_fxck(self):
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('//*[@id="ckBtn"]').click()
        time.sleep(2)
        self.assertEqual('选中的物品只有【放行方式】，确定后直接出库！', self.dr.find_element_by_xpath('//*[@id="dialog-tips"]/div').text)
        self.dr.find_element_by_xpath('/html/body/div[6]/div[3]/div/button[2]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        tipEle = self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p')
        self.assertIn('操作成功', tipEle.text)

    # 出库_送检出库_送检出库
    def xdw_ck_normal_sjck(self,search_value={'telphone':'','ypmc':''}):
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('//*[@id="ckBtn"]').click()
        time.sleep(2)
        WebDriverWait(self.dr,5,0.2).until(expected_conditions.visibility_of_element_located((By.ID,'dialog-edit')))
        self.assertEqual('检验工作联系单', self.dr.find_element_by_xpath('//*[@id="sjdForm"]/div[1]').text)
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody[1]/tr[2]/td[2]/input').send_keys(search_value['telphone'])
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody[1]/tr[5]/td[1]/input').send_keys(search_value['ypmc'])
        self.dr.find_element_by_xpath('//*[@id="jyxm_chosen"]/ul').click()
        self.dr.find_element_by_xpath('//*[@id="jyxm_chosen"]/div/ul/li').click()
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody[1]/tr[9]/td/div[1]/label/input').click()
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody[1]/tr[11]/td/div/label[4]/input').click()
        self.dr.find_element_by_xpath('/html/body/div[5]/div[3]/div/button[2]').click()
        time.sleep(3)
        handles = self.dr.window_handles
        self.assertEqual(3, len(handles))

    # 出库_特殊出库_特殊出库
    def xdw_ck_tsck(self, search_value={'cklx2': '',}):
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('//*[@id="ckBtn"]').click()
        time.sleep(2)
        WebDriverWait(self.dr,5,0.2).until(expected_conditions.visibility_of_element_located((By.ID,'dialog-edit')))
        Select(self.dr.find_element_by_xpath('//*[@id="cklx2"]')).select_by_visible_text(search_value['cklx2'])
        self.dr.find_element_by_xpath('/html/body/div[5]/div[3]/div/button[2]').click()
        time.sleep(3)
        handles = self.dr.window_handles
        self.assertEqual(2, len(handles))
        self.assertEqual('没有找到匹配的记录',self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td').text)

    #退回_查询操作
    def xdw_return_search(self,search_value={'wpbh':'','wpmc':'','startTime':'','endTime':''}):
        self.dr.find_element_by_xpath('//*[@id="wpbh"]').clear()
        self.dr.find_element_by_xpath('//*[@id="wpbh"]').send_keys(search_value['wpbh'])
        self.dr.find_element_by_xpath('//*[@id="wpmc"]').clear()
        self.dr.find_element_by_xpath('//*[@id="wpmc"]').send_keys(search_value['wpmc'])
        self.dr.find_element_by_xpath('//*[@id="startTime"]').clear()
        self.dr.find_element_by_xpath('//*[@id="startTime"]').send_keys(search_value['startTime'])
        self.dr.find_element_by_xpath('//*[@id="endTime"]').clear()
        self.dr.find_element_by_xpath('//*[@id="endTime"]').send_keys(search_value['endTime'])
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(2)

    # 退回_延期
    def xdw_return_yq(self,time):
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[6]/div/div[1]').click()
        time.sleep(1)
        WebDriverWait(self.dr,5,0.2).until(expected_conditions.visibility_of_element_located((By.ID,'delayForm')))
        self.dr.find_element_by_xpath('//*[@id="date"]').clear()
        self.dr.find_element_by_xpath('//*[@id="date"]').send_keys(time)
        self.dr.find_element_by_xpath('/html/body/div[6]/div[3]/div/button[2]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        tipEle = self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p')
        self.assertIn('操作成功', tipEle.text)

    # 退回_预期转销毁
    def xdw_return_yqzxh(self):
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[6]/div/div[2]').click()
        time.sleep(2)
        WebDriverWait(self.dr,5,0.2).until(expected_conditions.visibility_of_element_located((By.ID,'dialog-tips')))
        self.assertEqual('是否将该条物品信息转为销毁？',self.dr.find_element_by_xpath('//*[@id="dialog-tips"]/div').text)
        self.dr.find_element_by_xpath('/html/body/div[7]/div[3]/div/button[2]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        tipEle = self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p')
        self.assertIn('预期转销毁成功', tipEle.text)

    # 退回_退回出库
    def xdw_return_th(self):
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[6]/div/div[2]').click()
        WebDriverWait(self.dr,5,0.2).until(expected_conditions.visibility_of_element_located((By.ID,'dialog-edit')))
        time.sleep(3)
        self.dr.find_element_by_xpath('/html/body/div[5]/div[3]/div/button[2]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        tipEle = self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p')
        self.assertIn('退回成功', tipEle.text)

    #销毁出库单据-查询操作
    def xdw_xhckdj_search(self,search_value={'xhdh':'','wpbh':'','start':'','end':'','ckr':''}):
        self.dr.find_element_by_xpath('//*[@id="form"]/div/div/div[1]/input').clear()
        self.dr.find_element_by_xpath('//*[@id="form"]/div/div/div[1]/input').send_keys(search_value['xhdh'])
        self.dr.find_element_by_xpath('//*[@id="form"]/div/div/div[2]/input').clear()
        self.dr.find_element_by_xpath('//*[@id="form"]/div/div/div[2]/input').send_keys(search_value['wpbh'])
        self.dr.find_element_by_xpath('//*[@id="start"]').clear()
        self.dr.find_element_by_xpath('//*[@id="start"]').send_keys(search_value['start'])
        self.dr.find_element_by_xpath('//*[@id="end"]').clear()
        self.dr.find_element_by_xpath('//*[@id="end"]').send_keys(search_value['end'])
        # Select(self.dr.find_element_by_xpath('//*[@id="cjrlb"]')).select_by_visible_text(search_value['ckr'])
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(2)

    # 送检出库单据-查询操作
    def xdw_sjckdj_search(self,search_value={'sjdh':'','wpbh':'','start':'','end':'','ckr':''}):
        self.dr.find_element_by_xpath('//*[@id="djbh"]').clear()
        self.dr.find_element_by_xpath('//*[@id="djbh"]').send_keys(search_value['sjdh'])
        self.dr.find_element_by_xpath('//*[@id="wpbh"]').clear()
        self.dr.find_element_by_xpath('//*[@id="wpbh"]').send_keys(search_value['wpbh'])
        self.dr.find_element_by_xpath('//*[@id="start"]').clear()
        self.dr.find_element_by_xpath('//*[@id="start"]').send_keys(search_value['start'])
        self.dr.find_element_by_xpath('//*[@id="end"]').clear()
        self.dr.find_element_by_xpath('//*[@id="end"]').send_keys(search_value['end'])
        # Select(self.dr.find_element_by_xpath('//*[@id="cjrlb"]')).select_by_visible_text(search_value['ckr'])
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(2)

    #移交保护部门出库单据-查询操作
    def xdw_yjbhbm_search(self,search_value={'yjdh':'','wpbh':'','start':'','end':'','ckr':''}):
        self.dr.find_element_by_xpath('//*[@id="djbh"]').clear()
        self.dr.find_element_by_xpath('//*[@id="djbh"]').send_keys(search_value['yjdh'])
        self.dr.find_element_by_xpath('//*[@id="wpbh"]').clear()
        self.dr.find_element_by_xpath('//*[@id="wpbh"]').send_keys(search_value['wpbh'])
        self.dr.find_element_by_xpath('//*[@id="start"]').clear()
        self.dr.find_element_by_xpath('//*[@id="start"]').send_keys(search_value['start'])
        self.dr.find_element_by_xpath('//*[@id="end"]').clear()
        self.dr.find_element_by_xpath('//*[@id="end"]').send_keys(search_value['end'])
        # Select(self.dr.find_element_by_xpath('//*[@id="cjrlb"]')).select_by_visible_text(search_value['ckr'])
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(2)

    # 转库单据-查询操作
    def xdw_zkdj_search(self,search_value={'zkdj':'','wpbh':'','wpmc':'','start':'','end':'','czr':'','zklx':''}):
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/div[1]/input').clear()
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/div[1]/input').send_keys(search_value['zkdj'])
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/div[2]/input').clear()
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/div[2]/input').send_keys(search_value['wpbh'])
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/div[3]/input').clear()
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/div[3]/input').send_keys(search_value['wpmc'])
        self.dr.find_element_by_xpath('//*[@id="start"]').clear()
        self.dr.find_element_by_xpath('//*[@id="start"]').send_keys(search_value['start'])
        self.dr.find_element_by_xpath('//*[@id="end"]').clear()
        self.dr.find_element_by_xpath('//*[@id="end"]').send_keys(search_value['end'])
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/div[5]/input').clear()
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/div/div[5]/input').send_keys(search_value['czr'])
        Select(self.dr.find_element_by_xpath('//*[@id="zklx"]')).select_by_visible_text(search_value['zklx'])
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(2)

    #转库单据-打印页面
    def xdw_zkdj_print(self,search_value):
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]/div/div').click()
        handles = self.dr.window_handles
        self.dr.switch_to.window(handles[-1])
        time.sleep(2)
        # print(self.dr.title)
        self.assertEqual('出库截留物清单',self.dr.title)
        self.assertEqual('转库截留物清单',self.dr.find_element_by_xpath('/html/body/div/div[3]/div/table/thead/tr[1]/th/span').text)
        self.assertEqual(search_value['zkdj'],
                         self.dr.find_element_by_xpath('/html/body/div/div[3]/div/table/tbody/tr/td[2]').text)
        self.assertEqual(search_value['wpbh'],
                         self.dr.find_element_by_xpath('/html/body/div/div[3]/div/table/tbody/tr/td[3]').text)
        self.assertEqual(search_value['wpmc'],
                         self.dr.find_element_by_xpath('/html/body/div/div[3]/div/table/tbody/tr/td[4]').text)
        self.assertEqual(search_value['wpmc'],
                         self.dr.find_element_by_xpath('/html/body/div/div[3]/div/table/tbody/tr/td[4]').text)
        self.assertIn(search_value['start'],
                         self.dr.find_element_by_xpath('/html/body/div/div[3]/div/table/tbody/tr/td[8]').text)
        self.assertEqual(search_value['czr'],
                         self.dr.find_element_by_xpath('/html/body/div/div[3]/div/table/tbody/tr/td[9]').text)
        self.assertIn(search_value['zklx'],
                         self.dr.find_element_by_xpath('/html/body/div/div[3]/div/table/tbody/tr/td[10]').text)

    #入库记录-查询
    def xdw_rkjl_search(self,search_value):
        self.dr.find_element_by_xpath('//*[@id="bh"]').clear()
        self.dr.find_element_by_xpath('//*[@id="bh"]').send_keys(search_value['wpbh'])
        self.dr.find_element_by_xpath('//*[@id="mc"]').clear()
        self.dr.find_element_by_xpath('//*[@id="mc"]').send_keys(search_value['wpmc'])
        self.dr.find_element_by_xpath('//*[@id="startTime"]').clear()
        self.dr.find_element_by_xpath('//*[@id="startTime"]').send_keys(search_value['startTime'])
        self.dr.find_element_by_xpath('//*[@id="endTime"]').clear()
        self.dr.find_element_by_xpath('//*[@id="endTime"]').send_keys(search_value['endTime'])
        # self.dr.find_element_by_xpath('//*[@id="bmmc"]').click()
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(2)

    # 入库记录-查询
    def xdw_rkjl_export(self):
        self.dr.find_element_by_xpath('//*[@id="export"]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        tipEle = self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p')
        self.assertIn('导出成功', tipEle.text)

    #出库记录-查询
    def xdw_ckjl_search(self,search_value):
        self.dr.find_element_by_xpath('//*[@id="wpbh"]').clear()
        self.dr.find_element_by_xpath('//*[@id="wpbh"]').send_keys(search_value['wpbh'])
        self.dr.find_element_by_xpath('//*[@id="wpmc"]').clear()
        self.dr.find_element_by_xpath('//*[@id="wpmc"]').send_keys(search_value['wpmc'])

        self.dr.find_element_by_xpath('//*[@id="wplb"]').click()
        time.sleep(0.5)
        if search_value['wplb']['wpdl']=='':
            self.dr.find_element_by_xpath('//*[@id="treeSelect_1_span"]').click()
        else:
            self.dr.find_element_by_xpath('//*[@id="treeSelect_'+search_value['wplb']['wpdl']+'_switch"]').click()
            time.sleep(0.5)
            self.dr.find_element_by_xpath('//*[@id="treeSelect_'+search_value['wplb']['wpxl']+'_span"]').click()
        self.dr.find_element_by_xpath('//*[@id="startTime"]').clear()
        self.dr.find_element_by_xpath('//*[@id="startTime"]').send_keys(search_value['startTime'])
        self.dr.find_element_by_xpath('//*[@id="endTime"]').clear()
        self.dr.find_element_by_xpath('//*[@id="endTime"]').send_keys(search_value['endTime'])
        Select(self.dr.find_element_by_xpath('//*[@id="ckjglx"]')).select_by_visible_text(search_value['ckjglx'])
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(3)

    # 出库记录-导出
    def xdw_ckjl_export(self):
        self.dr.find_element_by_xpath('//*[@id="export"]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        tipEle = self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p')
        self.assertIn('导出成功', tipEle.text)

    #隔离检疫记录-查询
    def xdw_gljyjl_search(self,search_value):
        self.dr.find_element_by_xpath('//*[@id="jldbh"]').clear()
        self.dr.find_element_by_xpath('//*[@id="jldbh"]').send_keys(search_value['jldh'])
        self.dr.find_element_by_xpath('//*[@id="zjh"]').clear()
        self.dr.find_element_by_xpath('//*[@id="zjh"]').send_keys(search_value['zjh'])
        self.dr.find_element_by_xpath('//*[@id="wpmc"]').clear()
        self.dr.find_element_by_xpath('//*[@id="wpmc"]').send_keys(search_value['wpmc'])
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(2)

    #隔离检疫记录-查看
    def xdw_gljyjl_details(self,search_value):
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]/div/button').click()
        handles = self.dr.window_handles
        self.dr.switch_to.window(handles[-1])
        time.sleep(2)
        self.assertEqual('凭证单打印',self.dr.title)
        self.assertEqual(search_value,self.dr.find_element_by_xpath('/html/body/div[2]/div[2]').text)

    # 隔离检疫记录-导出
    def xdw_gljyjl_export(self):
        self.dr.find_element_by_xpath('//*[@id="export"]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        tipEle = self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p')
        self.assertIn('导出成功', tipEle.text)

    #现场退回记录-查询
    def xdw_xcthjl_search(self,search_value):
        self.dr.find_element_by_xpath('//*[@id="jldbh"]').clear()
        self.dr.find_element_by_xpath('//*[@id="jldbh"]').send_keys(search_value['jldh'])
        self.dr.find_element_by_xpath('//*[@id="zjh"]').clear()
        self.dr.find_element_by_xpath('//*[@id="zjh"]').send_keys(search_value['zjh'])
        self.dr.find_element_by_xpath('//*[@id="wpmc"]').clear()
        self.dr.find_element_by_xpath('//*[@id="wpmc"]').send_keys(search_value['wpmc'])
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(3)

    # 现场退回记录-查看
    def xdw_xcthjl_details(self,search_value):
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[10]/div/button').click()
        handles = self.dr.window_handles
        self.dr.switch_to.window(handles[-1])
        time.sleep(2)
        self.assertEqual('凭证单打印',self.dr.title)
        self.assertEqual(search_value,self.dr.find_element_by_xpath('/html/body/div[2]/div[2]').text)

    # 现场退回记录-导出
    def xdw_xcthjl_export(self):
        self.dr.find_element_by_xpath('//*[@id="export"]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        tipEle = self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p')
        self.assertIn('导出成功', tipEle.text)

    #业务流程查询
    def xdw_ywlccx_search(self,search_value):
        Select(self.dr.find_element_by_xpath('//*[@id="lx"]')).select_by_visible_text(search_value['lx'])
        self.dr.find_element_by_xpath('//*[@id="wpbh"]').clear()
        if search_value['lx'] == '物品记录':
            self.dr.find_element_by_xpath('//*[@id="wpbh"]').send_keys(search_value['wpbh'])
        else:
            self.dr.find_element_by_xpath('//*[@id="wpbh"]').send_keys(search_value['jldh'])
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(3)
        if search_value['lx']=='物品记录':
            self.assertEqual(search_value['wpbh'],self.dr.find_element_by_xpath('//*[@id="list"]/tbody[1]/tr/td[2]').text)
        else:
            self.assertEqual(jld_id,self.dr.find_element_by_xpath('//*[@id="list"]/tbody[1]/tr/td[1]').text)

    #截留物查询-查询
    def xdw_jlwcy_search(self,search_value):
        self.dr.find_element_by_xpath('//*[@id="wpbh"]').clear()
        self.dr.find_element_by_xpath('//*[@id="wpbh"]').send_keys(search_value['wpbh'])
        self.dr.find_element_by_xpath('//*[@id="wpmc"]').clear()
        self.dr.find_element_by_xpath('//*[@id="wpmc"]').send_keys(search_value['wpmc'])
        if search_value['wplb']['wpdl']=='':
            pass
        else:
            self.dr.find_element_by_xpath('//*[@id="wplb"]').click()
            time.sleep(1)
            self.dr.find_element_by_xpath('//*[@id="indexTreeSelect_'+str(search_value['wplb']['wpdl'])+'_switch"]').click()
            time.sleep(1)
            self.dr.find_element_by_xpath('//*[@id="indexTreeSelect_'+str(search_value['wplb']['wpxl'])+'_span"]').click()
        Select(self.dr.find_element_by_xpath('//*[@id="cllx"]')).select_by_visible_text(search_value['cllx'])
        # Select(self.dr.find_element_by_xpath('//*[@id="kaksdm"]')).select_by_visible_text()
        self.dr.find_element_by_xpath('//*[@id="kssj"]').clear()
        self.dr.find_element_by_xpath('//*[@id="kssj"]').send_keys(search_value['kssj'])
        self.dr.find_element_by_xpath('//*[@id="jssj"]').clear()
        self.dr.find_element_by_xpath('//*[@id="jssj"]').send_keys(search_value['jssj'])
        self.dr.find_element_by_xpath('//*[@id="zjh"]').clear()
        self.dr.find_element_by_xpath('//*[@id="zjh"]').send_keys(search_value['zjh'])
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(2)

    #截留物查询-导出
    def xdw_jlwcy_export(self):
        self.dr.find_element_by_xpath('//*[@id="export"]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        tipEle = self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p')
        self.assertIn('导出成功', tipEle.text)

    #旅客记录查询-查询
    def xdw_lkjlcx_search(self,search_value):
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/input').clear()
        self.dr.find_element_by_xpath('//*[@id="form"]/div[1]/input').send_keys(search_value['lkxm'])
        self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/input').clear()
        self.dr.find_element_by_xpath('//*[@id="form"]/div[2]/input').send_keys(search_value['zjh'])
        self.dr.find_element_by_xpath('//*[@id="startTime"]').clear()
        self.dr.find_element_by_xpath('//*[@id="startTime"]').send_keys(search_value['startTime'])
        self.dr.find_element_by_xpath('//*[@id="endTime"]').clear()
        self.dr.find_element_by_xpath('//*[@id="endTime"]').send_keys(search_value['endTime'])
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(1)

    # 旅客记录查询-删除功能
    def xdw_lkjlcx_delete(self):
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[9]/div/button[1]').click()
        time.sleep(1)
        WebDriverWait(self.dr,5,0.2).until(expected_conditions.visibility_of_element_located((By.ID,'dialog-tips')))
        self.assertEqual('确定删除吗？', self.dr.find_element_by_xpath('//*[@id="dialog-tips"]/div').text)
        self.dr.find_element_by_xpath('/html/body/div[6]/div[3]/div/button[2]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        tipEle = self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p')
        self.assertIn('删除成功', tipEle.text)

    # 旅客记录查询-批量删除功能
    def xdw_lkjlcx_Batch_deletion(self):
        self.dr.find_element_by_xpath('//*[@id="list"]/thead/tr/th[1]/div[1]/input').click()
        self.dr.find_element_by_xpath('//*[@id="btnDelete"]').click()
        time.sleep(1)
        WebDriverWait(self.dr, 5, 0.2).until(expected_conditions.visibility_of_element_located((By.ID, 'dialog-tips')))
        self.assertEqual('确定删除吗？',self.dr.find_element_by_xpath('//*[@id="dialog-tips"]/div').text)
        self.dr.find_element_by_xpath('/html/body/div[6]/div[3]/div/button[2]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        tipEle = self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p')
        self.assertIn('删除成功', tipEle.text)

    #截留单查询-查询功能
    def xdw_jldcx_search(self,search_value):
        self.dr.find_element_by_xpath('//*[@id="form"]/div/div[1]/input').clear()
        self.dr.find_element_by_xpath('//*[@id="form"]/div/div[1]/input').send_keys(search_value['jldbh'])
        self.dr.find_element_by_xpath('//*[@id="form"]/div/div[2]/input').clear()
        self.dr.find_element_by_xpath('//*[@id="form"]/div/div[2]/input').send_keys(search_value['ysh'])
        self.dr.find_element_by_xpath('//*[@id="form"]/div/div[3]/input').clear()
        self.dr.find_element_by_xpath('//*[@id="form"]/div/div[3]/input').send_keys(search_value['lkxm'])
        self.dr.find_element_by_xpath('//*[@id="form"]/div/div[4]/input').clear()
        self.dr.find_element_by_xpath('//*[@id="form"]/div/div[4]/input').send_keys(search_value['zjhm'])
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(2)

    # 截留单查询-查询功能
    def xdw_jldcx_details(self):
        self.dr.find_element_by_xpath('//*[@id="list"]/tbody/tr/td[8]/div/button[1]').click()
        time.sleep(1)
        WebDriverWait(self.dr,5,0.2).until(expected_conditions.visibility_of_element_located((By.ID,'dialog-edit')))

    #科室工作量-查询
    def xdw_ksgzl_search(self,search_value):
        self.dr.find_element_by_xpath('//*[@id="kssj"]').clear()
        self.dr.find_element_by_xpath('//*[@id="kssj"]').send_keys(search_value['kssj'])
        self.dr.find_element_by_xpath('//*[@id="jssj"]').clear()
        self.dr.find_element_by_xpath('//*[@id="jssj"]').send_keys(search_value['jssj'])
        # 科室
        # self.dr.find_element_by_xpath('//*[@id="ksmc"]').click()
        # self.dr.find_element_by_xpath('//*[@id="wplb"]').click()
        # time.sleep(1)
        # self.dr.find_element_by_xpath(
        #     '//*[@id="indexTreeSelect_' + str(search_value['wplb']['wpdl']) + '_switch"]').click()
        # time.sleep(1)
        # self.dr.find_element_by_xpath(
        #     '//*[@id="indexTreeSelect_' + str(search_value['wplb']['wpxl']) + '_span"]').click()
        self.dr.find_element_by_xpath('//*[@id="wpmc"]').click()
        self.dr.find_element_by_xpath('//*[@id="wpmc"]').clear()
        self.dr.find_element_by_xpath('//*[@id="wpmc"]').send_keys(search_value['wpmc'])
        self.dr.find_element_by_xpath('//*[@id="jldbh"]').clear()
        self.dr.find_element_by_xpath('//*[@id="jldbh"]').send_keys(search_value['jldbh'])
        Select(self.dr.find_element_by_xpath('//*[@id="cllx"]')).select_by_visible_text(search_value['cllx'])
        self.dr.find_element_by_xpath('//*[@id="lyd"]').clear()
        self.dr.find_element_by_xpath('//*[@id="lyd"]').send_keys(search_value['lyd'])
        self.dr.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(1)

    # 科室工作量-导出
    def xdw_ksgzl_exprot(self):
        self.dr.find_element_by_xpath('//*[@id="export"]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        tipEle = self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p')
        self.assertIn('导出成功', tipEle.text)

    # 科室工作量-打印
    def xdw_ksgzl_print(self):
        self.dr.find_element_by_xpath('//*[@id="open"]').click()
        handles = self.dr.window_handles
        self.dr.switch_to.window(handles[-1])
        self.assertEqual('科室工作量清单',self.dr.find_element_by_xpath('/html/body/div/div/div[1]/div[2]').text)

    # 工作量汇总-导出
    def xdw_gzlhz_exprot(self):
        self.dr.find_element_by_xpath('//*[@id="export"]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        tipEle = self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p')
        self.assertIn('导出成功', tipEle.text)

    #仓库盘点_查询
    def xdw_ckpd_search(self,search_value):
        self.dr.find_element_by_xpath('//*[@id="wpbh"]').clear()
        self.dr.find_element_by_xpath('//*[@id="wpbh"]').send_keys(search_value['wpbh'])
        self.dr.find_element_by_xpath('//*[@id="wpmc"]').clear()
        self.dr.find_element_by_xpath('//*[@id="wpmc"]').send_keys(search_value['wpmc'])
        Select(self.dr.find_element_by_xpath('//*[@id="wpfl"]')).select_by_visible_text(search_value['wpfl'])
        Select(self.dr.find_element_by_xpath('//*[@id="clfs"]')).select_by_visible_text(search_value['clfs'])
        self.dr.find_element_by_xpath('//*[@id="minTime"]').clear()
        self.dr.find_element_by_xpath('//*[@id="minTime"]').send_keys(search_value['minTime'])
        self.dr.find_element_by_xpath('//*[@id="maxTime"]').clear()
        self.dr.find_element_by_xpath('//*[@id="maxTime"]').send_keys(search_value['maxTime'])
        self.dr.find_element_by_xpath('//*[@id="search1"]').click()
        time.sleep(1)

    # 仓库盘点_导出
    def xdw_ckpd_export(self):
        self.dr.find_element_by_xpath('//*[@id="export1"]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        tipEle = self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p')
        self.assertIn('导出成功', tipEle.text)

    #仓库盘点-仓库物品汇总
    def xdw_ckpd_ckwphz(self):
        self.dr.find_element_by_xpath('//*[@id="send"]/span').click()
        time.sleep(2)

    def xdw_ckpd_ckwphz_search(self,search_value):
        Select(self.dr.find_element_by_xpath('//*[@id="wpfl2"]')).select_by_visible_text(search_value['wpfl'])
        self.dr.find_element_by_xpath('//*[@id="minTime2"]').clear()
        self.dr.find_element_by_xpath('//*[@id="minTime2"]').send_keys(search_value['minTime2'])
        self.dr.find_element_by_xpath('//*[@id="maxTime2"]').clear()
        self.dr.find_element_by_xpath('//*[@id="maxTime2"]').send_keys(search_value['maxTime2'])
        self.dr.find_element_by_xpath('//*[@id="search2"]').click()
        time.sleep(1)

    def xdw_ckpd_ckwphz_export(self):
        self.dr.find_element_by_xpath('//*[@id="export2"]').click()
        WebDriverWait(self.dr, 5, 0.2).until(
            expected_conditions.visibility_of_element_located((By.ID, 'gritter-notice-wrapper')))
        tipEle = self.dr.find_element_by_xpath('//*[@id="gritter-notice-wrapper"]/div/div[2]/div[2]/p')
        self.assertIn('导出成功', tipEle.text)

if __name__=='__main__':
    unittest.main()