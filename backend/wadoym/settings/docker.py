# -*- coding: utf-8 -*-
"""
Docker settings file
"""
# Local imports
# Third-party imports

import pymongo

from redis import StrictRedis


# Local imports
from .base import *



MONGO_DB = pymongo.MongoClient('mongodb/wadoym')

REDIS_DB = StrictRedis('redisdb')

