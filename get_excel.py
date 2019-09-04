# -*- coding: UTF-8 -*-
'''
@Auther: ywei
@Date: 2019-07-24
'''
import xlrd
from log import *

def get_excel(filePath):
    ids = []
    url = []
    params = []
    method = []
    result = []

    try:
        file = xlrd.open_workbook(filePath)
        sheet = file.sheets()[0]

        for i in range(1, sheet.nrows):
            ids.append(sheet.cell(i, 0).value)
            url.append(sheet.cell(i, 1).value)
            params.append(sheet.cell(i, 2).value)
            method.append(sheet.cell(i, 3).value)
            result.append(sheet.cell(i, 4).value)

        return ids, url, params, method, result
    except Exception as e:
        # return {"code": 1, "result": "文件打开失败，失败原因：%s" %e}
        LOG.info("文件打开失败，失败原因：%s" %e)

if __name__ == '__main__':
    ids, url, params, method, result = get_excel(".\\interface.xlsx")
    for i in range(len(url)):
        print(method[i])