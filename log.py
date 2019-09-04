# -*- coding: UTF-8 -*-
'''
@Auther: ywei
@Date: 2019-09-04
'''
import logging, sys
from functools import wraps

logging.basicConfig(filename='./log.log', filemode='w',
                    format='[%(levelname)s]: %(message)s',
                    datefmt='[%a %d %b %Y %H:%M:%S]',level=logging.INFO)
logger_name = 'demo'
LOG = logging.getLogger(logger_name)

def logger(param):
    def wrap(function):
        @wraps(function)
        def _wrap(*args, **kwargs):
            LOG.info("Current Module : %s" %(param))
            return function(*args, **kwargs)
        return _wrap
    return wrap