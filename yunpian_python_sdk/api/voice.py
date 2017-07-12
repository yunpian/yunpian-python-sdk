# -*- coding: utf-8 -*-
'''
Created on Jun 19, 2017

@author: dzh
'''
from ..model.constant import (
    YP_VOICE_HOST, APIKEY, MOBILE, CODE, VERSION_V1, RESULT, VERSION_V2, VOICE_STATUS, TPL_ID, TPL_VALUE)
from .ypapi import YunpianApi, CommonResultHandler


class VoiceApi(YunpianApi):
    '''语音验证码、通知接口 https://www.yunpian.com/api2.0/voice.html'''

    def _init(self, clnt):
        super(VoiceApi, self)._init(clnt)
        self.host(clnt.conf(YP_VOICE_HOST, 'https://voice.yunpian.com'))


    def send(self, param, must=[APIKEY, MOBILE, CODE]):
        '''发语音验证码

        参数名 类型 是否必须 描述 示例
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        mobile String 是 接收的手机号、固话（需加区号） 15205201314 01088880000
        code String 是 验证码，支持4~6位阿拉伯数字 1234
        encrypt String 否 加密方式 使用加密 tea (不再使用)
        _sign String 否 签名字段 参考使用加密 393d079e0a00912335adfe46f4a2e10f (不再使用)
        callback_url String 否 本条语音验证码状态报告推送地址 http://your_receive_url_address
        display_num String 否 透传号码，为保证全国范围的呼通率，云片会自动选择最佳的线路，透传的主叫号码也会相应变化。
        如需透传固定号码则需要单独注册报备，为了确保号码真实有效，客服将要求您使用报备的号码拨打一次客服电话

        Args:
            param:  
        Results:
            Result
        '''
        r = self.verify_param(param, must)
        if not r.is_succ():
            return r
        h = CommonResultHandler(lambda rsp: {VERSION_V1:rsp.get(RESULT), VERSION_V2:rsp}[self.version()])
        return self.path('send.json').post(param, h, r)

    def pull_status(self, param=None, must=[APIKEY]):
        '''获取状态报告

        参数名 是否必须 描述 示例
        apikey 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        page_size 否 每页个数，最大100个，默认20个 20
        type Integer 否 拉取类型，1-语音验证码 2-语音通知，默认type=1 1

        Args:
            param:  
        Results:
            Result
        '''
        param = {} if param is None else param
        r = self.verify_param(param, must)
        if not r.is_succ():
            return r
        h = CommonResultHandler(lambda rsp: {VERSION_V1:rsp[VOICE_STATUS] if VOICE_STATUS in rsp else None, VERSION_V2:rsp}[self.version()])
        return self.path('pull_status.json').post(param, h, r)

    def tpl_notify(self, param, must=[APIKEY, MOBILE, TPL_ID, TPL_VALUE]):
        '''发送语音通知
        
        功能说明：通过电话直呼到用户手机(固话)播放指定模版内容的文本，默认播放1次。
        特别说明：模版需要先审核通过
        访问方式：POST
        参数：
        参数名    类型    是否必须    描述    示例
        apikey    String    是    用户唯一标识    9b11127a9701975c734b8aee81ee3526
        mobile    String    是    接收的手机号、固话（需加区号）    15205201314 01088880000
        tpl_id    Long    是    审核通过的模版ID    1136
        tpl_value    String    是    变量名和变量值对。请先对您的变量名和变量值分别进行urlencode再传递。    模板： 课程#name#在#time#开始。
        最终发送结果： 课程深度学习在14:00开始。 tplvalue=urlencode("name=深度学习&time=14:00","utf-8");
        callback_url    String    否    本条语音验证码状态报告推送地址    http://your_receive_url_address
        
        Args:
            param:  
        Results:
            Result
        '''
        r = self.verify_param(param, must)
        if not r.is_succ():
            return r
        h = CommonResultHandler(lambda rsp: {VERSION_V2:rsp}[self.version()])
        return self.path('tpl_notify.json').post(param, h, r)
