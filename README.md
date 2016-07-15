
# SDK使用指南

---
## python
### 添加依赖包
1. 使用pip安装依赖

```
pip install yunpian-sdk-python
```

或者 下载包[]()进行安装

```
pip install yunpian-sdk-python-1.0.0.tar.gz
```

### 使用


```
# -*- coding:utf-8 -*-
# filename:TestPost
# 16/1/20 下午4:01

__author__ = 'bingone'
from yunpian.SmsOperator import SmsOperator
from yunpian.VoiceOperator import VoiceOperator
from yunpian.TplOperator import TplOperator
from yunpian.UserOperator import UserOperator
from yunpian.FlowOperator import FlowOperator
import sys
import json

reload(sys)
sys.setdefaultencoding('utf-8')

# 更多内容请参考 <url>https://www.yunpian.com/api2.0/howto.html</url>
# 如您第一次使用云片网，强烈推荐先看云片网络设置教程 <url>https://blog.yunpian.com/?p=94</url>
# 使用说明
# 1、登陆 <url>http://www.yunpian.com/</url> 获取APIKEY
# 2、使用APIKEY生成操作类SmsOperator/UserOperator/TplOperator/FlowOperator/VoiceOperator
# 3、通过Result来接收返回值，通过ok()判断是否成功。具体可参考示例
# 
# 返回值参考
# <url>https://www.yunpian.com/api2.0/sms.html</url>
# <url>https://www.yunpian.com/api2.0/record.html</url>
# 单条短信发送
APIKEY = 'xxxxxx'
smsOperator = SmsOperator(APIKEY)
result = smsOperator.single_send({'mobile': '13004000020', 'text': '【云片网】您的验证码是4444'})
print json.dumps(result.content, ensure_ascii=False)

# 批量短信发送（批量发送的接口耗时比单号码发送长，如果需要更高并发速度，推荐使用single_send/tpl_single_send）
# print json.dumps(smsOperator.batch_send({'mobile': '13000000001,13000000002', 'text': '【云片网】您的验证码是0000'}).content,
#                  ensure_ascii=False)

# （这个是个性化接口发送，批量发送的接口耗时比单号码发送长，如果需要更高并发速度，推荐使用single_send/tpl_single_send，不推荐使用）
# print json.dumps(smsOperator.multi_send(
#     {'mobile': '13000000003,13000000004', 'text': '【云片网】您的验证码是4442,【云片网】您的验证码是4441'}).content,
#                   ensure_ascii=False)

# （这个是指定模板单发接口发送，特殊字符会导致编码问题，不推荐使用）
# print json.dumps(smsOperator.tpl_single_send({'mobile': '13000000001', 'text': '【云片网】您的验证码是0000'}).content,
#                   ensure_ascii=False)
#
# （这个是指定模板批量接口发送，批量发送的接口耗时比单号码发送长，如果需要更高并发速度，推荐使用single_send/tpl_single_send，特殊字符会导致编码问题，不推荐使用）
# print json.dumps(smsOperator.tpl_batch_send({'mobile': '13000000001,13000000002', 'text': '【云片网】您的验证码是0000'}).content,
#                   ensure_ascii=False)
#

# 获取账号信息
userOperator = UserOperator(APIKEY)
result = userOperator.get()
print json.dumps(result.content, ensure_ascii=False)

# 短信模板
tplOperator = TplOperator(APIKEY)
result = tplOperator.get()
print json.dumps(result.content, ensure_ascii=False)
print json.dumps(tplOperator.get_default({'tpl_id': '2'}).content, ensure_ascii=False)

# 流量
# flowOperator = FlowOperator(APIKEY)
# print json.dumps(flowOperator.recharge({'mobile': '13020080000', 'sn': '1008601'}).content, ensure_ascii=False)

# 语音
# voiceOperator = VoiceOperator(APIKEY)
# print json.dumps(voiceOperator.send({'mobile': '13020080000', 'code': '0012'}).content, ensure_ascii=False)


```



