import pymongo
import pprint

# This connects to the cluster
client = pymongo.MongoClient("mongodb+srv://root:trackstar@track-tyc0p.gcp.mongodb.net/test?retryWrites=true")

# This chooses which database in the array to write to
db = client.track

marathon = db.Marathon

print(marathon.find_one({'type' : "maraSchedule", "1" : 3}))