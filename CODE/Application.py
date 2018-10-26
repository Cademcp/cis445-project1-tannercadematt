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


@app.route('/Braves')
def displayBraves():
    team = query_database({"Team": "Braves"})
    return render_template('index.html', team_name=team)


@app.route('/Brewers')
def displayBrewers():
    team = query_database({"Team": "Brewers"})
    return render_template('index.html', team_name=team)


@app.route('/Dodgers')
def displayDodgers():
    team = query_database({"Team": "Dodgers"})
    return render_template('index.html', team_name=team)


@app.route('/Astros')
def displayAstros():
    team = query_database({"Team": "Astros"})
    return render_template('index.html', team_name=team)


@app.route('/Yankees')
def displayYankees():
    team = query_database({"Team": "Yankees"})
    return render_template('index.html', team_name=team)


@app.route('/Indians')
def displayIndians():
    team = query_database({"Team": "Indians"})
    return render_template('index.html', team_name=team)


@app.route('/RedSox')
def displayRedSox():
    team = query_database({"Team": "Red Sox"})
    return render_template('index.html', team_name=team)


def query_database(query):
    client = pymongo.MongoClient(
        'mongodb+srv://mattgates:passwordmdb@tannercadematt-'
        'kkd3l.mongodb.net/test?retryWrites=true')

    db = client.Project1

    collection = db.Project1

    team_name = []

    for x in collection.find(query):
        team_name.append(x)

    client.close()

    return team_name


if __name__ == "__main__":
    app.run(debug=True)



