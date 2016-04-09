# -*- coding:utf-8 -*-
# filename:SmsOperator
# 16/1/20 下午4:22

__author__ = 'bingone'
import urllib
from yunpian.Config import yunpian_config
from yunpian.model.Result import Result
from yunpian.HttpUtil import request_post


class SmsOperator(object):
    def __init__(self, apikey=None, api_secret=None):
        if apikey == None:
            raise Exception("please set apikey")
        else:
            self.apikey = apikey
        if api_secret != None:
            self.api_secret = api_secret

    def single_send(self, data=None):

        if not data:
            data = {}
        if 'mobile' not in data:
            return Result(None, 'mobile 为空')
        if 'text' not in data:
            return Result(None, 'text 为空')

        data['apikey'] = self.apikey

        return request_post(self,yunpian_config['URI_SEND_SINGLE_SMS'], data)

    def batch_send(self, data=None):

        if not data:
            data = {}
        if 'mobile' not in data:
            return Result(None, 'mobile 为空')
        if 'text' not in data:
            return Result(None, 'text 为空')

        data['apikey'] = self.apikey

        return request_post(self,yunpian_config['URI_SEND_BATCH_SMS'], data)

    def multi_send(self, data=None):
        if not data:
            data = {}
        if 'mobile' not in data:
            return Result(None, 'mobile 为空')
        if 'text' not in data:
            return Result(None, 'text 为空')
        data['apikey'] = self.apikey
        mobile = data['mobile']
        text = data['text']
        if len(str(mobile).split(',')) != len(str(text).split(',')):
            return Result(None, 'mobile 与 text 个数不匹配')
        data['text'] = ''
        for s in str(text).split(','):
            data['text'] += urllib.quote(s) + ','
        data['text'] = data['text'][0:-1]
        return request_post(self,yunpian_config['URI_SEND_MULTI_SMS'], data)

    def tpl_single_send(self, data=None):
        if not data:
            data = {}
        if 'mobile' not in data:
            return Result(None, 'mobile 为空')
        if 'tpl_id' not in data:
            return Result(None, 'tpl_id 为空')
        if 'tpl_value' not in data:
            return Result(None, 'tpl_value 为空')
        data['apikey'] = self.apikey

        return request_post(self,yunpian_config['URI_SEND_TPL_SINGLE_SMS'], data)

    def tpl_batch_send(self, data=None):
        if not data:
            data = {}
        if 'mobile' not in data:
            return Result(None, 'mobile 为空')
        if 'tpl_id' not in data:
            return Result(None, 'tpl_id 为空')
        if 'tpl_value' not in data:
            return Result(None, 'tpl_value 为空')
        data['apikey'] = self.apikey

        return request_post(self,yunpian_config['URI_SEND_TPL_BATCH_SMS'], data)