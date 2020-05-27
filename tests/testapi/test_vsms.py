import unittest, json, base64

from yunpian_python_sdk.model.constant import (MOBILE, TPL_ID)

from . import TestYunpianApi


class TestSmsApi(TestYunpianApi):
    '''Test SmsApi'''
    def test_tpl_batch_send(self):
        clnt = self._clnt
        param = {MOBILE: 'xxx', TPL_ID: 'xxx'}
        r = clnt.vsms().tpl_batch_send(param)
        self.show(r)

    def test_add_tpl(self):
        clnt = self._clnt
        l = {
                "vlVersion": "0.0.1",
                "subject": "title",
                "frames": [
                    {
                        "index": 1,
                        "playTimes": 1,
                        "attachments": [
                            {
                                "index": 1,
                                "fileName": "1.jpg"
                            },
                            {
                                "index": 2,
                                "fileName": "content.txt"
                            },
                        ]
                    }
                ]
            }
        param = {
            'sign': '【超级短信测试】',
            'layout': json.dumps(l),
            'material': open('/your_path/yunpian-python-sdk/tests/testapi/pkg.zip', 'rb').read()
        }
        r = clnt.vsms().add_tpl(param)
        self.show(r)

    def test_get_tpl(self):
        clnt = self._clnt
        param = {'tpl_id': '1234'}
        r = clnt.vsms().get_tpl(param)
        self.show(r)

    def test_delete_tpl(self):
        clnt = self._clnt
        param = {'tpl_id': '1234'}
        r = clnt.vsms().delete_tpl(param)
        self.show(r)

    def test_add_sign(self):
        clnt = self._clnt
        certificate_file_contents = base64.b64encode(open('xxx.jpg', 'rb').read()).decode()
        license_file_contents = base64.b64encode(open('xxx.jpg', 'rb').read()).decode()
        param = {'sign': 'test_sign', 'certificate_file_suffix': 'jpg',
                 'certificate_file_contents': certificate_file_contents,
                 'license_file_contents': license_file_contents,
                 'license_file_suffix': 'jpg'}
        r = clnt.vsms().add_sign(param)
        self.show(r)

    def test_search_sign(self):
        clnt = self._clnt
        param = {'sign': 'aaa'}
        r = clnt.vsms().search_sign(param)
        self.show(r)

    def test_delete_sign(self):
        clnt = self._clnt
        param = {'sign': 'aaa'}
        r = clnt.vsms().delete_sign(param)
        self.show(r)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()