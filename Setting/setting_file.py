import unittest
import re
import time
import xlrd
import os
# from Setting.setting_file import url,login_name_user1,login_name_password1
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from Setting.menu import mk


'''---------------------------------------脚本基本配置------------------------------------------------------------------'''

#测试地址
url='http://192.168.111.8:8089/ciqxdw/login'

#一般用户
login_name_user1='hl2'
login_name_password1='123456'

#科长
login_name_user2='hl3'
login_name_password2='123456'

#口岸领导
login_name_user3='hl4'
login_name_password3='123456'

#其他科室科员
login_name_user4='hl5'
login_name_password4='123456'


'''-----------------------------------------数据库链接------------------------------------------------------------------'''
username='NBHG'
password='123456'
dbname='192.168.5.91:1521/ORCL'
sql="select MKID,MKXSMC from ACC_T_MK where ZCXTID='ciqxdw'"

'''-----------------------------------------目录配置--------------------------------------------------------------------'''
dir_file = os.getcwd()
work_space=r'E:\胡亮\项目工作安排\测试文件svn\web自动化\携带物2.0'
setting_xls=r'E:\胡亮\项目工作安排\测试文件svn\web自动化\携带物2.0\Setting\Testdata.xlsx'

# export_file=r'C:\Users\Administrator\Downloads\\'
# file_list=[]
# for files in os.listdir(r'C:\Users\Administrator\Downloads\\'):
#     if os.path.splitext(files)[1]=='.xls':
#         file_list.append(files)
#
# file_list=sorted(file_list, key=lambda x: os.path.getmtime(os.path.join(r'C:\Users\Administrator\Downloads\\', x)))
# print(file_list)


'''-----------------------------------------公告函数--------------------------------------------------------------------'''

def findnum(string):
    comp = re.compile('-?[1-9]\d*')
    list_str = comp.findall(string)
    list_num = []
    for item in list_str:
        item = int(item)
        list_num.append(item)
    # print(list_num)
    return list_num


'''-----------------------------------------公告类--------------------------------------------------------------------'''
class xdw_TestCase(unittest.TestCase):

    def setUp(self):
        #打开Chrome浏览器
        self.dr=webdriver.Chrome()
        #最大化google浏览器窗口
        self.dr.maximize_window()

    def tearDown(self):
        #关闭浏览器
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

    def login_keyuan(self,user,password):
        #跳转到指定的链接
        self.dr.get(url)
        #输入用户名
        self.dr.find_element_by_xpath('//*[@id="username"]').send_keys(user)
        #输入密码
        self.dr.find_element_by_xpath('//*[@id="password"]').send_keys(password)
        #登陆
        self.dr.find_element_by_xpath('//*[@id="tijiao"]').click()
        time.sleep(2)
        #校验同组人员弹框来判断登陆是否正常和员工登陆时选择同组人员弹框是否会自动弹出
        self.assertEqual('选择同组人员',self.dr.find_element_by_xpath('//*[@id="selectTzry"]').text)
        # self.dr.find_element_by_xpath('//*[@id="selectTzry"]').click()
        time.sleep(1)
        Select(self.dr.find_element_by_xpath('//*[@id="tzryms2side__sx"]')).select_by_value('koujun')
        self.dr.find_element_by_xpath('//*[@id="tzryForm"]/div[1]/div/div[2]/p[1]').click()
        self.dr.find_element_by_xpath('/html/body/div[9]/div[3]/div/button[2]').click()
        time.sleep(2)
        self.assertIn('同组人员',self.dr.find_element_by_xpath('//*[@id="navSearch"]').text)

    '''
       查询功能数据校验：hl-胡亮
       paginal_number：“显示第 1 到第 2 条记录，总共 2 条记录”；运用findnum函数取出数据条数
       search_value：查询值，传入函数是为了做查询功能正常与否的校验
       column：校验数据在表单中的列数
       type:分页样式xpath
       '''

    def pagination_num(self, search_num, search_value, column,type):
        number = findnum(search_num)[-1]
        # print(number)
        tens = int(number / 10)
        single = int(number % 10)

        if tens == 0:
            for j in range(1, single + 1):
                xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
        if tens == 1:
            if single == 0:
                for j in range(1, 11):
                    xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                    self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
                    time.sleep(0.5)
            else:
                for j in range(1, 11):
                    xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                    self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
                if type==0:
                    page = '/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[2]/ul/li[' + str(tens + 3) + ']/a'
                    self.dr.find_element_by_xpath(page).click()
                elif type==1:
                    page = '//*[@id="3lists"]/div[2]/div[1]/div/div[4]/div[2]/ul/li['+ str(tens + 3) +']/a'
                    self.dr.find_element_by_xpath(page).click()
                elif type==2:
                    page = '/html/body/div[1]/div/div[3]/div/div[1]/div/div[4]/div[2]/ul/li['+ str(tens + 3) +']/a'
                    self.dr.find_element_by_xpath(page).click()
                elif type==3:
                    page = '//*[@id="tbList"]/div[2]/div[1]/div/div[4]/div[2]/ul/li['+ str(tens + 3) +']/a'
                    self.dr.find_element_by_xpath(page).click()
                elif type==4:
                    page = '//*[@id="tbList"]/div/div[1]/div/div[4]/div[2]/ul/li['+ str(tens + 3) +']/a'
                    self.dr.find_element_by_xpath(page).click()
                elif type==5:
                    page = '/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/div[2]/ul/li['+ str(tens + 3) +']/a'
                    self.dr.find_element_by_xpath(page).click()
                elif type==6:
                    page = '/html/body/div[1]/div/div/div/div[1]/div/div[4]/div[2]/ul/li['+ str(tens + 3) +']/a'
                    self.dr.find_element_by_xpath(page).click()
                elif type==7:
                    page = '/html/body/div[1]/div/div/div[2]/div[1]/div/div[4]/div[2]/ul/li['+ str(tens + 3) +']/a'
                    self.dr.find_element_by_xpath(page).click()
                elif type==8:
                    page = '//*[@id="tbList"]/div[1]/div[1]/div/div[4]/div[2]/ul/li['+ str(tens + 3) +']/a'
                    self.dr.find_element_by_xpath(page).click()
                elif type==10:
                    page = '//*[@id="pageControltable"]/li['+ str(tens + 2) +']/a'
                    self.dr.find_element_by_xpath(page).click()
                else:
                    pass
                time.sleep(0.5)
                if single == 0:
                    print(single)
                else:
                    for j in range(1, single + 1):
                        xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                        self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
                        time.sleep(0.5)
        if 1 < tens < 7:
            for i in range(1, tens + 2):
                if single == 0:
                    if i < tens + 1:
                        for j in range(1, 11):
                            xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                            self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
                            time.sleep(0.5)
                        if type == 0:
                            page = '/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[2]/ul/li[' + str(
                                tens + 2) + ']/a'
                            self.dr.find_element_by_xpath(page).click()
                        elif type == 1:
                            page = '//*[@id="3lists"]/div[2]/div[1]/div/div[4]/div[2]/ul/li[' + str(tens + 2) + ']/a'
                            self.dr.find_element_by_xpath(page).click()
                        elif type == 2:
                            page = '/html/body/div[1]/div/div[3]/div/div[1]/div/div[4]/div[2]/ul/li[' + str(
                                tens + 2) + ']/a'
                            self.dr.find_element_by_xpath(page).click()
                        elif type == 3:
                            page = '//*[@id="tbList"]/div[2]/div[1]/div/div[4]/div[2]/ul/li[' + str(tens + 2) + ']/a'
                            self.dr.find_element_by_xpath(page).click()
                        elif type == 4:
                            page = '//*[@id="tbList"]/div/div[1]/div/div[4]/div[2]/ul/li[' + str(tens + 2) + ']/a'
                            self.dr.find_element_by_xpath(page).click()
                        elif type == 5:
                            page = '/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/div[2]/ul/li[' + str(
                                tens + 2) + ']/a'
                            self.dr.find_element_by_xpath(page).click()
                        elif type == 6:
                            page = '/html/body/div[1]/div/div/div/div[1]/div/div[4]/div[2]/ul/li[' + str(
                                tens + 2) + ']/a'
                            self.dr.find_element_by_xpath(page).click()
                        elif type == 7:
                            page = '/html/body/div[1]/div/div/div[2]/div[1]/div/div[4]/div[2]/ul/li[' + str(
                                tens + 2) + ']/a'
                            self.dr.find_element_by_xpath(page).click()
                        elif type == 8:
                            page = '//*[@id="tbList"]/div[1]/div[1]/div/div[4]/div[2]/ul/li[' + str(tens + 2) + ']/a'
                            self.dr.find_element_by_xpath(page).click()
                        elif type == 10:
                            if i == 1:
                                page = '//*[@id="pageControltable"]/li[' + str(tens + 1) + ']/a'
                            else:
                                page = '//*[@id="pageControltable"]/li[' + str(tens + 3) + ']/a'
                            self.dr.find_element_by_xpath(page).click()
                        else:
                            pass
                        time.sleep(0.5)
                    if i == tens + 1:
                        for j in range(1, single + 1):
                            if single == 0:
                                print(single)
                            else:
                                for j in range(1, single + 1):
                                    xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                                    self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
                                    time.sleep(0.5)
                else:
                    if i < tens + 1:
                        for j in range(1, 11):
                            xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                            self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
                            time.sleep(0.5)
                        if type == 0:
                            page = '/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[2]/ul/li[' + str(
                                tens + 3) + ']/a'
                            self.dr.find_element_by_xpath(page).click()
                        elif type == 1:
                            page = '//*[@id="3lists"]/div[2]/div[1]/div/div[4]/div[2]/ul/li[' + str(tens + 3) + ']/a'
                            self.dr.find_element_by_xpath(page).click()
                        elif type == 2:
                            page = '/html/body/div[1]/div/div[3]/div/div[1]/div/div[4]/div[2]/ul/li[' + str(
                                tens + 3) + ']/a'
                            self.dr.find_element_by_xpath(page).click()
                        elif type == 3:
                            page = '//*[@id="tbList"]/div[2]/div[1]/div/div[4]/div[2]/ul/li[' + str(tens + 3) + ']/a'
                            self.dr.find_element_by_xpath(page).click()
                        elif type == 4:
                            page = '//*[@id="tbList"]/div/div[1]/div/div[4]/div[2]/ul/li[' + str(tens + 3) + ']/a'
                            self.dr.find_element_by_xpath(page).click()
                        elif type == 5:
                            page = '/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/div[2]/ul/li[' + str(
                                tens + 3) + ']/a'
                            self.dr.find_element_by_xpath(page).click()
                        elif type == 6:
                            page = '/html/body/div[1]/div/div/div/div[1]/div/div[4]/div[2]/ul/li[' + str(
                                tens + 3) + ']/a'
                            self.dr.find_element_by_xpath(page).click()
                        elif type == 7:
                            page = '/html/body/div[1]/div/div/div[2]/div[1]/div/div[4]/div[2]/ul/li[' + str(
                                tens + 3) + ']/a'
                            self.dr.find_element_by_xpath(page).click()
                        elif type == 8:
                            page = '//*[@id="tbList"]/div[1]/div[1]/div/div[4]/div[2]/ul/li[' + str(tens + 3) + ']/a'
                            self.dr.find_element_by_xpath(page).click()
                        elif type == 10:
                            if i == 1:
                                page = '//*[@id="pageControltable"]/li[' + str(tens + 2) + ']/a'
                            else:
                                page = '//*[@id="pageControltable"]/li[' + str(tens + 4) + ']/a'
                            self.dr.find_element_by_xpath(page).click()
                        else:
                            pass
                        time.sleep(2)
                    if i == tens + 1:
                        for j in range(1, single + 1):
                            if single == 0:
                                print(single)
                            else:
                                for j in range(1, single + 1):
                                    xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                                    self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
        if tens >= 7:
            for i in range(1, tens + 2):
                if i < tens + 1:
                    for j in range(1, 11):
                        xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                        self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
                        time.sleep(0.5)
                    if type == 0:
                        page = '/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[2]/ul/li[9]/a'
                        self.dr.find_element_by_xpath(page).click()
                    elif type == 1:
                        page = '//*[@id="3lists"]/div[2]/div[1]/div/div[4]/div[2]/ul/li[9]/a'
                        self.dr.find_element_by_xpath(page).click()
                    elif type == 2:
                        page = '/html/body/div[1]/div/div[3]/div/div[1]/div/div[4]/div[2]/ul/li[9]/a'
                        self.dr.find_element_by_xpath(page).click()
                    elif type == 3:
                        page = '//*[@id="tbList"]/div[2]/div[1]/div/div[4]/div[2]/ul/li[9]/a'
                        self.dr.find_element_by_xpath(page).click()
                    elif type == 4:
                        page = '//*[@id="tbList"]/div/div[1]/div/div[4]/div[2]/ul/li[9]/a'
                        self.dr.find_element_by_xpath(page).click()
                    elif type == 5:
                        page = '/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/div[2]/ul/li[9]/a'
                        self.dr.find_element_by_xpath(page).click()
                    elif type == 6:
                        page = '/html/body/div[1]/div/div/div/div[1]/div/div[4]/div[2]/ul/li[9]/a'
                        self.dr.find_element_by_xpath(page).click()
                    elif type == 7:
                        page = '/html/body/div[1]/div/div/div[2]/div[1]/div/div[4]/div[2]/ul/li[9]/a'
                        self.dr.find_element_by_xpath(page).click()
                    elif type == 8:
                        page = '//*[@id="tbList"]/div[1]/div[1]/div/div[4]/div[2]/ul/li[9]/a'
                        self.dr.find_element_by_xpath(page).click()
                    elif type == 10:
                        if i == 1:
                            page = '//*[@id="pageControltable"]/li[' + str(tens + 1) + ']/a'
                        else:
                            page = '//*[@id="pageControltable"]/li[10]/a'
                        self.dr.find_element_by_xpath(page).click()
                    else:
                        pass
                    time.sleep(0.5)
                if i == tens + 1:
                    for j in range(1, single + 1):
                        if single == 0:
                            pass
                        else:
                            for j in range(1, single + 1):
                                xpath = '//*[@id="list"]/tbody/tr[' + str(j) + ']/td[' + str(column) + ']'
                                self.assertIn(search_value, self.dr.find_element_by_xpath(xpath).text, '校验查询结果')
                                time.sleep(0.5)

    # def export(self,search_num,search_value,column):
    #     number = findnum(search_num)[-1]
    #     for i in range(1,number+1):



if __name__=='__main__':
    unittest.main()