# -*- coding: utf-8 -*-
'''
Created on Jul 4, 2017

@author: dzh
'''
import unittest

from yunpian_python_sdk.model.constant import (MOBILE, CODE, VERSION_V1, PAGE_SIZE, TPL_VALUE, TPL_ID)

from . import TestYunpianApi


class TestVoiceApi(TestYunpianApi):
    '''Test VoiceApi'''

    def test_send(self):
        clnt = self._clnt

        param = {MOBILE : '18616020000', CODE: '1234'}
        r = clnt.voice().send(param)
        self.show(r)

        # v1
        r = clnt.voice().version(VERSION_V1).send(param)
        self.show(r)

    def test_pull_status(self):
        clnt = self._clnt

        param = {PAGE_SIZE : '10'}
        r = clnt.voice().pull_status(param)
        self.show(r)

        # v1
        r = clnt.voice().version(VERSION_V1).pull_status(param)
        self.show(r)

    def test_tpl_notify(self):
        clnt = self._clnt

        param = {MOBILE:'18616020000', TPL_ID : '1', TPL_VALUE:'name=dzh&time=2'}
        r = clnt.voice().tpl_notify(param)
        self.show(r)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
