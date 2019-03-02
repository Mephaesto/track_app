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
        "B" : [["Barbell good mornings","5x5", 10], ["Broad jumps", "5x5", 120]],
        "C": [["Anterior reaching lunges", "3x8", 10],["Lateral reaching lunges", "3x8", 10],
            ["Posterior reaching lunges", "3x8", 120]]}
speed = {'type': 'speed', 'A': [["Lateral sled drag into sprint explosion", "8x20", 75]],
        'B': [["Falling sprint", "8x30", 75]], 'C': [["Sliding lateral lunge", "4x10", 10],
            ["Plank", "4x60", 60]]}
conditioning = {'type': 'conditioning', 'A': [["Three-point stance sprint", "6x40", 45]],
        'B': [["30 yd lateral shuffle", "6x1", 45]], 'C': [["KB/DB swing", "5x8", 10],
            ["Explosive push ups", "5x8", 10], ["Split squat jumps", "5x3", 90]]}

# This inserts a singular dictionary into the associated document
baseball.replace_one({'type': "agility"},agility, upsert=True)
baseball.replace_one({'type': "speed"}, speed, upsert=True)
#baseball.insert_one(speed)
baseball.replace_one({'type': "conditioning"}, conditioning, upsert=True)

