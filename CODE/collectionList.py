import pymongo

client = pymongo.MongoClient(
    'mongodb+srv://mattgates:passwordmdb@tannercadematt-kkd3l.mongodb.net/test?retryWrites=true')


db = client.Project1

collection = db.Project1

rockies = []
dodgers = []
braves = []
brewers = []

print("=========================================Rockies")
for x in collection.find({"Team": "Rockies"}):
    rockies.append(x)

for x in rockies:
    print(x['Player Name'])

print("=========================================Dodgers")
for x in collection.find({"Team": "Dodgers"}):
    dodgers.append(x)

for x in dodgers:
    print(x['Player Name'])

print("=========================================Braves")
for x in collection.find({"Team": "Braves"}):
    braves.append(x)

for x in braves:
    print(x['Player Name'])

print("=========================================Brewers")
for x in collection.find({"Team": "Brewers"}):
    brewers.append(x)

for x in brewers:
    print(x['Player Name'])
