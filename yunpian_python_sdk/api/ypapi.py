# -*- coding: utf-8 -*-
'''Basic Yunpian API
Created on Jul 6, 2017

@author: dzh
'''

from ..model.constant import (VERSION_V2, YP_VERSION, CHARSET_UTF8, VERSION_V1, CODE, APIKEY, MSG, DETAIL, HTTP_CHARSET)
from ..model.result import Result, Code


class ResultHandler(object):
    '''interface to parse the response'''

    def succ(self, code, rsp, r):
        '''return success Result
        Args:
            code: = 0
            rsp: a dict representing api's response
            r: Result
        Returns:
            r
        '''
        raise NotImplementedError("implemented this")

    def fail(self, code, rsp, r):
        '''return failure Result
        Args:
            code: != 0
            rsp: a dict representing api's response
            r: Result
        Returns:
            r
        '''
        raise NotImplementedError("implemented this")

    def catch_exception(self, e, r):
        '''return exception Result
        Args:
            e: Error
            rsp: a dict representing api's response
            r: Result
        Returns:
            r
        '''
        raise NotImplementedError("implemented this")

class CommonResultHandler(ResultHandler):

    def __init__(self, func):
        '''return exception Result
        Args:
            version: api's version
            func: Result receive data by calling func(version,rsp)
        '''
        self._func = func

    def succ(self, code, rsp, r):
        return r.code(code, True).msg(rsp[MSG] if MSG in rsp else None, True).data(self._func(rsp), True)

    def fail(self, code, rsp, r):
        return r.code(code, True).msg(rsp[MSG] if MSG in rsp else None, True).detail(rsp[DETAIL] if DETAIL in rsp else None, True)

    def catch_exception(self, e, r):
        return r.code(Code.UNKNOWN_EXCEPTION, True).exception(e, True)

class YunpianApiResult(object):
    '''interface to retrieve the Result from the response'''

    def result(self, rsp, h, r=Result()):
        '''
        Args:
            rsp: a dict representing api's response
            h: ResultHandler
            r: Result
        Returns:
             r Result
        '''
        raise NotImplementedError("implemented this")

    def code(self, rsp, version=VERSION_V2):
        '''
        Args:
            rsp: a dict object representing api's response
            version: api's version
        Returns:
            api's int code
        '''
        raise NotImplementedError("implemented this")

class YunpianApi(YunpianApiResult):
    '''basic API object'''

    def _init(self, clnt):
        '''initialize api by YunpianClient'''
        assert clnt, "clnt is None"
        self._clnt = clnt
        self._apikey = clnt.apikey()
        self._version = clnt.conf(YP_VERSION, defval=VERSION_V2)
        self._charset = clnt.conf(HTTP_CHARSET, defval=CHARSET_UTF8)
        self._name = self.__class__.__module__.split('.')[-1]

    def client(self, clnt=None):
        if clnt:
            self._clnt = clnt
            return self
        return self._clnt

    def host(self, host=None):
        if host:
            self._host = host
            return self
        return self._host

    def version(self, version=None):
        if version:
            self._version = version
            return self
        return self._version

    def path(self, path=None):
        if path:
            self._path = path
            return self
        return self._path

    def apikey(self, apikey=None):
        if apikey:
            self._apikey = apikey
            return self
        return self._apikey

    def charset(self, charset=None):
        if charset:
            self._charset = charset
            return self
        return self._charset

    def name(self, name=None):
        '''api name, default is module.__name__'''
        if name:
            self._name = name
            return self
        return self._name

    def uri(self):
        return '{}/{}/{}/{}'.format(self.host(), self.version(), self.name(), self.path())


    def post(self, param, h, r=Result()):
        '''
        Args:
            param: request parameters
            h: ResultHandler
            r: YunpianApiResult
        '''
        try:
            rsp = self.client().post(self.uri(), param)
            # print(rsp)
            return self.result(rsp, h, r)
        except ValueError as err:
            return h.catch_exception(err, r)

    def result(self, rsp, h, r=Result()):
        code = self.code(rsp, self.version())
        return h.succ(code, rsp, r) if code == Code.SUCC else h.fail(code, rsp, r)

    def code(self, rsp, version=VERSION_V2):
        if rsp is None:
            return Code.SUCC

        code = Code.UNKNOWN_EXCEPTION
        if version == VERSION_V1:
            code = int(rsp[CODE]) if CODE in rsp else Code.UNKNOWN_EXCEPTION
        elif version == VERSION_V2:
            code = int(rsp[CODE]) if CODE in rsp else Code.SUCC

        return code

    def verify_param(self, param={}, must=[], r=Result()):
        '''return Code.ARGUMENT_MISSING if every key in must not found in param'''
        if APIKEY not in param:
            param[APIKEY] = self.apikey()

        for p in must:
            if p not in param:
                r.code(Code.ARGUMENT_MISSING).detail('missing-' + p)
                break

        return r
