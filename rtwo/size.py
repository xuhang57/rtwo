"""
rtwo size.

"""
from abc import ABCMeta

from rtwo.provider import AWSProvider, EucaProvider, OSProvider


class BaseSize(object):
    __metaclass__ = ABCMeta


class Size(BaseSize):

    provider = None

    def __init__(self, lc_size):
        self._size = lc_size
        self.id = self._size.id
        self.name = self._size.name
        self.price = self._size.price
        self.ram = self._size.ram
        self.disk = self._size.disk
        if hasattr(self._size, 'extra'):
            self.extra = self._size.extra
        else:
            self.extra = {}
        self.cpu = self.extra.get('cpu', 0)
        self.ephemeral = self.extra.get('ephemeral', 0)

    def __unicode__(self):
        return str(self)

    def __str__(self):
        return reduce(
            lambda x, y: x+y,
            map(unicode, [self.__class__, " ", self.json()]))

    def __repr__(self):
        return str(self)

    def json(self):
        return {'id': self._size.name,
                'provider': self.provider.identifier,
                'alias': self._size.id,
                'name': self._size.name,
                'cpu': self.cpu,
                'ram': self._size.ram,
                'root': self._size.disk,
                'disk': self.ephemeral,
                'bandwidth': self._size.bandwidth,
                'price': self._size.price}


class EucaSize(Size):

    provider = EucaProvider


class AWSSize(Size):

    provider = AWSProvider


class OSSize(Size):

    provider = OSProvider
