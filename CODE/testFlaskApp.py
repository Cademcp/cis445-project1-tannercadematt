from flask import Flask, render_template

testDB = {
    "Player": {
        "Name": "Carlos Gonzalez",
        "Number": "5",
        "Position": "OF",
        "Age": "32",
        "Hits": "L",
        "Throws": "L",
        "Image": "Ap_Creative_Stock_Header.jpg",
        "Height": "6' 1\"",
        "Weight": "220lbs"
    }


}

app = Flask(__name__)


@app.route('/')
def index():
    name = testDB['Player']['Name']
    number = testDB['Player']['Number']
    position = testDB['Player']['Position']
    age = testDB['Player']['Age']
    hits = testDB['Player']['Hits']
    throws = testDB['Player']['Throws']
    image = testDB['Player']['Image']
    height = testDB['Player']['Height']
    weight = testDB['Player']['Weight']
    return render_template('index.html', playerName=name,
                           playerNumber=number, playerPosition=position, playerAge=age,
                           playerHits=hits, playerThrows=throws,
                           playerImage=image, playerHeight=height,
                           playerWeight=weight)


if __name__ == "__main__":
    app.run(debug=True)



