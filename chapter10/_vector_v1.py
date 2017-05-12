# -*- coding: utf-8 -*-
"""
Created on Thu May 11 14:38:24 2017
"""

from array import array
import reprlib
import math


class Vector:
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
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))
        
    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))  # <6>

    def __bool__(self):
        return bool(abs(self))
    
    
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)
    

if __name__ == "__main__":
    v6 = Vector(range(6))
    print(v6)
    print(abs(v6))
    octets = bytes(v6)
    print(octets)
    print(bool(v6), bool(Vector([0, 0])))
    print(repr(v6))
    """
    (0.0, 1.0, 2.0, 3.0, 4.0, 5.0)
    7.416198487095663
    b'd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x10@\x00\x00\x00\x00\x00\x00\x14@'
    True False
    --> array('d', [0.0, 1.0, 2.0, 3.0, 4.0, ...])
    Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])
    """