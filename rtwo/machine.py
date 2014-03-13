"""
rtwo machine.

"""
from abc import ABCMeta

from rtwo.provider import AWSProvider, EucaProvider, OSProvider

from threepio import logger


class BaseMachine(object):
    __metaclass__ = ABCMeta


class Machine(BaseMachine):

    provider = None

    lc_images = None

    def __init__(self, lc_image):
        self._image = lc_image
        self.id = lc_image.id
        self.alias = lc_image.id
        self.name = lc_image.name

    def __unicode__(self):
        return str(self)

    def __str__(self):
        return reduce(
            lambda x, y: x+y,
            map(unicode, [self.__class__, " ", self.json()])
        )

    def __repr__(self):
        return str(self)

    def json(self):
        return {'id': self.id,
                'alias': self.alias,
                'name': self.name,
                'provider': self.provider.name}


class AWSMachine(Machine):

    provider = AWSProvider


class EucaMachine(Machine):

    provider = EucaProvider


class OSMachine(Machine):

    provider = OSProvider
