# -*- coding: utf-8 -*-
'''
Created on Jun 19, 2017

@author: dzh
'''

from ..model.constant import (APIKEY, YP_FLOW_HOST, VERSION_V1, FLOW_PACKAGE, VERSION_V2, MOBILE, RESULT, FLOW_STATUS, SN)
from .ypapi import YunpianApi, CommonResultHandler


class FlowApi(YunpianApi):
    '''流量接口 https://www.yunpian.com/api2.0/api-flow.html'''

    def _init(self, clnt):
        super(FlowApi, self)._init(clnt)
        self.host(clnt.conf(YP_FLOW_HOST, 'https://flow.yunpian.com'))

    def get_package(self, param=None, must=[APIKEY]):
        '''查询流量包
        
        参数名 类型 是否必须 描述 示例
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        carrier String 否 运营商ID 传入该参数则获取指定运营商的流量包， 否则获取所有运营商的流量包 移动：10086 联通：10010 电信：10000
        
        Args:
            param:
        Results:
            Result
        '''
        param = {} if param is None else param
        r = self.verify_param(param, must)
        if not r.is_succ():
            return r
        h = CommonResultHandler(lambda rsp: {VERSION_V1:rsp[FLOW_PACKAGE] if FLOW_PACKAGE in rsp else None, VERSION_V2:rsp}[self.version()])
        return self.path('get_package.json').post(param, h, r)

    def recharge(self, param, must=[APIKEY, MOBILE, SN]):
        '''充值流量
        
        参数名 类型 是否必须 描述 示例
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        mobile String 是 接收的手机号（仅支持大陆号码） 15205201314
        sn String 是 流量包的唯一ID 点击查看 1008601
        callback_url String 否 本条流量充值的状态报告推送地址 http://your_receive_url_address
        encrypt String 否 加密方式 使用加密 tea (不再使用)
        _sign String 否 签名字段 参考使用加密 393d079e0a00912335adfe46f4a2e10f (不再使用)
        
        Args:
            param:
        Results:
            Result
        '''
        r = self.verify_param(param, must)
        if not r.is_succ():
            return r
        h = CommonResultHandler(lambda rsp: {VERSION_V1:rsp[RESULT] if RESULT in rsp else None, VERSION_V2:rsp}[self.version()])
        return self.path('recharge.json').post(param, h, r)

    def pull_status(self, param=None, must=[APIKEY]):
        '''获取状态报告
        
        参数名 是否必须 描述 示例
        apikey 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        page_size 否 每页个数，最大100个，默认20个 20
        
        Args:
            param:
        Results:
            Result
        '''
        param = {} if param is None else param
        r = self.verify_param(param, must)
        if not r.is_succ():
            return r
        h = CommonResultHandler(lambda rsp: {VERSION_V1:rsp[FLOW_STATUS] if FLOW_STATUS in rsp else None, VERSION_V2:rsp}[self.version()])
        return self.path('pull_status.json').post(param, h, r)
