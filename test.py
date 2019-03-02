#! /usr/bin/env python3
# -*- encoding: utf-8 -*-


import pymongo

# This connects to the cluster
client = pymongo.MongoClient("mongodb+srv://root:trackstar@track-tyc0p.gcp.mongodb.net/test?retryWrites=true")

# This chooses which database in the array to write to
db = client.track

#These assign variables to documents in the database
baseball = db.Baseball
marathon = db.Marathon
triathlon = db.Triathlon

baseball.create_index([('type', pymongo.ASCENDING)], unique=True)
marathon.create_index([('type', pymongo.ASCENDING)], unique=True)
triathlon.create_index([('type', pymongo.ASCENDING)], unique=True)

# This is a python dictionary which you can pass to the insert function to be parsed into BSON
agility = {'type': 'agility', "A" : [["Barbell back squat", "5x5",  10], ["Bodyweight vertical jumps", "5x5", 120]],
        "B" : [["Barbell good mornings","5x5", 10], ["Broad jumps", "5x5", 120]]}

# This inserts a singular dictionary into the associated document
baseball.insert_one(agility)

