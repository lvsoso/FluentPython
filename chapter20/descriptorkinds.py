#coding=utf-8


### 辅助显示函数 ###

def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]

def display(obj):
    cls = type(obj)
    if cls is type:
        return '<class {}>'.format(obj.__name__)
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return '<{} object>'.format(cls_name(obj))

def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print('-> {}.__{}__({})'.format(cls_name(args[0]), name, pseudo_args))


### 演示使用类 ###

class Overriding:
    """ 数据描述符 或 强制描述符 覆盖型描述符"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)

    def __set__(self, instance, value):
        print_args('set', self, instance, value)

class OverridingNoGet:
    """ 没有重写 '__get__' 方法 覆盖型描述符 """

    def __set__(self, instance, value):
        print_args('set', self, instance, value)

class NonOverriding:
    """ 非数据描述符或遮盖型描述符（会遮盖描述符） """

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)


class Managed:
    """ 托管类 """
    over = Overriding()
    over_no_get = OverridingNoGet()
    non_over = NonOverriding()

    def spam(self):
        print('-> Managed.spam({})'.format(display(self)))


if __name__ == "__main__":
    ##################
    """
    obj = Managed()
    print(obj.over)
    print(Managed.over)
    print('===============')
    obj.over = 7
    print(obj.over)
    print('===============')
    obj.__dict__['over'] = 8
    print(vars(obj))
    print(obj.over)
    """
    ##########################
    """
    obj = Managed()
    print(obj.over_no_get)
    print(Managed.over_no_get)
    print('===============')
    obj.over_no_get = 7
    print(obj.over_no_get)
    print('===============')
    obj.__dict__['over_no_get'] = 9
    #over_no_get 实例属性会遮盖描述符，但是只有读操作是如此。
    print(obj.over_no_get) 
    obj.over_no_get = 7
    print(obj.over_no_get)
    """
    ##########################
    """
    obj = Managed()
    print(obj.non_over)
    print(Managed.non_over)
    print('===============')
    obj.non_over = 7
    print(obj.non_over)
    print('===============')
    print(Managed.non_over) 
    del obj.non_over
    print(obj.non_over)
    """
    obj =Managed()
    print(obj.spam)
    print(Managed.spam)
    obj.spam = 7
    print(obj.spam)
    print(Managed.spam)
