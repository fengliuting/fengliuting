# -*- coding:utf8 -*-
import os
import sys

import openpyxl
'''
关键字驱动+Excel数据驱动
'''
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from base.base_fuc import WebDemo

excel=openpyxl.load_workbook('../teseCase/demo01.xlsx')

sheets=excel.sheetnames
for sheet1 in sheets:
    sheet=excel[sheet1]
    # print(sheet)
    # print(sheet.values)
    for values in sheet.values:
        # print(values)
        params={}
        params['name']=values[2]
        params['value']=values[3]
        params['txt']=values[4]
        if type(values[0]) is int:
            if values[1] == 'browser':
                wd=WebDemo()
            else:
                getattr(wd,values[1])(**params)

        else:
            pass