# -*- coding: utf-8 -*-
"""
Created on Thu May 11 22:12:12 2017

#python 3

"""


from array import array
import reprlib
import math
import numbers
import string
import functools
import operator
import itertools

class Vector:
    
    shortcut_names = string.lowercase
    
    typecode = 'd'
    
    
    def __init__(self, components):
        self._components = array(self.typecode, components)
        
    def __iter__(self):
        return iter(self._components)
    
    def __repr__(self):
        components = reprlib.repr(self._components)
        print("-->",components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)
    
    def __str__(self):
        return str(tuple(self))
    
    def __bytes__(self):
        """转换为byte"""
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))
        
    def __eq__(self, other):
        """判断是否相等"""
        #return tuple(self) == tuple(other)

        #if len(self) != len(other):
         #   return False
        #for a, b in zip(self, other):
         #   if a != b:
          #     return False
           # return True
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))
    

    def __abs__(self):
        """绝对值"""
        return math.sqrt(sum(x * x for x in self))
    
    def __neg__(self):
        """负值"""
        return Vector(-x for x in self)
    
    def __pos__(self):
        """正值"""
        return Vector(self)

    def __bool__(self):
        """布尔值"""
        return bool(abs(self))
    
    
    @classmethod
    def frombytes(cls, octets):
        """使用字节流创建对象"""
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)
    
    def __len__(self):
        """返回长度"""
        return len(self._components)
    
    def __getitem__(self, index):
        """索引"""
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._componentsp[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))
    
    def __getattr__(self, name):
        """动态获取属性"""
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))
        
    def __setattr__(self, name, value):
        """设置新属性值"""
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    def __hash__(self):
        hashes = (hash(x) for x in self._components)
        return functools.reduce(operator.xor, hashes, 0)
    
    def angle(self, n):
        """计算夹角"""
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n-1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 -a
        else:
            return a
        
    def angles(self):
        """计算角度"""
        #创建生成器表达式，按需计算所有角坐标。
        return (self.angle(n) for n in range(1, len(self)))
    
    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('h'): # 超球面坐标
            fmt_spec = fmt_spec[:-1]
            #使用itertools.chain 函数生成生成器表达式，无缝迭代向量的模和各个角坐标。
            coords = itertools.chain([abs(self)],
                                         self.angles())
            outer_fmt = '<{}>'
        else:
            coords = self
            outer_fmt = '({})'
        #创建生成器表达式，按需格式化各个坐标元素。
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(', '.join(components))
    
    def __add__(self, other):
        #python 3
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)
            return Vector(a + b for a, b in pairs)
        except TypeError:
            return NotImplemented
    
    def __radd__(self, other):
        return self + other
        
            
                                   
if __name__ == "__main__":
    print(format(Vector([1, 1]), 'h'))
    print(format(Vector([1, 1]), '.3eh'))
    print(format(Vector([-1, -1, -1, -1]), 'h'))
    print("=========================")
    v1 = Vector([3, 4, 5])
    vv = v1 + (10, 20, 30)
    print(vv)