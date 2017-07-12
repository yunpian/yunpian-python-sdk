yunpian-python-sdk
==================

`云片 <https://www.yunpian.com/>`__ SDK

快速开始
--------

-  安装SDK

   .. code:: python

       pip install yunpian-python-sdk

   **注**:
   master是最新稳定版,发布版本见\ `PyPI <https://pypi.python.org/pypi>`__

-  使用YunpianClient 

   .. code:: python
     
        from yunpian_python_sdk.model import constant as YC
        from yunpian_python_sdk.ypclient import YunpianClient
        # 初始化client,apikey作为所有请求的默认值
        clnt = YunpianClient('apikey')
        param = {YC.MOBILE:'18616020***',YC.TEXT:'【云片网】您的验证码是1234'}
        r = clnt.sms().single_send(param)
        # 获取返回结果, 返回码:r.code(),返回码描述:r.msg(),API结果:r.data(),其他说明:r.detail(),调用异常:r.exception()
        # 短信:clnt.sms() 账户:clnt.user() 签名:clnt.sign() 模版:clnt.tpl() 语音:clnt.voice() 流量:clnt.flow()

**注**:
v1.0.0不兼容之前版本\ `0.0.8 <https://github.com/yunpian/yunpian-python-sdk/releases/tag/0.0.8>`__

配置说明 (默认配置就行)
-----------------------
-  构造器配置

   -  ``YunpianClient('apikey')``
   -  ``YunpianClient('apikey',conf)``,
      conf字典key详见model.constant.YP\_\*

-  apikey的优先级:接口的param[APIKEY] > 构造器的apikey > 构造器的conf[YP\_APIKEY]

源码说明
--------
-  接口参数的apikey可以不传，因为所有接口默认传入`YunpianClient`构造时的apikey
-  接口默认使用v2版本,可以在调用时指定版本,如\ ``clnt.sms().version('v1').single_send(param)``
-  API单元测试目录tests,支持tox
-  分支说明: master是最新发布版本,develop是待发布的分支(开源贡献可以pull request到develop分支)

联系我们
--------

`云片支持
QQ <https://static.meiqia.com/dist/standalone.html?eid=30951&groupid=0d20ab23ab4702939552b3f81978012f&metadata=%7B%22name%22:%22github%22%7D>`__

SDK开源QQ群: 106469530

.. image:: docs/sdk_qq.jpeg
   :height: 60px
   :width: 60px
   :scale: 15%

文档链接
--------

-  `API文档 <https://www.yunpian.com/api2.0/guide.html>`__

其他SDK
-------

-  https://github.com/yunpian/sms/tree/master/yunpian/python/ypclient
   支持py2/3