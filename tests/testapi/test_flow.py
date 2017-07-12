# -*- coding: utf-8 -*-
'''
Created on Jul 4, 2017

@author: dzh
'''
import unittest

from yunpian_python_sdk.model.constant import VERSION_V1, MOBILE, SN

from . import TestYunpianApi


class TestFlowApi(TestYunpianApi):
    '''Test FlowApi'''

    def test_get_package(self):
        clnt = self._clnt

        r = clnt.flow().get_package()
        self.show(r)

        # v1
        r = clnt.flow().version(VERSION_V1).get_package()
        self.show(r)

    def test_recharge(self):
        clnt = self._clnt

        param = {MOBILE : '18616020000', SN : '1008601'}
        r = clnt.flow().recharge(param)
        self.show(r)

        # v1
        r = clnt.flow().version(VERSION_V1).recharge(param)
        self.show(r)

    def test_pull_status(self):
        clnt = self._clnt

        r = clnt.flow().pull_status()
        self.show(r)

        # v1
        r = clnt.flow().version(VERSION_V1).pull_status()
        self.show(r)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
