# -*- coding:utf-8 -*-
#filename:Config
#16/1/20 下午4:23

__author__ = 'bingone'
yunpian_config={}

# You can get the APIKEY and APISECRET from http://www.yunpian.com/ when log on.
yunpian_config['APIKEY'] = ""

yunpian_config['API_SECRET'] = ""






#System
yunpian_config['SMS_HOST'] = 'https://sms.yunpian.com'
yunpian_config['VOICE_HOST'] = 'https://voice.yunpian.com'
yunpian_config['FLOW_HOST'] = 'https://flow.yunpian.com'
yunpian_config['VERSION'] = '/v2'

# test System
# yunpian_config['SMS_HOST'] = 'http://127.0.0.1:8081'
# yunpian_config['VOICE_HOST'] = 'http://127.0.0.1:8081'
# yunpian_config['FLOW_HOST'] = 'http://127.0.0.1:8081'
# yunpian_config['VERSION'] = '/v2'
# yunpian_config['APIKEY'] = "xxx"
# yunpian_config['API_SECRET'] = "12345678"

# 短信
yunpian_config['URI_SEND_SINGLE_SMS'] = yunpian_config['SMS_HOST'] + yunpian_config['VERSION'] + "/sms/single_send.json"
yunpian_config['URI_SEND_BATCH_SMS'] = yunpian_config['SMS_HOST'] + yunpian_config['VERSION'] + "/sms/batch_send.json"
yunpian_config['URI_SEND_MULTI_SMS'] = yunpian_config['SMS_HOST'] + yunpian_config['VERSION'] + "/sms/multi_send.json"
yunpian_config['URI_SEND_TPL_SINGLE_SMS'] = yunpian_config['SMS_HOST'] + yunpian_config['VERSION'] + '/sms/tpl_signle_send.json'
yunpian_config['URI_SEND_TPL_BATCH_SMS'] = yunpian_config['SMS_HOST'] + yunpian_config['VERSION'] + '/sms/tpl_batch_send.json'
yunpian_config['URI_PULL_SMS_STATUS'] = yunpian_config['SMS_HOST'] + yunpian_config['VERSION'] + "/sms/pull_status.json"
# 获取回复短信
yunpian_config['URI_PULL_SMS_REPLY'] = yunpian_config['SMS_HOST'] + yunpian_config['VERSION'] + "/sms/pull_reply.json"
# 查询回复短信
yunpian_config['URI_GET_SMS_REPLY'] = yunpian_config['SMS_HOST'] + yunpian_config['VERSION'] + "/sms/get_reply.json"
# 查短信发送记录
yunpian_config['URI_GET_SMS_RECORD'] = yunpian_config['SMS_HOST'] + yunpian_config['VERSION'] + "/sms/get_record.json"

# 语音
yunpian_config['URI_SEND_VOICE_SMS'] = yunpian_config['VOICE_HOST'] + yunpian_config['VERSION'] + "/voice/send.json"
yunpian_config['URI_PULL_VOICE_STATUS'] = yunpian_config['VOICE_HOST'] + yunpian_config['VERSION'] + "/voice/pull_status.json"

# 流量
yunpian_config['URI_GET_FLOW_PACKAGE'] = yunpian_config['FLOW_HOST'] + yunpian_config['VERSION'] + "/flow/get_package.json"
yunpian_config['URI_PULL_FLOW_STATUS'] = yunpian_config['FLOW_HOST'] + yunpian_config['VERSION'] + "/flow/pull_status.json"
yunpian_config['URI_RECHARGE_FLOW'] = yunpian_config['FLOW_HOST'] + yunpian_config['VERSION'] + "/flow/recharge.json"

# 用户操作
yunpian_config['URI_GET_USER_INFO'] = yunpian_config['SMS_HOST'] + yunpian_config['VERSION'] + "/user/get.json"
yunpian_config['URI_SET_USER_INFO'] = yunpian_config['SMS_HOST'] + yunpian_config['VERSION'] + "/user/set.json"


# 模板操作
yunpian_config['URI_GET_DEFAULT_TEMPLATE'] = yunpian_config['SMS_HOST'] + yunpian_config['VERSION'] + "/tpl/get_default.json"
yunpian_config['URI_GET_TEMPLATE'] = yunpian_config['SMS_HOST'] + yunpian_config['VERSION'] + "/tpl/get.json"
yunpian_config['URI_ADD_TEMPLATE'] = yunpian_config['SMS_HOST'] + yunpian_config['VERSION'] + "/tpl/add.json"
yunpian_config['URI_UPD_TEMPLATE'] = yunpian_config['SMS_HOST'] + yunpian_config['VERSION'] + "/tpl/update.json"
yunpian_config['URI_DEL_TEMPLATE'] = yunpian_config['SMS_HOST'] + yunpian_config['VERSION'] + "/tpl/del.json"



# print yunpian_config