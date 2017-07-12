# -*- coding: utf-8 -*-
'''
Created on Jul 4, 2017

@author: dzh
'''
import unittest

from yunpian_python_sdk.model.constant import (
    SIGN, NOTIFY, APPLYVIP, ISONLYGLOBAL, INDUSTRYTYPE, OLD_SIGN, PAGE_NUM, PAGE_SIZE)

from . import TestYunpianApi


class TestSignApi(TestYunpianApi):
    '''Test SignApi'''


    def test_add(self) :
        clnt = self._clnt

        param = {SIGN:'你好吗', NOTIFY:'true', APPLYVIP:'false', ISONLYGLOBAL:'false', INDUSTRYTYPE:'其他'}
        r = clnt.sign().add(param)
        self.show(r)

    def test_update(self):
        clnt = self._clnt

        param = {OLD_SIGN :'你好吗', SIGN : '我很好', NOTIFY : 'true', APPLYVIP :'false',
                ISONLYGLOBAL: 'false', INDUSTRYTYPE: '其他'}
        r = clnt.sign().update(param)
        self.show(r)

    def test_get(self) :
        clnt = self._clnt

        param = {PAGE_NUM : '1', PAGE_SIZE:"3"}
        r = clnt.sign().get(param)
        self.show(r)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
