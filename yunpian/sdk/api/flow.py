'''
Created on Jun 19, 2017

@author: dzh
'''
from sdk.api.ypapi import YunpianApi, CommonResultHandler
from sdk.model.constant import APIKEY, YP_FLOW_HOST, VERSION_V1, FLOW_PACKAGE, \
    VERSION_V2, MOBILE, RESULT, FLOW_STATUS


class FlowApi(YunpianApi):
    '''流量接口 <a>https://www.yunpian.com/api2.0/api-flow.html</a>'''

    def _init(self, clnt):
        super.init(clnt)
        self.host(clnt.conf(YP_FLOW_HOST, 'https://flow.yunpian.com'))

    def get_package(self, param={}):
        '''
        <h1>查询流量包</h1>
        <p>
        参数名 类型 是否必须 描述 示例
        </p>
        <p>
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        </p>
        <p>
        carrier String 否 运营商ID 传入该参数则获取指定运营商的流量包， 否则获取所有运营商的流量包 移动：10086 联通：10010 电信：10000
        </p>
        Args:
            param:  
        Results:
            Result
        '''
        r = self.verify_param(param, [APIKEY])
        if not r.is_succ():
            return r
        h = CommonResultHandler(self.version(), lambda v, rsp: {VERSION_V1:rsp[FLOW_PACKAGE], VERSION_V2:rsp}[v])
        return self.path('get_package.json').post(param, h, r)

    def recharge(self, param={}):
        '''
        <h1>充值流量</h1>
        <p>
        参数名 类型 是否必须 描述 示例
        </p>
        <p>
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        </p>
        <p>
        mobile String 是 接收的手机号（仅支持大陆号码） 15205201314
        </p>
        <p>
        sn String 是 流量包的唯一ID 点击查看 1008601
        </p>
        <p>
        callback_url String 否 本条流量充值的状态报告推送地址 http://your_receive_url_address
        </p>
        <p>
        encrypt String 否 加密方式 使用加密 tea (不再使用)
        </p>
        <p>
        _sign String 否 签名字段 参考使用加密 393d079e0a00912335adfe46f4a2e10f (不再使用)
        </p>
        Args:
            param 
        Results:
            Result
        '''
        r = self.verify_param(param, [APIKEY, MOBILE])
        if not r.is_succ():
            return r
        h = CommonResultHandler(self.version(), lambda v, rsp: {VERSION_V1:rsp[RESULT], VERSION_V2:rsp}[v])
        return self.path('recharge.json').post(param, h, r)

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
        Args:
            param:
        Results:
            Result
        '''
        r = self.verify_param(param, [APIKEY])
        if not r.is_succ():
            return r
        h = CommonResultHandler(self.version(), lambda v, rsp: {VERSION_V1:rsp[FLOW_STATUS], VERSION_V2:rsp}[v])
        return self.path('pull_status.json').post(param, h, r)
