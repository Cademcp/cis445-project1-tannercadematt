from flask import Flask, render_template
import pymongo

client = pymongo.MongoClient('mongodb+srv://mattgates:passwordmdb@tannercadematt-kkd3l.mongodb.net/test?retryWrites=true')


db = client.Project1

collection = db.Project1

rockies = []

for x in collection.find():
    rockies.append(x)

for x in rockies:
    print(x['Player Name'])