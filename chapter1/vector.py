#coding=utf-8

from math import hypot

class Vector:
    """自定义二维向量"""
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __repr__(self):
        """
        repr 就是通过 __repr__ 这个特殊方法来得到一个对象的字符串表示形式的。
        
        __repr__ 和 __str__ 的区别在于，
        后者是在 str() 函数被使用，
        或是在用 print 函数打印一个对象的时候才被调用的，
        并且它返回的字符串对终端用户更友好。
        
        如果一个对象没有 __str__ 函数，
        而 Python 又需要调用它的时候，
        解释器会用 __repr__ 作为替代。
        """
        return "Vector(%r, %r)"%(self.x, self.y)
        
    def __abs__(self):
        """
        中缀运算符的基本原则就是不改变操作对象，而是产出一个新的值。
        """
        return hypot(self.x, self.y)
        
    def __bool_(self):
        """
        默认情况下，我们自己定义的类的实例总被认为是真的，
        除非这个类对 __bool__ 或者 __len__ 函数有自己的实现。
        bool(x) 的背后是调用 x.__bool__() 的结果；
        如果不存在 __bool__ 方法，那么 bool(x) 会尝试调用 x.__len__()。
        
        若返回 0，则 bool 会返回 False；否则返回 True。
        """
        #return self.bool(abs(self))
        #更高效
        return bool(self.x or self.y)
        
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
        
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    