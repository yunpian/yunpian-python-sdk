# -*- coding: utf-8 -*-
'''
Created on Jun 19, 2017

@author: dzh
'''
from ..model.constant import (YP_TPL_HOST, APIKEY, VERSION_V2, VERSION_V1, TEMPLATE, TPL_CONTENT, TPL_ID)
from .ypapi import YunpianApi, CommonResultHandler


class TplApi(YunpianApi):
    '''模版接口 https://www.yunpian.com/api2.0/tpl.html'''

    def _init(self, clnt):
        super(TplApi, self)._init(clnt)
        self.host(clnt.conf(YP_TPL_HOST, 'https://sms.yunpian.com'))

    def get_default(self, param=None, must=[APIKEY]):
        '''取默认模板

        参数名 类型 是否必须 描述 示例
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        tpl_id Long 否 模板id，64位长整形。指定id时返回id对应的默认 模板。未指定时返回所有默认模板 1

        Args:
            param:  
        Results:
            Result
        '''
        param = {} if param is None else param
        r = self.verify_param(param, must)
        if not r.is_succ():
            return r
        h = CommonResultHandler(lambda rsp: {VERSION_V1:rsp[TEMPLATE] if TEMPLATE in rsp else None, VERSION_V2:rsp}[self.version()])
        return self.path('get_default.json').post(param, h, r)


    def get(self, param=None, must=[APIKEY]):
        '''取模板

        参数名 类型 是否必须 描述 示例
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        tpl_id Long 否 模板id，64位长整形。指定id时返回id对应的 模板。未指定时返回所有模板 1

        Args:
            param:  
        Results:
            Result
        '''
        param = {} if param is None else param
        r = self.verify_param(param, must)
        if not r.is_succ():
            return r
        h = CommonResultHandler(lambda rsp: {VERSION_V1:rsp[TEMPLATE] if TEMPLATE in rsp else None, VERSION_V2:rsp}[self.version()])
        return self.path('get.json').post(param, h, r)


    def add(self, param, must=[APIKEY, TPL_CONTENT]):
        '''添加模板

        参数名 类型 是否必须 描述 示例
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        tpl_content String 是 模板内容，必须以带符号【】的签名开头 【云片网】您的验证码是#code#
        notify_type Integer 否 审核结果短信通知的方式: 0表示需要通知,默认; 1表示仅审核不通过时通知; 2表示仅审核通过时通知;
        3表示不需要通知 1
        lang String 否 国际短信模板所需参数，模板语言:简体中文zh_cn; 英文en; 繁体中文 zh_tw; 韩文ko,日文 ja
        zh_cn

        Args:
            param:  
        Results:
            Result
        '''
        r = self.verify_param(param, must)
        if not r.is_succ():
            return r
        h = CommonResultHandler(lambda rsp: {VERSION_V1:rsp.get(TEMPLATE), VERSION_V2:rsp}[self.version()])
        return self.path('add.json').post(param, h, r)

    def del_tpl(self, param, must=[APIKEY, TPL_ID]):
        '''删除模板
        
        参数名 类型 是否必须 描述 示例
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        tpl_id Long 是 模板id，64位长整形 9527

        Args:
            param:  
        Results:
            Result
        '''
        r = self.verify_param(param, must)
        if not r.is_succ():
            return r
        h = CommonResultHandler(lambda rsp: {VERSION_V2:rsp}[self.version()])
        return self.path('del.json').post(param, h, r)

    def update(self, param, must=[APIKEY, TPL_ID, TPL_CONTENT]):
        '''修改模板

        参数名 类型 是否必须 描述 示例
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        tpl_id Long 是 模板id，64位长整形，指定id时返回id对应的模板。未指定时返回所有模板 9527
        tpl_content String 是
        模板id，64位长整形。指定id时返回id对应的模板。未指定时返回所有模板模板内容，必须以带符号【】的签名开头 【云片网】您的验证码是#code#
        notify_type Integer 否 审核结果短信通知的方式: 0表示需要通知,默认; 1表示仅审核不通过时通知; 2表示仅审核通过时通知;
        3表示不需要通知 1
        lang String 否 国际短信模板所需参数，模板语言:简体 中文zh_cn; 英文en; 繁体中文 zh_tw; 韩文ko,日文 ja
        zh_cn

        Args:
            param:  
        Results:
            Result
        '''
        r = self.verify_param(param, must)
        if not r.is_succ():
            return r
        h = CommonResultHandler(lambda rsp: {VERSION_V1:rsp.get(TEMPLATE),
                                             VERSION_V2:rsp[TEMPLATE] if TEMPLATE in rsp else rsp}[self.version()])
        return self.path('update.json').post(param, h, r)

    def add_voice_notify(self, param, must=[APIKEY, TPL_CONTENT]):
        '''添加语音通知模版
        
        访问方式：POST
        参数：
        参数名    类型    是否必须    描述    示例
        apikey    String    是    用户唯一标识    9b11127a9701975c734b8aee81ee3526
        tpl_content    String    是    模板内容，没有签名    您的验证码是#code#
        notify_type    Integer    否    审核结果短信通知的方式:0表示需要通知,默认;1表示仅审核不通过时通知;2表示仅审核通过时通知;3表示不需要通知 1
        
        Args:
            param:  
        Results:
            Result
        '''
        r = self.verify_param(param, must)
        if not r.is_succ():
            return r
        h = CommonResultHandler(lambda rsp: {VERSION_V2:rsp}[self.version()])
        return self.path('add_voice_notify.json').post(param, h, r)

    def update_voice_notify(self, param, must=[APIKEY, TPL_ID, TPL_CONTENT]):
        '''修改语音通知模版
        
        注意：模板成功修改之后需要重新审核才能使用！同时提醒您如果修改了变量，务必重新测试，以免替换出错!
        参数：
        参数名    类型    是否必须    描述    示例
        apikey    String    是    用户唯一标识    9b11127a9701975c734b8aee81ee3526
        tpl_id    Long    是    模板id，64位长整形。指定id时返回id对应的模板。未指定时返回所有模板    9527
        tpl_content    String    是    模板id，64位长整形。指定id时返回id对应的模板。未指定时返回所有模板模板内容    您的验证码是#code#
        
        Args:
            param:  
        Results:
            Result
        '''
        r = self.verify_param(param, must)
        if not r.is_succ():
            return r
        h = CommonResultHandler(lambda rsp: {VERSION_V2:rsp}[self.version()])
        return self.path('update_voice_notify.json').post(param, h, r)
