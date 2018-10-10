from flask import Flask, render_template
import pymongo




app = Flask(__name__)


@app.route('/')
def index():
    team = query_database({"Team": "Rockies"})
    return render_template('home.html', team_name=team)

@app.route('/Rockies')
def displayRockies():
    team = query_database({"Team": "Rockies"})
    return render_template('index.html', team_name=team)


def query_database(query):
    client = pymongo.MongoClient(
        'mongodb+srv://mattgates:passwordmdb@tannercadematt-kkd3l.mongodb.net/test?retryWrites=true')

    db = client.Project1

    collection = db.Project1

    team_name = []

    for x in collection.find(query):
        team_name.append(x)

    client.close()

    return team_name


if __name__ == "__main__":
    app.run(debug=True)



