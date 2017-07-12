# -*- coding: utf-8 -*-
'''
Created on Jun 19, 2017

@author: dzh
'''
class Code(object):
    '''Code Value'''
    # 成功
    SUCC = 0
    # 请求参数缺失
    ARGUMENT_MISSING = 1
    # 请求参数格式错误
    BAD_ARGUMENT_FORMAT = 2
    # 未知异常
    UNKNOWN_EXCEPTION = -50

class Result(object):
    '''API Response Result
    response code => result.code() 0 if is_succ() else !=0
    code's message => result.msg()
    code's detail => result.detail()
    response data => result.data()
    '''

    def __init__(self, code=Code.SUCC):
        self._code = code
        self._msg = None
        self._data = None
        self._detail = None
        self._err = None

    def code(self, code=None, ret_r=False):
        '''
        Args:
            code: (Optional) set code
            ret_r: (Optional) force to return Result. Default value is False
        returns:
            response code(0-success, others-failure) or self
        '''
        if code or ret_r:
            self._code = code
            return self
        return self._code

    def msg(self, msg=None, ret_r=False):
        '''code's message'''
        if msg or ret_r:
            self._msg = msg
            return self
        return self._msg

    def detail(self, detail=None, ret_r=False):
        '''code's detail'''
        if detail or ret_r:
            self._detail = detail
            return self
        return self._detail

    def data(self, data=None, ret_r=False):
        '''response data'''
        if data or ret_r:
            self._data = data
            return self
        return self._data

    def exception(self, err=None, ret_r=False):
        if err or ret_r:
            self._err = err
            return self
        return self._err

    def is_succ(self):
        return self._code == Code.SUCC
