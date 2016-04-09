# -*- coding:utf-8 -*-
# filename:TestPost
# 16/1/20 下午4:01
# from yunpian.DES import DES

__author__ = 'bingone'
from yunpian.SmsOperator import SmsOperator
from yunpian.VoiceOperator import VoiceOperator
from yunpian.TplOperator import TplOperator
from yunpian.UserOperator import UserOperator
from yunpian.FlowOperator import FlowOperator
from yunpian.Tea import Tea
import sys
import json

reload(sys)
sys.setdefaultencoding('utf-8')

# 返回格式可参考官网:   www.yunpian.com
# You can get the APIKEY and APISECRET from http://www.yunpian.com/ when log on.

# 单条短信发送
APIKEY='xxxxxx'
API_SECRET='12345678'
smsOperator = SmsOperator(APIKEY)
result = smsOperator.single_send({'mobile': '13004000020', 'text': '【yunpian】您的验证码是4444'})
print json.dumps(result.content, ensure_ascii=False)

#
# TEA加密短信发送
# 要生成带api_secret 的对象
smsOperator = SmsOperator(APIKEY,API_SECRET)
result = smsOperator.single_send(
    {'mobile': '13000400001', 'text': '13400000001', 'encrypt': Tea.encrypt_name})
print json.dumps(result.content, ensure_ascii=False)

# DES加密短信发送
# result = smsOperator.single_send(
#     {'mobile': '13000000002', 'text': '13000000002', 'encrypt': DES.encrypt_name})
# print json.dumps(result.content, ensure_ascii=False)

#
# 批量短信发送
print json.dumps(smsOperator.batch_send({'mobile': '13000000001,13000000002', 'text': '【yunpian】您的验证码是0000'}).content,
                 ensure_ascii=False)
# 个性化短信发送
print json.dumps(smsOperator.multi_send(
    {'mobile': '13000000003,13000000004', 'text': '【yunpian】您的验证码是4442,【yunpian】您的验证码是4441'}).content,
                 ensure_ascii=False)

# 获取账号信息
userOperator = UserOperator(APIKEY)
result = userOperator.get()
print json.dumps(result.content,ensure_ascii=False)

# 短信模板
tplOperator = TplOperator(APIKEY)
result = tplOperator.get()
print json.dumps(result.content,ensure_ascii=False)
print json.dumps(tplOperator.get_default({'tpl_id': '2'}).content, ensure_ascii=False)

# 流量
flowOperator = FlowOperator(APIKEY)
print json.dumps(flowOperator.recharge({'mobile': '18720085991', 'sn': '1008601'}).content, ensure_ascii=False)

# 语音
voiceOperator = VoiceOperator(APIKEY)
print json.dumps(voiceOperator.send({'mobile': '18720085991', 'code': '0012'}).content, ensure_ascii=False)
