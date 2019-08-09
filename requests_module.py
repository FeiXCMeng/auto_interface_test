# -*- coding: UTF-8 -*-
'''
@Auther: ywei
@Date: 2019-07-19
'''
import requests, json

class Requ(object):
    def __init__(self):
        self.headers = {"User-Agent":
                            "Mozilla/5.0 (Windows NT 6.1; WOW64) "
                            "AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/75.0.3770.142 Safari/537.36"}

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
        params = json.dumps(params)
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
    data = {"key1": "values1", "key2": "value2"}
    result = requ.post("http://www.httpbin.org/post", params=data)
    print(result)

