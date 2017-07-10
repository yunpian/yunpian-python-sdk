'''
Created on Jun 19, 2017

@author: dzh
'''
from sdk.api.ypapi import YunpianApi, CommonResultHandler
from sdk.model.constant import YP_VOICE_HOST, APIKEY, MOBILE, CODE, VERSION_V1, \
    RESULT, VERSION_V2, VOICE_STATUS, TPL_ID, TPL_VALUE


class VoiceApi(YunpianApi):
    '''
    语音验证码、语音通知接口 <a>https://www.yunpian.com/api2.0/voice.html</a>
    '''

    def _init(self, clnt):
        super.init(clnt)
        self.host(clnt.conf(YP_VOICE_HOST, 'https://voice.yunpian.com'))


    def send(self, param={}):
        '''
        <h1>发语音验证码</h1>
        <p>
        参数名 类型 是否必须 描述 示例
        </p>
        <p>
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        </p>
        <p>
        mobile String 是 接收的手机号、固话（需加区号） 15205201314 01088880000
        </p>
        <p>
        code String 是 验证码，支持4~6位阿拉伯数字 1234
        </p>
        <p>
        encrypt String 否 加密方式 使用加密 tea (不再使用)
        </p>
        <p>
        _sign String 否 签名字段 参考使用加密 393d079e0a00912335adfe46f4a2e10f (不再使用)
        </p>
        <p>
        callback_url String 否 本条语音验证码状态报告推送地址 http://your_receive_url_address
        </p>
        <p>
        display_num String 否 透传号码，为保证全国范围的呼通率，云片会自动选择最佳的线路，透传的主叫号码也会相应变化。
        如需透传固定号码则需要单独注册报备，为了确保号码真实有效，客服将要求您使用报备的号码拨打一次客服电话
        </p>
        Args:
            param:  
        Results:
            Result
        '''
        r = self.verify_param(param, [APIKEY, MOBILE, CODE])
        if not r.is_succ():
            return r
        h = CommonResultHandler(self.version(), lambda v, rsp: {VERSION_V1:rsp[RESULT], VERSION_V2:rsp}[v])
        return self.path('send.json').post(param, h, r)

    def pull_status(self, param={}):
        '''
        <h1>获取状态报告</h1>
        <p>
        参数名 是否必须 描述 示例
        </p>
        <p>
        apikey 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        </p>
        <p>
        page_size 否 每页个数，最大100个，默认20个 20
        </p>
        <p>
        type Integer 否 拉取类型，1-语音验证码 2-语音通知，默认type=1 1
        </p>
        Args:
            param:  
        Results:
            Result
        '''
        r = self.verify_param(param, [APIKEY])
        if not r.is_succ():
            return r
        h = CommonResultHandler(self.version(), lambda v, rsp: {VERSION_V1:rsp[VOICE_STATUS], VERSION_V2:rsp}[v])
        return self.path('pull_status.json').post(param, h, r)

    def tpl_notify(self, param={}):
        '''
        <h1>发送语音通知</h1>
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
        r = self.verify_param(param, [APIKEY, MOBILE, TPL_ID, TPL_VALUE])
        if not r.is_succ():
            return r
        h = CommonResultHandler(self.version(), lambda v, rsp: {VERSION_V2:rsp}[v])
        return self.path('tpl_notify.json').post(param, h, r)
