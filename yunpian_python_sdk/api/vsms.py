'''
Created on 2020-05-27

@author: fixJ
'''

from ..model.constant import (APIKEY, MOBILE, RESULT, VERSION_V2, TPL_ID, YP_VSMS_HOST, SIGN, LAYOUT, MATERIAL,
                              CERTIFICATE_FILE_SUFFIX, CERTIFICATE_FILE_CONTENTS, LICENSE_FILE_SUFFIX, LICENSE_FILE_CONTENTS)
from .ypapi import YunpianApi, CommonResultHandler


class VsmsApi(YunpianApi):

    def _init(self, clnt):
        super(VsmsApi, self)._init(clnt)
        self.host(clnt.conf(YP_VSMS_HOST, 'https://sms.yunpian.com'))

    def tpl_batch_send(self, param, must=[APIKEY, MOBILE, TPL_ID]):
        """
        批量发送超级短信
        apikey 必传: 用户唯一标识，在"账号设置"-"子帐号管理"中查看
        mobile 必传: 手机号,多个号码用英文逗号,分隔,限制 1000 个
        tpl_id 必传: 超级短信模版id
        uid 非必传: 用户自定义的 uid，系统会在状态报告中返回此字段
        tpl_param_json 非必传: 短信模板变量对应的实际值，JSON格式。 如果JSON中需要带换行符，请参照标准的JSON协议处理；且模板变量值的个数必须与手机号码个数相同、内容一一对应，表示向指定手机号码中发对应变量内容的短信，且短信模板中的变量参数替换为对应的值。
        callback_url 非必传: 短信发送后将向这个地址推送(运营商返回的)发送报告。 如推送地址固定，可以在“超级短信设置-数据推送设置”中添加。 如后台已设置地址，且请求内也包含此参数，将以请求内地址为准。
        """
        r = self.verify_param(param, must)
        if not r.is_succ():
            return r
        h = CommonResultHandler(lambda rsp: {VERSION_V2: rsp.get(RESULT)}[self.version()])
        return self.path('tpl_batch_send.json').post(param, h, r)

    def add_tpl(self, param, must=[APIKEY, SIGN, LAYOUT, MATERIAL]):
        """
        添加超级短信模板
        apikey 必传: 用户唯一标识，在"账号设置"-"子帐号管理"中查看
        sign 必传: 超级短信签名
        layout 必传: 内容布局的 json 描述文件
        material 必传: 素材的字节数组，即素材内容压成zip包后转成字节数组。若需在文本中添加变量，请用英文双#号表示，变量名格式为10字以内的英文、数字和短线，如#name_1#
            注意: 所有素材文件直接放在zip包根目录下，
            zip包内没有文件夹，且所有资源小于1.8M。
        callback_url 非必传: 模板审核结果更新后将向这个地址推送。 如推送地址固定，可以在“超级短信设置-数据推送设置”中添加。 如后台已设置地址，且添加模板请求内也包含此参数，将以请求内地址为准。
        """
        r = self.verify_param(param, must)
        file = {
            MATERIAL: (MATERIAL, param.pop(MATERIAL), 'application/octet-stream')
        }
        if not r.is_succ():
            return r
        h = CommonResultHandler(lambda rsp: {VERSION_V2: rsp.get(RESULT)}[self.version()])
        return self.path('add_tpl.json').post_multipart(param, file, h, r)

    def get_tpl(self, param, must=[APIKEY, TPL_ID]):
        """
        查询超级短信模板
        apikey 必传: 用户唯一标识，在"账号设置"-"子帐号管理"中查看
        tpl_id 必传: 超级短信模版 id
        """
        r = self.verify_param(param, must)
        if not r.is_succ():
            return r
        h = CommonResultHandler(lambda rsp: {VERSION_V2: rsp.get(RESULT)}[self.version()])
        return self.path('get_tpl.json').post(param, h, r)

    def delete_tpl(self, param, must=[APIKEY, TPL_ID]):
        """
        删除视频短信模板
        apikey 必传: 用户唯一标识，在"账号设置"-"子帐号管理"中查看
        tpl_id 必传: 超级短信模版 id
        """
        r = self.verify_param(param, must)
        if not r.is_succ():
            return r
        h = CommonResultHandler(lambda rsp: {VERSION_V2: rsp.get(RESULT)}[self.version()])
        return self.path('delete_tpl.json').post(param, h, r)

    def add_sign(self, param, must=[APIKEY, SIGN, CERTIFICATE_FILE_SUFFIX,
                                         CERTIFICATE_FILE_CONTENTS, LICENSE_FILE_SUFFIX, LICENSE_FILE_CONTENTS]):
        """
        添加视频短信签名
        apikey 必传: 用户唯一标识，在"账号设置"-"子帐号管理"中查看
        sign 必传: 签名内容，2-12字，可包含中文、英文、数字和常用符号，不能包含【】
        certificate_file_suffix 必传: 签名授权书文件格式，当前支持jpg、png或jpeg格式的图片。
        certificate_file_contents 必传: 签名授权书文件经base64编码后的字符串。图片不超过5 MB。
        license_file_suffix 必传: 营业执照文件格式，当前支持jpg、png或jpeg格式的图片
        license_file_contents 必传: 营业执照文文件经base64编码后的字符串。图片不超过5 MB。
        """
        r = self.verify_param(param, must)
        if not r.is_succ():
            return r
        h = CommonResultHandler(lambda rsp: {VERSION_V2: rsp.get(RESULT)}[self.version()])
        return self.path('add_sign.json').post(param, h, r)

    def search_sign(self, param, must=[APIKEY]):
        """
        查询视频短信签名
        apikey 必传: 用户唯一标识，在"账号设置"-"子帐号管理"中查看
        sign 非必传: 超级短信签名
        page_num 非必传: 页码，1 开始，不传或者格式错误则默认为1
        page_size 非必传: 返回条数，必须大于 0，不传或者格式错误则默认为20
        """
        r = self.verify_param(param, must)
        if not r.is_succ():
            return r
        h = CommonResultHandler(lambda rsp: {VERSION_V2: rsp.get(RESULT)}[self.version()])
        return self.path('search_sign.json').post(param, h, r)

    def delete_sign(self, param, must=[APIKEY, SIGN]):
        """
        删除视频短信签名
        apikey 必传: 用户唯一标识，在"账号设置"-"子帐号管理"中查看
        sign 必传: 签名内容。说明：不带【】
        """
        r = self.verify_param(param, must)
        if not r.is_succ():
            return r
        h = CommonResultHandler(lambda rsp: {VERSION_V2: rsp.get(RESULT)}[self.version()])
        return self.path('delete_sign.json').post(param, h, r)
