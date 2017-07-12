# -*- coding: utf-8 -*-
'''
Created on Jul 4, 2017

@author: dzh
'''
import unittest

import requests
from yunpian_python_sdk.model.constant import YP_VERSION, HTTP_CONN_TIMEOUT
from yunpian_python_sdk.ypclient import _YunpianConf


class TestYunpianClient(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def test_YunpianConf(self):
        print(__name__)
        conf = _YunpianConf()
        self.assertEqual(conf.conf(YP_VERSION), "v2")
        self.assertEqual(conf.conf(HTTP_CONN_TIMEOUT), "10")

    def test_uri(self):
        url = '{}/{}/{}/{}'.format('https://test-api.yunpian.com', 'v2', 'user', 'get.json')
        self.assertEqual('https://test-api.yunpian.com/v2/user/get.json', url)


    def test_name(self):
        import sys
        self.assertEqual('tests.test_ypclient', sys.modules[__name__].__name__)

    def test_requests(self):
        r = requests.get('https://github.com/dzh')
        print(r.status_code)

        r = requests.get('https://www.yunpian.com/')
        print(r.status_code)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

