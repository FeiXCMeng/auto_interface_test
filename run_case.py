# -*- coding: UTF-8 -*-
'''
@Auther: ywei
@Date: 2019-08-17
'''
import os, time
from fengZhuang import TestApi
from get_excel import get_excel
from assert_method import assert_method

def test_interface():
    path = os.getcwd() + '\\interface.xlsx'
    ids, url, params, method, result = get_excel(path)
    for i in range(len(ids)):
        api = TestApi(url=url[i], params=params[i], method=method[i], result=result[i])
        api_json = api.test_api()
        json_data = api_json['result']
        assert_result = assert_method(except_result=result[i], json_data=json_data)
        if assert_result['code'] == 0:
            print('success')
        else:
            print('fail')

if __name__ == '__main__':
    test_interface()