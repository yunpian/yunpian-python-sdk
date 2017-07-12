# -*- coding: utf-8 -*-
'''
Created on Jul 4, 2017

@author: dzh
'''
import unittest

from yunpian_python_sdk.model.constant import (
    MOBILE, TEXT, TPL_ID, TPL_VALUE, PAGE_SIZE, VERSION_V1, START_TIME, END_TIME, PAGE_NUM)

from . import TestYunpianApi


class TestSmsApi(TestYunpianApi):
    '''Test SmsApi'''

    def test_single_send(self):
        clnt = self._clnt;

        param = {MOBILE:'18616020000', TEXT:'【云片网】您的验证码是1234'}
        r = clnt.sms().single_send(param)
        self.show(r)

    def test_batch_send(self):
        clnt = self._clnt

        param = {MOBILE:'18616020000', TEXT:'【云片网】您的验证码是1234'}
        r = clnt.sms().batch_send(param)
        self.show(r)

    def test_multi_send(self):
        clnt = self._clnt
        param = {MOBILE : '18616020610,18616020611',
            TEXT: clnt.urlEncodeAndJoin(['【哈哈哈】您的验证码,是1234', '【哈哈哈】您的验证码是1234'])}
        r = clnt.sms().multi_send(param)
        self.show(r)

    # deprecated
    def test_tpl_single_send(self):
        clnt = self._clnt

        param = {MOBILE:'18616020000', TPL_ID:'1', TPL_VALUE:'#company#=云片网'}
        r = clnt.sms().tpl_single_send(param)
        self.show(r)

    # deprecated
    def test_tpl_batch_send(self):
        clnt = self._clnt;

        param = {MOBILE :'18616020000', TPL_ID :'1', TPL_VALUE :'#company#=云片网'}
        r = clnt.sms().tpl_batch_send(param)
        self.show(r)

    def test_pull_status(self):
        clnt = self._clnt;

        param = {PAGE_SIZE :'20'}
        r = clnt.sms().pull_status(param)
        self.show(r)

        # v1
        r = clnt.sms().version(VERSION_V1).pull_status(param)
        self.show(r)

    def test_pull_reply(self):
        clnt = self._clnt;

        param = {PAGE_SIZE :'20'}
        r = clnt.sms().pull_reply(param)
        self.show(r)

        # v1
        r = clnt.sms().version(VERSION_V1).pull_reply(param)
        self.show(r)

    def test_get_record(self):
        clnt = self._clnt;

        param = {START_TIME : '2013-08-11 00:00:00', END_TIME : '2016-12-05 00:00:00', PAGE_NUM : '1',
                PAGE_SIZE :'20'}
        r = clnt.sms().get_record(param)
        self.show(r)

        # v1
        r = clnt.sms().version(VERSION_V1).get_record(param)
        self.show(r)

    def test_get_black_word(self):
        clnt = self._clnt

        param = {TEXT: '高利贷,发票'}
        r = clnt.sms().get_black_word(param)
        self.show(r)

        # v1
        r = clnt.sms().version(VERSION_V1).get_black_word(param)
        self.show(r)


    # deprecated
    def test_send(self):
        clnt = self._clnt

        param = {MOBILE:'18616020000', TEXT : '【云片网】您的验证码是1234'}
        r = clnt.sms().version(VERSION_V1).send(param)
        self.show(r)

    def test_get_reply(self):
        clnt = self._clnt

        param = {START_TIME: '2013-08-11 00:00:00', END_TIME : '2016-12-05 00:00:00', PAGE_NUM : '1',
                 PAGE_SIZE : '20'}
        r = clnt.sms().get_reply(param)
        self.show(r)

        # v1
        r = clnt.sms().version(VERSION_V1).get_reply(param)
        self.show(r)

    # deprecated
    def test_tpl_send(self):
        clnt = self._clnt

        param = {MOBILE : '18616020000', TPL_ID : '1', TPL_VALUE :'#company#=云片网'}
        r = clnt.sms().version(VERSION_V1).tpl_send(param)
        self.show(r)

    def test_count(self):
        clnt = self._clnt;

        param = {START_TIME : '2013-08-11 00:00:00', END_TIME :'2016-12-05 00:00:00', PAGE_NUM : '1',
                 PAGE_SIZE :'20'}
        # v1
        r = clnt.sms().version(VERSION_V1).count(param)
        self.show(r)

        # don't invoke v2/count which result is invalid json
        # r = clnt.sms().count(param)
        # self.show(r)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
