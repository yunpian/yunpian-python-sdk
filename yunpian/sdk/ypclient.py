#!/usr/bin/python3
'''Yunpian APIs' HttpClient
Usage:
    clnt = YunpianClient('apikye')
    # sms
    clnt.sms().send

Created on Jun 18, 2017

@author: dzh
'''

import json

import requests

from sdk.api.ypapi import ApiFactory
from sdk.model.constant import YP_APIKEY, CHARSET_UTF8


class YunpianClient(object):
    '''
    Http client for Yunpian restful APIs, support v1|v2 interfaces.
    
    https://www.yunpian.com/api2.0/api-domestic.html
    
    TODO(dzh)  
    
    Attributes:
    '''

    def __init__(self, apikey=None, conf={}):
        '''
        Args:
            apikey: apikey
            conf: custom config to initialize ypconf
        '''
        if apikey is None:
            apikey = conf[YP_APIKEY]
        assert apikey , "apikey is nil"
        self.__ypconf = YunpianConf().customApikey(apikey).customConf(conf)
        self.__api = ApiFactory(self)

    def flow(self):
        '''flow api'''
        return self.__api.api("flow")

    def sign(self):
        '''sign api'''
        return self.__api.api("sign")

    def sms(self):
        '''sms api'''
        return self.__api.api("sms")

    def tpl(self):
        '''tpl api'''
        return self.__api.api("tpl")

    def user(self):
        '''user api'''
        return self.__api.api("user")

    def voice(self):
        '''voice api'''
        return self.__api.api("voice")

    def ypconf(self, key=None, defval=None):
        '''return YunpianConf if key=None, else return value in YunpianConf'''
        if key is None:
            return self.__ypconf
        val = self.__ypconf.conf(key)
        return defval if val is None else val

    def apikey(self):
        return self.__ypconf.apikey()

    def post(self, url, data={}, charset=CHARSET_UTF8, headers={}):
        '''response json text'''
        if'Content-Type' not in headers:
            headers['Content-Type'] = "application/x-www-form-urlencoded;charset=" + charset;
        r = requests.post(url, data, headers=headers, timeout=())
        return json.loads(r.text)

    def __del__(self):
        pass


class YunpianConf(object):
    '''
    SDK Configuration
    '''

    def __init__(self):
        import configparser
        from os import path
        '''
        load yunpian.ini
        '''
        config = configparser.ConfigParser()
        config.read(path.join(path.abspath(path.dirname(__file__)), 'yunpian.ini'), CHARSET_UTF8)
        self.__conf = {}
        for section in config.sections():
            for (k, v) in config.items(section):
                self.__conf[k] = v

    def customApikey(self, apikey):
        self.__conf[YP_APIKEY] = apikey
        return self;

    def customConf(self, conf={}):
        for (k, v) in conf.items():
            self.__conf[k] = v
        return self

    def apikey(self):
        return self.__conf[YP_APIKEY]

    def conf(self, key):
        '''get config'''
        return self.__conf[key]


if __name__ == '__main__':
    pass
