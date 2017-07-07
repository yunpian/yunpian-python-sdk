'''
Created on Jun 19, 2017

@author: dzh
'''

class Result(object):
    ''' 
    API Response Result
    response code => result.code() ==0 if is_succ() else !=0
    code's message => result.msg()
    code's detail => result.detail()
    response data => result.data()
    '''

    def __init__(self, code=Code.OK):
        self.code = code

    def code(self, code=None, rr=False):
        '''
        returns:
            response code(0-success, others-failure) or self
        '''
        if rr or code is None:
            return self.code
        self.code = code
        return self

    def msg(self, msg=None, rr=False):
        '''code's message'''
        if rr or msg is None:
            return self.msg
        self.msg = msg
        return self

    def detail(self, detail=None, rr=False):
        '''code's detail'''
        if rr or detail is None:
            return self.detail
        self.detail = detail
        return self

    def data(self, data, rr=False):
        '''response data'''
        if rr or data is None:
            return self.data
        self.data = data
        return self

    def exception(self, e, rr=False):
        if rr or e is None:
            return self.e
        self.e = e
        return self

    def is_succ(self):
        return self.code == Code.OK;


class Code(object):
    '''
    Code Value
    '''
    # 成功
    OK = 0
    # 请求参数缺失
    ARGUMENT_MISSING = 1
    # 请求参数格式错误
    BAD_ARGUMENT_FORMAT = 2
    # 未知异常
    UNKNOWN_EXCEPTION = -50


