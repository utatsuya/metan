# -*- coding:utf-8 -*-

__all__ = [u"MayaCommandError", u"MetanRuntimeError", u"MetanObjectNotFoundError", u"MetanAttributeError",
           u"MetanTypeError", u"MetanArgumentError"]

class MayaCommandError(RuntimeError):pass
class MetanRuntimeError(RuntimeError):pass

class MetanObjectNotFoundError(RuntimeError):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return u"{0} does not exist in Scene".format(self.name)

class MetanAttributeError(AttributeError):pass
class MetanTypeError(TypeError):pass
class MetanArgumentError(TypeError):pass


