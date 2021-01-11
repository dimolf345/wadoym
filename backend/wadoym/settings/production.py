# -*- coding: utf-8 -*-
"""
Production settings file
"""
# Local imports
# Third-party imports

import pymongo

from redis import StrictRedis


# Local imports
from .base import *



MONGO_DB = pymongo.MongoClient('')

REDIS_DB = StrictRedis('')

