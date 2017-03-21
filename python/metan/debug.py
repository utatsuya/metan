# -*- coding:utf-8 -*-
from functools import wraps
import time
import cProfile
import pstats
import StringIO


class FuncTimer(object):
    data = {}
    show_print = False

    @classmethod
    def show(cls, count=False, total=False, average=False):

        d = []
        if count:
            d = [(k, v[0] + 1) for k, v in sorted(cls.data.items(), reverse=True, key=lambda x: x[1][0])]
        elif total:
            d = [(k, v[1]) for k, v in sorted(cls.data.items(), reverse=True, key=lambda x: x[1][1])]
        elif average:
            d = [(k, v[1] / (v[0] + 1)) for k, v in
                 sorted(cls.data.items(), reverse=True, key=lambda x: x[1][1] / (x[1][0] + 1))]

        for k, v in d:
            print str(v).ljust(18, " "), k

    @classmethod
    def clear(cls):
        cls.data = {}

    @classmethod
    def watch(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            s = time.clock()
            result = func(*args, **kwargs)
            proctime = time.clock() - s

            try:
                funcname = "{0}.{1}.{2}()".format(func.__module__, func.im_self.__name__, func.__name__)
                if cls.show_print:
                    print "{0} ms : {1}".format(proctime, funcname)
            except RuntimeError:
                funcname = "{0}.{1}()".format(func.__module__, func.__name__)
                if cls.show_print:
                    print "{0} ms : {1}".format(proctime, funcname)

            if funcname in cls.data.keys():
                cls.data[funcname][0] += 1
                cls.data[funcname][1] += proctime
            else:
                cls.data[funcname] = [0, proctime]
            return result
        return wrapper


def run_profile(func, sort_order="cumtime", count=1, strip_dir=True, name_filter=""):
    """sort_order : keywords 'ncalls', 'tottime', 'cumtime', 'filename' """

    @wraps(func)
    def wrapper(*args, **kwargs):

        def cmd():
            for i in range(count):
                func(*args, **kwargs)

        prof = cProfile.Profile()
        _profile = prof.runctx("cmd()", globals(), locals())
        stream = StringIO.StringIO()
        stats = pstats.Stats(_profile, stream=stream)
        if strip_dir:
            stats.strip_dirs()
        stats.sort_stats(sort_order)
        stats.print_stats(name_filter)
        return stream.getvalue()
    return wrapper


