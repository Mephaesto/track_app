#! /usr/bin/env python3
# -*- encoding: utf-8 -*-


import pymongo

client = pymongo.MongoClient("mongodb+srv://root:trackstar@track-tyc0p.gcp.mongodb.net/test?retryWrites=true")
db = client.track
baseball = db.Baseball
marathon = db.Marathon
triathlon = db.Triathlon

agility = { "A" : [["Barbell back squat", "5x5",  10], ["Bodyweight vertical jumps", "5x5", 120]],
        "B" : [["Barbell good mornings","5x5", 10], ["Broad jumps", "5x5", 120]]}

baseball.insert_one(agility)

