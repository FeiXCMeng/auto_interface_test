# -*- coding: UTF-8 -*-
'''
@Auther: ywei
@Date: 2019-07-27
'''
# from get_excel import *
# from requests_module import *

def assert_method(except_result, json_data):
    data = str(except_result).split('&')
    result = dict([(item.split('=')) for item in data])
    value1 = ([str(json_data[key]) for key in result.keys()])
    value2 = ([str(value) for value in result.values()])

    if value1 == value2:
        return {"code": 0, "result": "sucess"}
    else:
        return {"code": 1, "result": "fail"}

if __name__ == '__main__':
    except_result = "code=200&name=a"
    json_data = {"code": 500, "name": "a"}
    print(assert_method(except_result, json_data))