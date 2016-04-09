# -*- coding:utf-8 -*-
# filename:FlowOperator
# 16/1/20 下午5:11

__author__ = 'bingone'
from yunpian.Config import yunpian_config
from yunpian.model.Result import Result
from yunpian.HttpUtil import request_post


class VoiceOperator(object):
    def __init__(self, apikey=None, api_secret=None):
        if apikey == None:
            raise Exception("please set apikey")
        else:
            self.apikey = apikey
        if api_secret != None:
            self.api_secret = api_secret

    def pull_status(self, data=None):

        if not data:
            data = {}
        data['apikey'] = self.apikey

        return request_post(self,yunpian_config['URI_PULL_VOICE_STATUS'], data)

    def send(self, data=None):
        if not data:
            data = {}
        if 'mobile' not in data:
            return Result(None, 'mobile 为空')
        if 'code' not in data:
            return Result(None, 'code 为空')
        data['apikey'] = self.apikey

        return request_post(self,yunpian_config['URI_SEND_VOICE_SMS'], data)
