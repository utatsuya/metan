# -*- coding:utf-8 -*-
from __future__ import print_function, absolute_import, division
import sys
from logging import getLogger, INFO, DEBUG, StreamHandler, Handler, Formatter
import maya.cmds as cmds

MSG_FORMAT  = "%(name)s %(levelname)s : %(message)s"
MSG_FORMAT_DEBUG  = "%(name)s %(asctime)s %(levelname)s : %(message)s"
DATE_FORMAT = "%H:%M:%S"


def set_level(info=False, debug=False):
    global log
    global __handler
    if info is False and debug is False:
        return

    if info: level = INFO
    elif debug: level = DEBUG
    else: level = None

    if level:
        log.setLevel(level)
        __handler.setLevel(level)


class MayaHandler(Handler):
    def __init__(self):
        Handler.__init__(self)
        # self.fmt_info = Formatter(MSG_FORMAT, DATE_FORMAT)
        # self.fmt_debug = Formatter(MSG_FORMAT_DEBUG, DATE_FORMAT)

    def emit(self, record):
        # msg = self.format(record)
        # msg = record.msg
        # print(record.levelname)
        print(dir(record))
        if record.levelname == "DEBUG":
            # self.setFormatter(self.fmt_debug)
            # msg = self.format(record)
            msg = "{0} {1} {2} : {3}".format(record.name, record.created, record.levelname, record.msg)
        else:
            # self.setFormatter(self.fmt_info)
            # msg = self.format(record)
            msg = "{0} {2} : {3}".format(record.name, record.levelname, record.msg)


        print(msg)
        # sys.stdout.write(msg + u"\n")

log = getLogger(u"Metan")
# __formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# __formatter = Formatter(MSG_FORMAT, DATE_FORMAT)
# __handler = NullHandler()
# __handler = StreamHandler()
__handler = MayaHandler()
# __handler.setFormatter(__formatter)
log.addHandler(__handler)
log.propagate=0
# set_level(DEBUG)
