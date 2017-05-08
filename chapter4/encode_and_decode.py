# -*- coding: utf-8 -*-
"""
Created on Sun May 07 23:14:39 2017


"""


"""
字符的具体表述取决于所用的编码

编码是在码位和字节序列之间转换时使用的算法。
把码位转换成字节序列的过程是编码；
把字节序列转换成码位的过程是解码；
"""
s = u'café'
print s.__repr__()
print len(s)

b = s.encode('utf-8')
#字节序列b 有5 个字节（在UTF-8 中，“é”的码位编码成两个字节）。
print b.__repr__()

b.decode('utf8')
print b.__repr__()


"""
bytes 和bytearray 对象
"""
cafe = u'café'.encode('utf-8') #bytes('café', encoding='utf-8')

print cafe[0]
print cafe[:1]#bytes 对象的切片还是bytes 对象

cafe_arr = bytearray(cafe)
print cafe_arr[-1:]#bytearray 对象的切片还是bytearray 对象。


"""
python3

cafe = bytes('café', encoding='utf-8')

print(cafe[0])
print( cafe[:1])#bytes 对象的切片还是bytes 对象

cafe_arr = bytearray(cafe)
print(cafe_arr[-1:])#bytearray 对象的切片还是bytearray 对象。

print(bytes.fromhex('31 4B CE A9'))

99
b'c'
bytearray(b'\xa9')

b'1K\xce\xa9'
"""