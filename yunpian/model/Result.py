# -*- coding:utf-8 -*-
#filename:Result
#16/1/20 下午3:47

__author__ = 'bingone'
import json
class Result(object):
    """
    Attributes:
        request_data: dict变量 发送数据
        status_code: 整数变量，响应状态码
        content:   字符串变量，响应的body
        error:       字符串变量，响应的错误内容
    """

    def __init__(self, request_data,response, exception=None):
        self.request_data=request_data
        self.response = response
        self.exception = exception
        self.error = None
        if response is None:
            self.status_code = -1
            self.content = None
            self.error = str(exception)
        else:
            self.status_code = response.status_code
            try:
                self.content = json.loads(response.text,encoding='utf8')
            except Exception as e:
                self.error = str(e)
                self.content = response.text


    def ok(self):
        return self.status_code == 200

    def connect_failed(self):
        return self.__response is None

    def __str__(self):
        return ', '.join(['%s:%s' % item for item in self.__dict__.items()])

    def __repr__(self):
        return self.__str__()