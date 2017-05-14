# -*- coding: utf-8 -*-
"""
Created on Sat May 13 15:56:00 2017

"""


class LookingGlass(object):
    
    def __enter__(self):
        import sys
        #保存
        self.original_write = sys.stdout.write
        #为sys.stdout.write 打猴子补丁，替换成自己编写的方法
        sys.stdout.write = self.reverse_write
        return "JABBERWOCKY"
    
    def reverse_write(self, text):
        self.original_write(text[::-1])
        
    def __exit__(self, exc_type, exc_value, traceback):
        """Python 调用__exit__ 方法时传入的参数是None, None, None；如果抛
出了异常，这三个参数是异常数据，如下所述。"""
        import sys
        # 恢复
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print '零除错误!'
            return True
        
        
        
