'''
Created on Jul 4, 2017

@author: dzh
'''
import unittest

from sdk.model.constant import YunpianConstant as YC
from sdk.ypclient import YunpianConf


class TestYunpianClient(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testYunpianIni(self):
        print(__name__)
        conf = YunpianConf()
        self.assertEqual(conf.conf(YC.YP_VERSION), "v2")

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
