# -*- coding: UTF-8 -*-
'''
@Auther: ywei
@Date: 2019-07-19
'''
import requests, json
from get_excel import  get_excel

class Requ(object):
    def __init__(self):
        self.headers = {
                        "Content-Type": "application/json"
                        }

    def get(self, url, params):
        try:
            r = requests.get(url, params=params, headers=self.headers)
            r.encoding = 'UTF-8'
            json_response = json.loads(r.text)
            return {"code": 0, "result": json_response}
        except Exception as e:
            return {"code": 1, "result": "请求出错，出错原因是 %s" %e}

    def post(self, url, params):
        #dumps方法把Python对象转变成字符串
        # param = json.loads(params)
        try:
            r = requests.post(url, data=params, headers=self.headers)
            r.encoding = 'UTF-8'
            #loads方法把json字符串转变成Python对象
            json_response = json.loads(r.text)
            return {"code": 0, "result": json_response}
        except Exception as e:
            return {"code": 1, "result": "请求出错，出错原因是 %s" %e}

if __name__ == '__main__':

    requ = Requ()
    ids, url, params, method, result = get_excel(".\\interface.xlsx")
    # param = {
    #         "limit":10,
    #         "requestId":"bce3bb51-4ea6-4e8b-8268-584a4b2cc766",
    #         "userId":"80115209734401911"
    #         }
    # param = json.loads(params[0])
    print(type(params[0]))
    result = requ.post("http://116.62.33.250:8100/feed/notification/list", params=params[0])
    print(result)

