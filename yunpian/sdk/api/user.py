'''
Created on Jun 19, 2017

@author: dzh
'''
from sdk.api.ypapi import YunpianApi, CommonResultHandler
from sdk.model.constant import YP_USER_HOST, APIKEY, VERSION_V1, USER, \
    VERSION_V2


class UserApi(YunpianApi):
    '''
    用户接口 <a>https://www.yunpian.com/api2.0/user.html</a>
    '''

    def _init(self, clnt):
        super.init(clnt)
        self.host(clnt.conf(YP_USER_HOST, 'https://sms.yunpian.com'))


    def get(self, param={}):
        '''
        <h1>查账户信息</h1>
        <p>
        参数名 类型 是否必须 描述 示例
        </p>
        <p>
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        </p>
        Args:
            param:  
        Results:
            Result
        '''
        r = self.verify_param(param, [APIKEY])
        if not r.is_succ():
            return r
        h = CommonResultHandler(self.version(), lambda v, rsp: {VERSION_V1:rsp[USER], VERSION_V2:rsp}[v])
        return self.path('get.json').post(param, h, r)


    def set(self, param={}):
        '''
        <h1>修改账户信息</h1>
        <p>
        参数名 类型 是否必须 描述 示例
        </p>
        <p>
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        </p>
        <p>
        emergency_contact String 否 紧急联系人 zhangshan
        </p>
        <p>
        emergency_mobile String 否 紧急联系人手机号 13012345678
        </p>
        <p>
        alarm_balance Long 否 短信余额提醒阈值。 一天只提示一次 100
        </p>
        Args:
            param: emergency_contact emergency_mobile alarm_balance 
        Results:
            Result
        '''
        r = self.verify_param(param, [APIKEY])
        if not r.is_succ():
            return r
        h = CommonResultHandler(self.version(), lambda v, rsp: {VERSION_V2:rsp}[v])
        return self.path('set.json').post(param, h, r)
