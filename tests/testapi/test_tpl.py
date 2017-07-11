# -*- coding: utf-8 -*-
'''
Created on Jul 4, 2017

@author: dzh
'''
import unittest

from yunpian_python_sdk.model.constant import (TPL_CONTENT, VERSION_V1, TPL_ID)

from . import TestYunpianApi


class TestTplApi(TestYunpianApi):
    '''Test TplApi'''

    def _test_add(self):
        clnt = self._clnt

        param = {TPL_CONTENT : '【云片网】您的验证码是#code#'}
        r = clnt.tpl().add(param)
        self.show(r)

        # v1
        r = clnt.tpl().version(VERSION_V1).add(param)
        self.show(r)

    def _test_get(self):
        clnt = self._clnt

        param = {TPL_ID : '1'}
        r = clnt.tpl().get(param)
        self.show(r)

        # v1
        r = clnt.tpl().version(VERSION_V1).get(param)
        self.show(r)

    def _test_del(self):
        clnt = self._clnt

        param = {TPL_ID : '1'}
        r = clnt.tpl().del_tpl(param);
        self.show(r)

        # v1
        r = clnt.tpl().version(VERSION_V1).del_tpl(param)
        self.show(r)

    def _test_get_default(self):
        clnt = self._clnt

        param = {TPL_ID : '1'}
        r = clnt.tpl().get_default(param)
        self.show(r)

        # v1
        r = clnt.tpl().version(VERSION_V1).get_default(param)
        self.show(r)

    def _test_update(self):
        clnt = self._clnt

        param = {TPL_ID : '1', TPL_CONTENT : '【云片网】您的验证码是#code#'}
        r = clnt.tpl().update(param)
        self.show(r)

        # v1
        r = clnt.tpl().version(VERSION_V1).update(param)
        self.show(r)

    def _test_add_voice_notify(self):
        clnt = self._clnt

        param = {TPL_CONTENT : '您的验证码是#code#'}
        r = clnt.tpl().add_voice_notify(param)
        self.show(r)

    def _test_update_voice_notify(self):
        clnt = self._clnt

        param = {TPL_ID:'3405', TPL_CONTENT : '您的验证码是1#code#'}
        r = clnt.tpl().update_voice_notify(param)
        self.show(r)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
