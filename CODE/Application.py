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
    return render_template('team_info.html', team_name=team)


@app.route('/Braves')
def displayBraves():
    team = query_database({"Team": "Braves"})
    return render_template('team_info.html', team_name=team)


@app.route('/Brewers')
def displayBrewers():
    team = query_database({"Team": "Brewers"})
    return render_template('team_info.html', team_name=team)


@app.route('/Dodgers')
def displayDodgers():
    team = query_database({"Team": "Dodgers"})
    return render_template('team_info.html', team_name=team)


@app.route('/Astros')
def displayAstros():
    team = query_database({"Team": "Astros"})
    return render_template('team_info.html', team_name=team)


@app.route('/Yankees')
def displayYankees():
    team = query_database({"Team": "Yankees"})
    return render_template('team_info.html', team_name=team)


@app.route('/Indians')
def displayIndians():
    team = query_database({"Team": "Indians"})
    return render_template('team_info.html', team_name=team)


@app.route('/RedSox')
def displayRedSox():
    team = query_database({"Team": "Red Sox"})
    return render_template('team_info.html', team_name=team)


@app.route('/NLDS')
def displayNLDS():
    series1 = query_database_games({"Series": "NLDS1"})
    series2 = query_database_games({"Series": "NLDS2"})
    return render_template('NLDS_ALDS_info.html', playoff_rounds1=series1, playoff_rounds2=series2)


@app.route('/ALDS')
def displayALDS():
    series1 = query_database_games({"Series": "ALDS1"})
    series2 = query_database_games({"Series": "ALDS2"})
    return render_template('NLDS_ALDS_info.html', playoff_rounds1=series1, playoff_rounds2=series2)


@app.route('/NLCS')
def displayNLCS():
    series = query_database_games({"Series": "NLCS"})
    return render_template('series_info.html', playoff_rounds=series)


@app.route('/ALCS')
def displayALCS():
    series = query_database_games({"Series": "ALCS"})
    return render_template('series_info.html', playoff_rounds=series)


@app.route('/WorldSeries')
def displayWorldSeries():
    series = query_database_games({"Series": "WS"})
    return render_template('series_info.html', playoff_rounds=series)


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


def query_database_games(query):
    client = pymongo.MongoClient(
        'mongodb+srv://mattgates:passwordmdb@tannercadematt-'
        'kkd3l.mongodb.net/test?retryWrites=true')

    db = client.Project1

    collection = db.Games

    playoff_rounds = []

    for x in collection.find(query):
        playoff_rounds.append(x)

    client.close()

    return playoff_rounds


if __name__ == "__main__":
    app.run(debug=True)



