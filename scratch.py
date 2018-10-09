from flask import Flask, render_template
import pymongo

client = pymongo.MongoClient('mongodb+srv://mattgates:passwordmdb@tannercadematt-kkd3l.mongodb.net/test?retryWrites=true')


db = client.Project1

collection = db.Project1

for x in collection.find({"Age":"23"}):
    print(x)