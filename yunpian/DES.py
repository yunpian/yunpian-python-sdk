# -*- coding:utf-8 -*-
#filename:DES
#16/3/10 上午11:22
# need pyDes,download from this site : http://pydes.sourceforge.net/

# import base64
# import pyDes

__author__ = 'bingone'
class DES:
    encrypt_name='des'
    # @staticmethod
    # def encrypt_yunpian(s,key):
    #     if s==None or key==None or len(key) <8:
    #         raise Exception('encrypt data or key wrong')
    #     des = pyDes.des(key, pyDes.ECB, padmode=pyDes.PAD_PKCS5)
    #     return base64.encodestring(des.encrypt(s))[:-1]
    # @staticmethod
    # def decrypt_yunpian(s,key):
    #     if s==None or key==None or len(key) <8:
    #         raise Exception('encrypt data or key wrong')
    #     des = pyDes.des(key, pyDes.ECB, padmode=pyDes.PAD_PKCS5)
    #     return des.decrypt(base64.decodestring(s))
if __name__ == '__main__':
    pass
    # print DES.decrypt_yunpian("RLlJ+bgSQnRRguZMMPqQWPu7QmWwrxdSbgEIRSxtZD4X7RBRmdIllQ==","12345678")


