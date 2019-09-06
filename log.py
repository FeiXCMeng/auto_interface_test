# -*- coding: UTF-8 -*-
'''
@Auther: ywei
@Date: 2019-09-04
'''
import logging, sys, os, time
from functools import wraps

base_path = '.'
LOG_DIR = os.path.join(base_path, 'log')
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)

date_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
# logging.basicConfig(filename='./log.log', filemode='w',
#                     format='[%(levelname)s]: %(message)s',
#                     datefmt='[%a %d %b %Y %H:%M:%S]',level=logging.INFO)
# logger_name = 'demo'

LOG = logging.getLogger(__name__)

handler_stream = logging.StreamHandler()
handler_file = logging.FileHandler(filename='%s/%s-log.log' %(LOG_DIR, date_time), mode='w')

LOG.setLevel(logging.INFO)
handler_stream.setLevel(logging.INFO)
handler_file.setLevel(logging.INFO)

fomatter = logging.Formatter("[%(name)s-%(levelname)s-%(asctime)s]: %(message)s")
handler_stream.setFormatter(fomatter)
handler_file.setFormatter(fomatter)

LOG.addHandler(handler_stream)
LOG.addHandler(handler_file)

'''
如果将日志保存在一个文件中，那么时间一长，或者日志一多，单个日志文件就会很大，
既不利于备份，也不利于查看。我们会想到能不能按照时间或者大小对日志文件进行划分呢？
答案肯定是可以的，并且还很简单，logging 考虑到了我们这个需求。
logging.handlers 文件中提供了 TimedRotatingFileHandler 和 RotatingFileHandler 类
分别可以实现按时间和大小划分。
打开这个 handles 文件，可以看到还有其他功能的 Handler 类，它们都继承自基类 BaseRotatingHandler

每隔 1000 Byte 划分一个日志文件，备份文件为 3 个
file_handler = logging.handlers.RotatingFileHandler("test.log", mode="w", maxBytes=1000, backupCount=3, encoding="utf-8")
每隔 1小时 划分一个日志文件，interval 是时间间隔，备份文件为 10 个
handler2 = logging.handlers.TimedRotatingFileHandler("test.log", when="H", interval=1, backupCount=10)

'''


def logger(param):
    def wrap(function):
        @wraps(function)
        def _wrap(*args, **kwargs):
            LOG.info("Current Module : %s" %(param))
            return function(*args, **kwargs)
        return _wrap
    return wrap