'''
Created on Jul 6, 2017

@author: dzh
'''

from sdk.api import flow, sign, sms, tpl, user, voice
from sdk.model.constant import VERSION_V2, YP_VERSION, CHARSET_UTF8, VERSION_V1, \
    CODE, APIKEY, MSG, DETAIL
from sdk.model.result import Result, Code


class ApiFactory(object):
    '''Yunpian APIs Factory'''

    def __init__(self, clnt):
        assert clnt, "YunpianClient is None"
        self.__clnt = clnt

    def api(self, name):
        '''return special API by package's name'''
        assert name, "api name is None"

        api = None
        if flow.__name__ == name:
            api = flow.FlowApi()
        elif sign.__name__ == name:
            api = sign.SignApi()
        elif sms.__name__ == name:
            api = sms.SmsApi()
        elif tpl.__name__ == name:
            api = tpl.TplApi()
        elif user.__name__ == name:
            api = user.UserApi()
        elif voice.__name__ == name:
            api = voice.VoiceApi()

        assert api, "not found api-" + name

        api.init(self.__clnt)
        return api

class YunpianApiResult(object):
    '''interface to retrieve the Result from the response'''

    def result(self, rsp, h, r=Result()):
        ''' 
        Args:
            rsp: a dict representing api's response
            h: ResultHandler
            r: Result
        Returns:
             r Result
        '''
        raise NotImplementedError("implemented this")

    def code(self, rsp, version=VERSION_V2):
        '''
        Args:
            rsp: a dict representing api's response
            version: api's version
        Returns:
            api's int code
        '''
        raise NotImplementedError("implemented this")

class YunpianApi(YunpianApiResult):
    '''
    basic API object
    '''

    def init(self, clnt):
        '''initialize api by YunpianClient'''
        assert clnt, "clnt is None"
        self.clnt = clnt
        self.apikey = clnt.apikey()
        self.version = clnt.conf(YP_VERSION, defval=VERSION_V2)
        self.charset = clnt.conf(self.HTTP_CHARSET, defval=CHARSET_UTF8)

    def client(self, clnt=None):
        if clnt :
            self.clnt = clnt
        return self.clnt

    def host(self, host=None):
        if host:
            self.host = host
        return self.host

    def version(self, version=None):
        if version :
            self.version = version
        return self.version

    def path(self, path=None):
        if path :
            self.path = path
        return self.path

    def apikey(self, apikey=None):
        if apikey :
            self.apikey = apikey
        return self.apikey

    def charset(self, charset=None):
        if charset :
            self.charset = charset
        return self.charset

    def name(self):
        '''api name, default is package.__name__'''
        return __name__

    def uri(self):
        return '{}/{}/{}/{}'.format(self.host(), self.version(), self.name(), self.path())


    def post(self, param, h, r=Result()):
        '''
        Args:
            param: request parameters
            h: ResultHandler
            r: YunpianApiResult
        '''
        try:
            rsp = self.clnt.post(self.uri(), param={})
            return self.result(rsp, h, r)
        except ValueError as err:
            return h.catch_exception(err, r)

    def result(self, rsp, h, r=Result()):
        code = self.code(rsp, self.version())
        return h.succ(code, rsp, r) if code == Code.OK else h.fail(code, rsp, r)

    def code(self, rsp, version=VERSION_V2):
        if rsp is None:return Code.OK

        code = Code.UNKNOWN_EXCEPTION
        if version == VERSION_V1 :
            code = int(rsp[CODE]) if CODE in rsp else Code.UNKNOWN_EXCEPTION
        elif version == VERSION_V2:
            code = int(rsp[CODE]) if CODE in rsp else Code.OK

        return code

    def verify_param(self, param={}, must=[], r=Result()):
        '''return Code.ARGUMENT_MISSING if every key in must not found in param'''
        if APIKEY not in param:
            param[APIKEY] = self.apikey

        for p in must:
            if p not in param:
                r.code(Code.ARGUMENT_MISSING).detail(p)
                break

        return r

class ResultHandler(object):
    '''interface to parse the response'''

    def succ(self, code, rsp, r):
        ''' return success Result
        Args:
            code: = 0
            rsp: a dict representing api's response
            r: Result
        Returns:
            r
        '''
        raise NotImplementedError("implemented this")

    def fail(self, code, rsp, r):
        ''' return failure Result
        Args:
            code: != 0
            rsp: a dict representing api's response
            r: Result
        Returns:
            r
        '''
        raise NotImplementedError("implemented this")

    def catch_exception(self, e, r):
        ''' return exception Result
        Args:
            e: Error
            rsp: a dict representing api's response
            r: Result
        Returns:
            r
        '''
        raise NotImplementedError("implemented this")

def CommonResultHandler(ResultHandler):

    def __init__(self, version, func):
        ''' return exception Result
        Args:
            version: api's version
            func: Result receive data by calling func(version,rsp)
        '''
        self.__version = version
        self.__func = func

    def succ(self, code, rsp, r=Result()):
        return r.code(code).msg(rsp[MSG] if MSG in rsp else None).data(self.__func(self.__version, rsp))

    def faili(self, code, rsp, r=Result()):
        return r.code(code).msg(rsp[MSG] if MSG in rsp else None).detail(rsp[DETAIL] if DETAIL in rsp else None)

    def catch_exception(self, e, r=Result()):
        return r.code(Code.UNKNOWN_EXCEPTION).exception(e, True)

