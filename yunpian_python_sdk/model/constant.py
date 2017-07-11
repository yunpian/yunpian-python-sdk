# -*- coding: utf-8 -*-
'''Yunpian Constants
Created on Jul 6, 2017

@author: dzh
'''

# ************************** http ************************************
HTTP_CONN_TIMEOUT = 'http.conn.timeout'
HTTP_SO_TIMEOUT = 'http.so.timeout'
HTTP_CHARSET = 'http.charset'
HTTP_CONN_MAXPREROUTE = 'http.conn.maxpreroute'
HTTP_CONN_MAXTOTAL = 'http.conn.maxtotal'
HTTP_SSL_KEYSTORE = 'http.ssl.keystore'
HTTP_SSL_PASSWD = 'http.ssl.passwd'

# ************************** yunapian.ini ************************************
YP_FILE = 'yp.file'
YP_APIKEY = 'yp.apikey'
YP_VERSION = 'yp.version'
YP_USER_HOST = 'yp.user.host'
YP_SIGN_HOST = 'yp.sign.host'
YP_TPL_HOST = 'yp.tpl.host'
YP_SMS_HOST = 'yp.sms.host'
YP_VOICE_HOST = 'yp.voice.host'
YP_FLOW_HOST = 'yp.flow.host'
YP_CALL_HOST = 'yp.call.host'

# ************************** api ************************************
VERSION_V1 = 'v1'
VERSION_V2 = 'v2'

APIKEY = 'apikey'

CHARSET_UTF8 = 'utf-8'

# 返回值字段
CODE = 'code'
MSG = 'msg'
DETAIL = 'detail'
DATA = 'data'

# user
USER = 'user'
BALANCE = 'balance'

# 紧急联系人电话
EMERGENCY_MOBILE = 'emergency_mobile'
EMERGENCY_CONTACT = 'emergency_contact'

# 余额告警阈值
ALARM_BALANCE = 'alarm_balance'
IP_WHITELIST = 'ip_whitelist'
EMAIL = 'email'
MOBILE = 'mobile'
GMT_CREATED = 'gmt_created'
API_VERSION = 'api_version'

# sign
SIGN = 'sign'
NOTIFY = 'notify'
APPLYVIP = 'apply_vip'
ISONLYGLOBAL = 'is_only_global'
INDUSTRYTYPE = 'industry_type'
OLD_SIGN = 'old_sign'

# tpl
# 模板id
TPL_ID = 'tpl_id'
# 模板值
TPL_VALUE = 'tpl_value'

# 模板内容
TPL_CONTENT = 'tpl_content'
CHECK_STATUS = 'check_status'
REASON = 'reason'
TEMPLATE = 'template'

# 模板语言
LANG = 'lang'
COUNTRY_CODE = 'country_code'
NOTIFY_TYPE = 'notify_type'

# call
FROM = 'from'
TO = 'to'
DURATION = 'duration'
AREA_CODE = 'area_code'
MESSAGE_ID = 'message_id'
ANONYMOUS_NUMBER = 'anonymous_number'
PAGE_SIZE = 'page_size'

# flow
CARRIER = 'carrier'
FLOW_PACKAGE = 'flow_package'
_SIGN = '_sign'
CALLBACK_URL = 'callback_url'
RESULT = 'result'
FLOW_STATUS = 'flow_status'

# voice
DISPLAY_NUM = 'display_num'
VOICE_STATUS = 'voice_status'

# sms
EXTEND = 'extend'
SMS_STATUS = 'sms_status'
SMS_REPLY = 'sms_reply'
SMS = 'sms'
TOTAL = 'total'

NICK = 'nick'
UID = 'uid'

TEXT = 'text'
START_TIME = 'start_time'
END_TIME = 'end_time'
PAGE_NUM = 'page_num'

# 流量充值参数
SN = 'sn'

COUNT = 'count'
FEE = 'fee'
UNIT = 'unit'

SID = 'sid'

# batch_send 接口 增添的返回值名
TOTAL_COUNT = 'total_count'
TOTAL_FEE = 'total_fee'

SEPERATOR_COMMA = ','

RECORD_ID = 'record_id'
