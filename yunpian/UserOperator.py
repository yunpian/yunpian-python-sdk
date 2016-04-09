# -*- coding:utf-8 -*-
# filename:FlowOperator
# 16/1/20 下午5:10

__author__ = 'bingone'
from yunpian.Config import yunpian_config
from yunpian.HttpUtil import request_post


class UserOperator(object):
    def __init__(self, apikey=None, api_secret=None):
        if apikey == None:
            raise Exception("please set apikey")
        else:
            self.apikey = apikey
        if api_secret != None:
            self.api_secret = api_secret

    def get(self, data=None):

        if not data:
            data = {}
        data['apikey'] = self.apikey

        return request_post(self,yunpian_config['URI_GET_USER_INFO'], data)

    def set(self, data=None):

        if not data:
            data = {}
        data['apikey'] = self.apikey

        return request_post(self,yunpian_config['URI_SET_USER_INFO'], data)
