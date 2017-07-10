'''
Created on Jul 4, 2017

@author: dzh
'''
import unittest

from api import TestYunpianApi


class TestUserApi(TestYunpianApi):
    '''Test UserApi'''


    def _testGet(self):
        clnt = self.clnt
        r = clnt.user().get()
        print(self.toJson(r))

        # v1
        # r = clnt.user().version(constants.VERSION_V1).get()

    def _testSet(self):
        clnt = self.clnt
        param = {'emergency_mobile':'18616020000'}
        r = clnt.user().set(param)
        print(self.toJson(r))


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
