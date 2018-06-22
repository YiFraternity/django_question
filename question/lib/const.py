"""
常量类
"""
class _const(object):
    class ConstError(PermissionError):pass

    def __setattr__(self,name,value):
        if name in self.__dict__.keys():
            raise self.ConstError("不能重新绑定常量(%s)" % name)
        self.__dict__[name] = value
        pass

    def __delattr__(self,name):
        if name in self.__dict__:
            raise self.ConstError("不能解除绑定常量(%s)" % name)
        raise NameError(name)

import sys
sys.modules[__name__] = _const()
