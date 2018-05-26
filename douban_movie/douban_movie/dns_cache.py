# encoding=utf-8
# ---------------------------------------
#   版本：0.1
#   日期：2016-04-26
#   作者：九茶<bone_ace@163.com>
#   开发环境：Win64 + Python 2.7
# ---------------------------------------

import socket
# from gevent import socket

_dnscache = {}

def _setDNSCache():
    """ DNS缓存 """

    def _getaddrinfo(*args, **kwargs):
        if args in _dnscache:
            # print str(args) + " in cache"
            return _dnscache[args]
        else:
            # print str(args) + " not in cache"
            _dnscache[args] = socket._getaddrinfo(*args, **kwargs)
            return _dnscache[args]

    if not hasattr(socket, '_getaddrinfo'):
        socket._getaddrinfo = socket.getaddrinfo
        socket.getaddrinfo = _getaddrinfo