'''
Created on Jun 19, 2017

@author: dzh
'''
from sdk.api.ypapi import YunpianApi, CommonResultHandler
from sdk.model.constant import YP_TPL_HOST, APIKEY, VERSION_V2, VERSION_V1, \
    TEMPLATE, TPL_CONTENT, TPL_ID


class TplApi(YunpianApi):
    '''
    模版接口 <a>https://www.yunpian.com/api2.0/tpl.html</a>
    '''

    def init(self, clnt):
        super.init(clnt)
        self.host(clnt.conf(YP_TPL_HOST, 'https://sms.yunpian.com'))

    def get_default(self, param={}):
        '''
        <h1>取默认模板</h1>
        <p>
        参数名 类型 是否必须 描述 示例
        </p>
        <p>
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        </p>
        <p>
        tpl_id Long 否 模板id，64位长整形。指定id时返回id对应的默认 模板。未指定时返回所有默认模板 1
        </p>
        Args:
            param:  
        Results:
            Result
        '''
        r = self.verify_param(param, [APIKEY])
        if not r.is_succ():
            return r
        h = CommonResultHandler(self.version(), lambda v, rsp: {VERSION_V2:rsp}[v])
        return self.path('get_default.json').post(param, h, r)


    def get(self, param={}):
        '''
        <h1>取模板</h1>
        <p>
        参数名 类型 是否必须 描述 示例
        </p>
        <p>
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        </p>
        <p>
        tpl_id Long 否 模板id，64位长整形。指定id时返回id对应的 模板。未指定时返回所有模板 1
        </p>
        Args:
            param:  
        Results:
            Result
        '''
        r = self.verify_param(param, [APIKEY])
        if not r.is_succ():
            return r
        h = CommonResultHandler(self.version(), lambda v, rsp: {VERSION_V1:rsp[TEMPLATE], VERSION_V2:rsp}[v])
        return self.path('get.json').post(param, h, r)


    def add(self, param={}):
        '''
        <h1>添加模板</h1>
        <p>
        参数名 类型 是否必须 描述 示例
        </p>
        <p>
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        </p>
        <p>
        tpl_content String 是 模板内容，必须以带符号【】的签名开头 【云片网】您的验证码是#code#
        </p>
        <p>
        notify_type Integer 否 审核结果短信通知的方式: 0表示需要通知,默认; 1表示仅审核不通过时通知; 2表示仅审核通过时通知;
        3表示不需要通知 1
        </p>
        <p>
        lang String 否 国际短信模板所需参数，模板语言:简体中文zh_cn; 英文en; 繁体中文 zh_tw; 韩文ko,日文 ja
        zh_cn
        </p>
        Args:
            param:  
        Results:
            Result
        '''
        r = self.verify_param(param, [APIKEY, TPL_CONTENT])
        if not r.is_succ():
            return r
        h = CommonResultHandler(self.version(), lambda v, rsp: {VERSION_V1:rsp[TEMPLATE], VERSION_V2:rsp}[v])
        return self.path('add.json').post(param, h, r)

    def del_tpl(self, param={}):
        '''
        <h1>删除模板</h1>
        <p>
        参数名 类型 是否必须 描述 示例
        </p>
        <p>
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        </p>
        <p>
        tpl_id Long 是 模板id，64位长整形 9527
        </p>
        Args:
            param:  
        Results:
            Result
        '''
        r = self.verify_param(param, [APIKEY, TPL_ID])
        if not r.is_succ():
            return r
        h = CommonResultHandler(self.version(), lambda v, rsp: {VERSION_V2:rsp}[v])
        return self.path('del.json').post(param, h, r)

    def update(self, param={}):
        '''
        <h1>修改模板</h1>
        <p>
        参数名 类型 是否必须 描述 示例
        </p>
        <p>
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        </p>
        <p>
        tpl_id Long 是 模板id，64位长整形，指定id时返回id对应的模板。未指定时返回所有模板 9527
        </p>
        <p>
        tpl_content String 是
        模板id，64位长整形。指定id时返回id对应的模板。未指定时返回所有模板模板内容，必须以带符号【】的签名开头 【云片网】您的验证码是#code#
        </p>
        <p>
        notify_type Integer 否 审核结果短信通知的方式: 0表示需要通知,默认; 1表示仅审核不通过时通知; 2表示仅审核通过时通知;
        3表示不需要通知 1
        </p>
        <p>
        lang String 否 国际短信模板所需参数，模板语言:简体 中文zh_cn; 英文en; 繁体中文 zh_tw; 韩文ko,日文 ja
        zh_cn
        </p>
        Args:
            param:  
        Results:
            Result
        '''
        r = self.verify_param(param, [APIKEY, TPL_ID, TPL_CONTENT])
        if not r.is_succ():
            return r
        h = CommonResultHandler(self.version(), lambda v, rsp: {VERSION_V1:rsp[TEMPLATE], VERSION_V2:rsp[TEMPLATE] if TEMPLATE in rsp else rsp}[v])
        return self.path('update.json').post(param, h, r)

    def add_voice_notify(self, param={}):
        '''
        <h1>添加语音通知模版</h1>
        访问方式：POST
        参数：
        参数名    类型    是否必须    描述    示例
        apikey    String    是    用户唯一标识    9b11127a9701975c734b8aee81ee3526
        tpl_content    String    是    模板内容，没有签名    您的验证码是#code#
        notify_type    Integer    否    审核结果短信通知的方式:0表示需要通知,默认;1表示仅审核不通过时通知;2表示仅审核通过时通知;3表示不需要通知 1
        '''
        r = self.verify_param(param, [APIKEY, TPL_CONTENT])
        if not r.is_succ():
            return r
        h = CommonResultHandler(self.version(), lambda v, rsp: {VERSION_V2:rsp}[v])
        return self.path('add_voice_notify.json').post(param, h, r)

    def update_voice_notify(self, param={}):
        '''
        <h1>修改语音通知模版</h1>
        注意：模板成功修改之后需要重新审核才能使用！同时提醒您如果修改了变量，务必重新测试，以免替换出错!
        参数：
        参数名    类型    是否必须    描述    示例
        apikey    String    是    用户唯一标识    9b11127a9701975c734b8aee81ee3526
        tpl_id    Long    是    模板id，64位长整形。指定id时返回id对应的模板。未指定时返回所有模板    9527
        tpl_content    String    是    模板id，64位长整形。指定id时返回id对应的模板。未指定时返回所有模板模板内容    您的验证码是#code#
        '''
        r = self.verify_param(param, [APIKEY, TPL_ID, TPL_CONTENT])
        if not r.is_succ():
            return r
        h = CommonResultHandler(self.version(), lambda v, rsp: {VERSION_V2:rsp}[v])
        return self.path('update_voice_notify.json').post(param, h, r)
