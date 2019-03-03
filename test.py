#! /usr/bin/env python3
# -*- encoding: utf-8 -*-


import pymongo
import pandas as pd

# This connects to the cluster
client = pymongo.MongoClient("mongodb+srv://root:trackstar@track-tyc0p.gcp.mongodb.net/test?retryWrites=true")

# This chooses which database in the array to write to
db = client.track

#These assign variables to documents in the database
baseball = db.Baseball
marathon = db.Marathon
triathlon = db.Triathlon
df = pd.read_csv("Baseball - Sheet1.csv")
#maradf = pd.read_csv("Marathon 16 weeks - Sheet1.csv")
#triadf = pd.read_csv("Triathlon - Sheet1.csv")

records_ = df.to_dict('records')
#mara_records_ = maradf.to_dict(orient = 'records')
#tria_records_ = triadf.to_dict(orient = 'records')

result = baseball.insert_many(records_)

print(result)
