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
pitching = {'type': 'pitching', 'note': "Create a contrast training effect by going from heavy to light(and thus increasing your velocity when you come back to light)", 'throw': [["2-4", "5", 30], ["2-4", "7", 30],["2-4", "9", 45],["2-4", "5", 30]]}

#marathon
maraSchedule = {'type' : 'maraSchedule', "1" : [[{"week" : 1}, {"day" : 1}, "Flex", 3], [{"week" : 1}, {"day" : 2}, "Reg", 3], [{"week" : 1}, {"day" : 3}, "Rest", 0], [{"week" : 4}, {"day" : 5}, "Reg", 3], [{"week"                        :1}, {"day" : 5}, "Rest", 0], [{"week" : 1}, {"day" : 6}, "Rest", 0], [{"week" : 1}, {"day" : 7}, "Long", 6]],
             "2" : [["Flex", 3], ["Fartlek", 3], ["Rest", 0], ["Reg", 4], ["Rest", 0], ["AYF", 3], ["Long", 8]],
             "3" : [["Flex", 3], ["Tempo", 4], ["Rest", 0], ["Reg", 5], ["Rest", 0], ["AYF", 4], ["Long", 10]],
             "4" : [["Flex", 3], ["Intervals", 4], ["Rest", 0], ["Reg", 6], ["Rest", 0], ["AYF", 4], ["Long", 12]],
             "5" : [["Flex", 3], ["Hills", 4], ["Rest", 0], ["Reg", 6], ["Rest", 0], ["AYF", 5], ["Long", 10]],
             "6" : [["Flex", 3], ["Tempo", 5], ["Rest", 0], ["Reg", 5], ["Rest", 0], ["Rest", 0], ["Long", 14]],
             "7" : [["Flex", 3], ["Intervals", 5], ["Rest", 0], ["Reg", 5], ["Rest", 0], ["AYF", 5], ["Long", 10]],
             "8" : [["Flex", 3], ["Hills", 4], ["Rest", 0], ["Reg", 6], ["Rest", 0], ["AYF", 5], ["Long", 16]],
             "9" : [["Flex", 3], ["Tempo", 6], ["Rest", 0], ["Reg", 5], ["Rest", 0], ["AYF", 5], ["Long", 10]],
             "10" : [["Flex", 3], ["Intervals", 5], ["Rest", 0], ["Reg", 6], ["Rest", 0], ["AYF", 4], ["Long", 18]],
             "11" : [["Flex", 3], ["Hills", 5], ["Rest", 0], ["Reg", 8], ["Rest", 0], ["AYF", 5], ["Long", 10]],
             "12" : [["Flex", 3], ["Tempo", 8], ["Rest", 0], ["Reg", 6], ["Rest", 0], ["Rest", 0], ["Long", 20]],
             "13" : [["Flex", 3], ["Intervals", 4], ["Rest", 0], ["Reg", 8], ["Rest", 0], ["AYF", 5], ["Long", 10]],
             "14" : [["Flex", 3], ["Hills", 4], ["Rest", 0], ["Reg", 6], ["Rest", 0], ["AYF", 4], ["Long", 12]],
             "15" : [["Flex", 3], ["Tempo", 3], ["Rest", 0], ["Reg", 5], ["Rest", 0], ["AYF", 4], ["Long", 7]],
             "16" : [["Flex", 3], ["Reg", 3], ["Rest", 0], ["Reg", 3], ["Rest", 0], ["AYF", 2], ["Race!", 26.2]]}
Mdefinitions = {'type' : 'Mdefinitions', "1" : [["Flex", "Flex Day: The best day of the week to replace your run with a cross-training session or a day off!"], ["Fartlek", "Fartlek: Swedish for \“speed play.\" Fartlek workouts involve running at different speeds for varying periods--good preparation for shifting gears in a race"], ["Rest", "Take a day off!"], ["Reg", "Regular Run: A run performed at a comfortable, not-too-hard pace."], ["AYF", "As You Feel (AYF): For these runs, leave your watch and your cares behind. Run for the fun of it, not because you're training. Run as fast—or as slow—as you like."], ["Long", "Long Run: The most important workout of the week for distance runners. Long runs build both strength and confidence."], ["Intervals", "Intervals: Running short (usually between 200 and 1600 meters), fast repeats with recovery jogs in between. Interval training builds speed and endurance."], ["Tempo", "Tempo Run: A training run (usually 20 to 30 minutes) at a pace slightly slower than 10K race pace."], ["Hills", "Run in an area with lots of inclines!"]]}

# This inserts a singular dictionary into the associated document
baseball.replace_one({'type': "agility"},agility, upsert=True)
baseball.replace_one({'type': "speed"}, speed, upsert=True)
#baseball.insert_one(speed)
baseball.replace_one({'type': "conditioning"}, conditioning, upsert=True)
baseball.replace_one({'type': "pitching"}, pitching, upsert=True)

marathon.replace_one({'type' : "maraSchedule"},maraSchedule, upsert=True)
marathon.replace_one({'type' : "Mdefinitions"},Mdefinitions, upsert=True)
