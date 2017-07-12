# -*- coding: utf-8 -*-
'''
Created on Jul 4, 2017

@author: dzh
'''
import unittest

from yunpian_python_sdk.model.constant import (
    YP_FLOW_HOST, YP_SIGN_HOST, YP_SMS_HOST, YP_TPL_HOST, YP_USER_HOST, YP_VOICE_HOST)
from yunpian_python_sdk.ypclient import YunpianClient


class TestYunpianApi(unittest.TestCase):

    APIKEY = '******'

    CONF = {YP_FLOW_HOST:'https://test-api.yunpian.com', YP_SIGN_HOST:'https://test-api.yunpian.com',
            YP_SMS_HOST:'https://test-api.yunpian.com', YP_TPL_HOST:'https://test-api.yunpian.com',
            YP_USER_HOST:'https://test-api.yunpian.com', YP_VOICE_HOST:'https://test-api.yunpian.com'}

    def setUp(self):
        self._clnt = YunpianClient(TestYunpianApi.APIKEY, TestYunpianApi.CONF)
        pass


    def tearDown(self):
        pass

    def toJson(self, obj):
        import json
        return json.dumps(obj.__dict__)

    def show(self, obj):
        print(self.toJson(obj))


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
