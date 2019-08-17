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
        params = eval(params)
        try:
            '''
            在Python中，json对应的Python的数据类型是字符串
                需要注意的是python中并没有json类型这一说法，
                通过json.dumps(<dict>)转换的字典对象，
                最后得到的是一个字符串对象，
                也就是说，在python中json格式的数据实际上就是一个字符串
                
            post方法有两种参数，data和json两种类型，data的对象则是Python中的字典类型
            url = xxx
            data = {
                'a': 1,
                 'b': 2,
            }
            
            # 1
            requests.post(url, data=json.dumps(data))
            data接受的json格式的，json格式在Python中对应的是一个字符串，所以
            在读取Excel里面的元素后，得到的是一个'{}'这种格式的字符串，实际上是一个json格式
            
            # 2-json参数会自动将字典类型的对象转换为json格式,
            requests.post(url, json=data)
            这时候，传递的data必须是dict类型的（字符串转dict，必须用eval()）
            '''
            # r = requests.post(url, data=params, headers=self.headers)
            r = requests.post(url, json=params, headers=self.headers)
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
    # param = eval(params[0])
    param = params[0]
    result = requ.post("http://116.62.33.250:8100/feed/notification/list", params=param)
    print(result)

