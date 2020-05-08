import cx_Oracle # 导入数据库
import pandas as pd #导入操作数据集工具
from sqlalchemy import create_engine #导入 sqlalchemy 库,然后建立数据库连接
import time #导入时间模块
import numpy as np #导入numpy数值计算扩展
import os

os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.AL32UTF8' #保证select出来的中文显示没有问题

def mk(user,passwor,dbname,sql):
    db=cx_Oracle.connect(user,passwor,dbname)
    cur = db.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    mk = {}
    for i in range(0, len(rows)):
        mk[rows[i][1]] = rows[i][0]
    return mk
    db.close()

username='NBHG'
password='123456'
dbname='192.168.5.91:1521/ORCL'
sql="select MKID,MKXSMC from ACC_T_MK where ZCXTID='ciqxdw'"

data=mk(username,password,dbname,sql)
# print(data)
