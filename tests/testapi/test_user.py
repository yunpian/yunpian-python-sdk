# -*- coding: utf-8 -*-
'''
Created on Jul 4, 2017

@author: dzh
'''
import unittest

from yunpian_python_sdk.model.constant import VERSION_V1

from . import TestYunpianApi


class TestUserApi(TestYunpianApi):
    '''Test UserApi'''

    def test_get(self):
        clnt = self._clnt
        r = clnt.user().get()
        self.show(r)

        # v1
        r = clnt.user().version(VERSION_V1).get()
        self.show(r)

    def test_set(self):
        clnt = self._clnt
        param = {'emergency_mobile':'18616020000'}
        r = clnt.user().set(param)
        self.show(r)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
