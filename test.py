#! /usr/bin/env python3
# -*- encoding: utf-8 -*-


import pymongo

client = pymongo.MongoClient("mongodb://root:trackstar2019@track-tyc0p.gcp.mongodb.net/test?retryWrites=true")
db = client.track


