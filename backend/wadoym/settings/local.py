# -*- coding: utf-8 -*-
"""
Local settings file
"""
# Local imports
# Third-party imports

import pymongo

from redis import StrictRedis


# Local imports
from .base import *



MONGO_DB = pymongo.MongoClient('localhost/wadoym')

REDIS_DB = StrictRedis('localhost')

