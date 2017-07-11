# -*- coding: utf-8 -*-
'''Yunpian APIs' HttpClient

YunpianClient Usage:
    clnt = YunpianClient('apikey')
    # sms api
    r = clnt.sms().single_send({'mobile':'18616020***','text':'【云片网】您的验证码是1234'})
    # handle r(model.result.Result): r.code() r.msg() r.data() r.detail() r.exception()
    # othres api: clnt.flow()|sign()|sms()|tpl()|user()|voice()

Created on Jun 18, 2017

@author: dzh
'''
import json

import requests

from .api import flow, sign, sms, tpl, user, voice
from .model.constant import (CHARSET_UTF8, YP_APIKEY, HTTP_CONN_TIMEOUT, HTTP_SO_TIMEOUT)


class _YunpianConf(object):
    '''SDK Configuration'''

    # yunpian default config
    YP_CONF = {
               'http.conn.timeout':'10',
               'http.so.timeout':'30',
               'http.charset':'utf-8',
               'yp.version':'v2',
               'yp.user.host':'https://sms.yunpian.com',
               'yp.sign.host':'https://sms.yunpian.com',
               'yp.tpl.host':'https://sms.yunpian.com',
               'yp.sms.host':'https://sms.yunpian.com',
               'yp.voice.host':'https://voice.yunpian.com',
               'yp.flow.host':'https://flow.yunpian.com',
               'yp.call.host':'https://call.yunpian.com'
    }

    def __init__(self):
        # load yunpian.ini
#         import configparser
#         from os import path
#         config = configparser.ConfigParser()
#         config.read(path.join(path.abspath(path.dirname(__file__)), 'yunpian.ini'), CHARSET_UTF8)
#         self.__conf = {}
#         for section in config.sections():
#             for (key, val) in config.items(section):
#                 self.__conf[key] = val
        self.__conf = {}

    def custom_apikey(self, apikey):
        '''custom apikey'''
        if apikey:
            self.__conf[YP_APIKEY] = apikey
        return self

    def custom_conf(self, conf):
        '''custom apikey and http parameters'''
        if conf:
            for (key, val) in conf.items():
                self.__conf[key] = val
        return self

    def apikey(self):
        '''
        Returns:
            apikey: apikey
        '''
        return self.__conf[YP_APIKEY]

    def conf(self, key):
        '''get config'''
        return self.__conf[key] if key in self.__conf else _YunpianConf.YP_CONF.get(key)


class _ApiFactory(object):
    '''Yunpian APIs Factory'''

    def __init__(self, clnt):
        assert clnt, "YunpianClient is None"
        self._clnt = clnt

    def api(self, name):
        '''return special API by package's name'''

        assert name, 'name is none'
        if flow.__name__ == name:
            api = flow.FlowApi()
        elif sign.__name__ == name:
            api = sign.SignApi()
        elif sms.__name__ == name:
            api = sms.SmsApi()
        elif tpl.__name__ == name:
            api = tpl.TplApi()
        elif user.__name__ == name:
            api = user.UserApi()
        elif voice.__name__ == name:
            api = voice.VoiceApi()

        assert api, "not found api-" + name

        api._init(self._clnt)
        return api


class YunpianClient(object):
    '''
    Support Yunpian rest APIs, both v1|v2 interfaces.

    https://www.yunpian.com/api2.0/api-domestic.html

    TODO(dzh)

    Attributes:
        _ypconf: YunpianClient's configuration
        _api: An ApiFactory instance
    '''

    def __init__(self, apikey=None, conf={}):
        '''
        Args:
            apikey: apikey
            conf: custom config to initialize ypconf,keys like yp.*
        '''
        if apikey is None and YP_APIKEY in conf:
            apikey = conf[YP_APIKEY]
        assert apikey, "apikey is nil"
        self._ypconf = _YunpianConf().custom_conf(conf).custom_apikey(apikey)
        self._api = _ApiFactory(self)

    def flow(self):
        '''flow api
        Returns:
            api.flow.FlowApi
        '''
        return self._api.api(flow.__name__)

    def sign(self):
        '''sign api
        Returns:
            api.sign.SignApi
        '''
        return self._api.api(sign.__name__)

    def sms(self):
        '''sms api
        Returns:
            api.sms.SmsApi
        '''
        return self._api.api(sms.__name__)

    def tpl(self):
        '''tpl api
        Returns:
            api.tpl.TplApi
        '''
        return self._api.api(tpl.__name__)

    def user(self):
        '''user api
        Returns:
            api.user.UserApi
        '''
        return self._api.api(user.__name__)

    def voice(self):
        '''voice api
        Returns:
            api.voice.VoiceApi
        '''
        return self._api.api(voice.__name__)

    def conf(self, key=None, defval=None):
        '''return YunpianConf if key=None, else return value in YunpianConf'''
        if key is None:
            return self._ypconf
        val = self._ypconf.conf(key)
        return defval if val is None else val

    def apikey(self):
        return self._ypconf.apikey()

    def post(self, url, data, charset=CHARSET_UTF8, headers={}):
        '''response json text'''
        if 'Api-Lang' not in headers:
            headers['Api-Lang'] = 'python'
        if 'Content-Type' not in headers:
            headers['Content-Type'] = "application/x-www-form-urlencoded;charset=" + charset
        rsp = requests.post(url, data, headers=headers,
                            timeout=(int(self.conf(HTTP_CONN_TIMEOUT, '10')), int(self.conf(HTTP_SO_TIMEOUT, '30'))))
        return json.loads(rsp.text)

    def urlEncodeAndJoin(self, seq, sepr=','):
        '''sepr.join(urlencode(seq))
        Args:
            seq: string list to be urlencoded
            sepr: join seq with sepr
        Returns:
            str
        '''
        try:
            from urllib.parse import quote_plus as encode
            return sepr.join([encode(x, encoding=CHARSET_UTF8) for x in seq])
        except ImportError:
            from urllib import quote as encode
            return sepr.join([i for i in map(lambda x: encode(x), seq)])
