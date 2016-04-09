# -*- coding:utf-8 -*-
# filename:FlowOperator
# 16/1/20 下午5:30

__author__ = 'bingone'
from yunpian.Config import yunpian_config
from yunpian.model.Result import Result
from yunpian.HttpUtil import request_post


class TplOperator(object):
    def __init__(self, apikey=None, api_secret=None):
        if apikey == None:
            raise Exception("please set apikey")
        else:
            self.apikey = apikey
        if api_secret != None:
            self.api_secret = api_secret

    def get_default(self, data=None):
        if not data:
            data = {}
        data['apikey'] = self.apikey

        return request_post(self,yunpian_config['URI_GET_DEFAULT_TEMPLATE'], data)

    def get(self, data=None):
        if not data:
            data = {}
        data['apikey'] = self.apikey

        return request_post(self,yunpian_config['URI_GET_TEMPLATE'], data)

    def add(self, data=None):
        if not data:
            data = {}
        if 'tpl_content' not in data:
            return Result(None, 'tpl_content 为空')
        data['apikey'] = self.apikey

        return request_post(self,yunpian_config['URI_ADD_TEMPLATE'], data)

    def upd(self, data=None):
        if not data:
            data = {}
        if 'tpl_id' not in data:
            return Result(None, 'tpl_id 为空')
        if 'tpl_content' not in data:
            return Result(None, 'tpl_content 为空')
        data['apikey'] = self.apikey

        return request_post(self,yunpian_config['URI_UPD_TEMPLATE'], data)

    def delete(self, data=None):
        if not data:
            data = {}
        if 'tpl_id' not in data:
            return Result(None, 'tpl_id 为空')
        data['apikey'] = self.apikey

        return request_post(self,yunpian_config['URI_DEL_TEMPLATE'], data)
