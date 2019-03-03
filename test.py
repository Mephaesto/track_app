#! /usr/bin/env python3
# -*- encoding: utf-8 -*-


import pymongo
import pandas as pd

# This connects to the cluster
client = pymongo.MongoClient("mongodb+srv://root:trackstar@track-tyc0p.gcp.mongodb.net/test?retryWrites=true")

# This chooses which database in the array to write to
db = client.track
db.Baseball.drop()
db.Marathon.drop()
db.Traithlon.drop()

#These assign variables to documents in the database
baseball = db.Baseball
marathon = db.Marathon
triathlon = db.Triathlon
df = pd.read_csv("Baseball - Sheet1.csv")
maradf = pd.read_csv("Marathon 16 weeks - Sheet1.csv")
triadf = pd.read_csv("Triathlon - Sheet1.csv")

records_ = df.to_dict('records')
mara_records_ = maradf.to_dict(orient = 'records')
tria_records_ = triadf.to_dict(orient = 'records')

result = baseball.insert_many(records_)
result1 = marathon.insert_many(mara_records_)
result2 = triathlon.insert_many(tria_records_)

#print(result)
#print(result1)
#print(result2)

data = pd.DataFrame(list(baseball.find({'Week': 3, 'Day': 2})))

print(data)
