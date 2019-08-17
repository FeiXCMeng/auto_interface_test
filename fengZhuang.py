# -*- coding: UTF-8 -*-
'''
@Auther: ywei
@Date: 2019-07-23
'''
from requests_module import Requ
from get_excel import get_excel

requ = Requ()

class TestApi(object):
    def __init__(self, url, params, method, result):
        self.url = url
        self.params = params
        self.method = method
        self.result = result

    def test_api(self):
        if self.method.upper() == 'GET':
            self.response = requ.get(self.url, self.params)
        elif self.method.upper() == 'POST':
            self.response = requ.post(self.url, self.params)
        else:
            return "未知的http方法"
        return self.response

if __name__ == '__main__':
    ids, url, params, method, result = get_excel(".\\interface.xlsx")
    print(url[0], params[0], method[0], result[0])
    api = TestApi(url[0], params[0], method[0], result[0])
    print(api.test_api())




