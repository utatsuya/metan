# -*- coding:utf-8 -*-

class MayaCommandError(RuntimeError):pass
class MetanRuntimeError(RuntimeError):pass

class MetanObjectNotFoundError(RuntimeError):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "{0} does not exist in Scene".format(self.name)

class MetanAttributeError(AttributeError):pass
class MetanTypeError(TypeError):pass
class MetanArgumentError(TypeError):pass


