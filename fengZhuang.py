# -*- coding: UTF-8 -*-
'''
@Auther: ywei
@Date: 2019-07-23
'''
from .requests_module import Requ

requ = Requ()

class TestApi(object):
    def __init__(self, url, params, method, result):
        self.url = url
        self.params = params
        self.method = method
        self.result = result

    def test_api(self):
        if self.method == 'GET':
            self.response = requ.get(self.url, self.params)
        elif self.method == 'POST':
            self.response = requ.post(self.url, self.params)
        else:
            return "未知的http方法"
        return self.response




