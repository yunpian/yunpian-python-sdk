# -*- coding:utf-8 -*-
# filename:Sign
# 16/3/10 下午4:28
import hashlib

__author__ = 'bingone'


class Sign:
    singName='_sign'
    @staticmethod
    def getSign(d, apiSecret):
        pass
        if (d == None or apiSecret == None):
            raise Exception("dict or apiSecret is None")
        d['api_secret'] = apiSecret + apiSecret + apiSecret + apiSecret
        dd = sorted(d.iteritems(), key=lambda d: d[0])
        s = ''
        for k, v in dd:
            s = s + v + ','
        return Sign.md5(s[:-1])

    @staticmethod
    def md5(str):
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()


if __name__ == '__main__':
    pass
    print Sign.getSign({'mobile': '13000000000', 'text': '【yunpian】您的验证码是4444'}, '12345678')
