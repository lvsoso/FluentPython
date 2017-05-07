# -*- coding: utf-8 -*-
"""
Created on Sun May 07 18:06:09 2017


"""

import array

numbers = array.array('h', [-2, -1, 0, 1, 2])

#利用含有5 个短整型有符号整数的数组（类型码是'h'）创建一个memoryview。
memv = memoryview(numbers)

print(len(memv)) #5
print (memv[0]) #-2

#创建一个memv_oct，这一次是把memv 里的内容转换成'B' 类型，也就是无符号字符。
memv_oct = memv.cast('B')

print (memv_oct.tolist()) #[254, 255, 255, 255, 0, 0, 1, 0, 2, 0]

#把位于位置5 的字节赋值成4。
#把占2 个字节的整数的高位字节改成了4，所以这个有符号整数的值就变成
#了1024。
memv_oct[5] = 4
print (numbers) #array('h', [-2, -1, 1024, 1, 2])
