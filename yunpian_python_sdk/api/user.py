# -*- coding: utf-8 -*-
'''
Created on Jun 19, 2017

@author: dzh
'''
from ..model.constant import YP_USER_HOST, APIKEY, VERSION_V1, USER, VERSION_V2
from .ypapi import YunpianApi, CommonResultHandler


class UserApi(YunpianApi):
    '''用户接口 https://www.yunpian.com/api2.0/user.html'''

    def _init(self, clnt):
        super(UserApi, self)._init(clnt)
        self.host(clnt.conf(YP_USER_HOST, 'https://sms.yunpian.com'))


    def get(self, param={}):
        '''查账户信息
        
        参数名 类型 是否必须 描述 示例
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        
        Args:
            param: (Optional) 
        Results:
            Result
        '''
        r = self.verify_param(param, [APIKEY])
        if not r.is_succ():
            return r
        handle = CommonResultHandler(lambda rsp: {VERSION_V1:rsp.get(USER), VERSION_V2:rsp}[self.version()])
        return self.path('get.json').post(param, handle, r)


    def set(self, param={}):
        '''修改账户信息
        
        参数名 类型 是否必须 描述 示例
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        emergency_contact String 否 紧急联系人 zhangshan
        emergency_mobile String 否 紧急联系人手机号 13012345678
        alarm_balance Long 否 短信余额提醒阈值。 一天只提示一次 100
        
        Args:
            param: emergency_contact emergency_mobile alarm_balance 
        Results:
            Result
        '''
        r = self.verify_param(param, [APIKEY])
        if not r.is_succ():
            return r
        h = CommonResultHandler(lambda rsp: {VERSION_V2:rsp}[self.version()])
        return self.path('set.json').post(param, h, r)
