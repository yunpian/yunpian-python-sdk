'''
Created on Jul 4, 2017

@author: dzh
'''
import sys
import unittest

from sdk.model.constant import YP_VERSION, HTTP_CONN_TIMEOUT
from sdk.ypclient import _YunpianConf


class TestYunpianClient(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def testYunpianConf(self):
        print(__name__)
        conf = _YunpianConf()
        self.assertEqual(conf.conf(YP_VERSION), "v2")
        self.assertEqual(conf.conf(HTTP_CONN_TIMEOUT), "10")

    def testUri(self):
        url = '{}/{}/{}/{}'.format('https://test-api.yunpian.com', 'v2', 'user', 'get.json')
        self.assertEqual('https://test-api.yunpian.com/v2/user/get.json', url)

    def testName(self):
        print(sys.modules[__name__])

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

