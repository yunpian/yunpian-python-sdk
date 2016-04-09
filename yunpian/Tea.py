# -*- coding:utf-8 -*-
# filename:Tea
# 16/1/20 下午6:58
from ctypes import *
import base64
import struct
__author__ = 'bingone'


class Tea(object):

    encrypt_name='tea'
    @staticmethod
    def encrypt_yunpian(s,key):
        pass
        key=key+key+key+key
        # 0 get []key
        key = Tea.str_to_ints(key)
        # 1 str to bytes
        encrypt_bytes = list(s) #bytearray(s)
        # 2 add bytes to align,get encrypt_bytes
        n=8 - len(encrypt_bytes)%8
        for i in range(0,n):
            encrypt_bytes.insert(0,chr(0))
        encrypt_bytes[0]=chr(n)
        ret_bytes = ''
        for i in range(0,len(encrypt_bytes),8):
            pass
            c=''.join(encrypt_bytes)
            # print len (c)
            # print  ''.join(encrypt_bytes).decode('utf8')

            # print  ''.join(encrypt_bytes)[i:i+7].decode('utf8')
            tmp_int = struct.unpack('>II',''.join(encrypt_bytes)[i:i+8])
            x=Tea.encipher(tmp_int,key)
            # print x
            ret_bytes +=x
        #

        return base64.encodestring(ret_bytes)[0:-1]

    @staticmethod
    def byte_to_int(content,offset):
        pass

    @staticmethod
    def str_to_ints(k):
        kk=[]
        kk.append(int(str(k)[0:7],16))
        kk.append(int(str(k)[8:15],16))
        kk.append(int(str(k)[16:23],16))
        kk.append(int(str(k)[24:31],16))
        return kk

    @staticmethod
    def encipher(v, k,n = 32):

        y = c_int32(v[0]);
        z = c_int32(v[1]);
        sum = c_int32(0);
        # y=v[0]
        # z=v[1]
        # sum=0
        delta = 0x9E3779B9;
        if(delta > 0):
            delta = delta - 4294967296;

        w = [0, 0]

        while (n > 0):
            sum.value += delta
            # y += ((z <<4) + k[0]) ^ (z + sum) ^ ((z >>5) + k[1])
            # z += ((y <<4) + k[2]) ^ (y + sum) ^ ((y >>5) + k[3])
            y.value += (z.value << 4) + k[0] ^ z.value + sum.value ^ (z.value >> 5) + k[1]
            z.value += (y.value << 4) + k[2] ^ y.value + sum.value ^ (y.value >> 5) + k[3]
            n -= 1

        w[0] = y.value
        w[1] = z.value

        # return w
        return struct.pack('>ii',w[0],w[1])

    @staticmethod
    def decipher(v, k):
        y = c_uint32(v[0])
        z = c_uint32(v[1])
        sum = c_uint32(0xC6EF3720)
        delta = 0x9E3779B9
        n = 32
        w = [0, 0]

        while (n > 0):
            z.value -= (y.value << 4) + k[2] ^ y.value + sum.value ^ (y.value >> 5) + k[3]
            y.value -= (z.value << 4) + k[0] ^ z.value + sum.value ^ (z.value >> 5) + k[1]
            sum.value -= delta
            n -= 1

        w[0] = y.value
        w[1] = z.value
        return w




if __name__ == '__main__':
    pass
    tea = Tea()
    x=tea.encrypt_yunpian('','002d88e24fdaf41801d1d18ef8109996')[:-1]
    print (tea.encrypt_yunpian('','002d88e24fdaf41801d1d18ef8109996'))
    from pyDes import *
    import pyDes
    des = pyDes.des('12345678', pyDes.ECB, padmode=pyDes.PAD_PKCS5)
    print base64.encodestring(des.encrypt('12345678'))