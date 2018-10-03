from flask import Flask, render_template

testDB = {
    "Player": {
        "Name": "Carlos Gonzalez",
        "Number": "22",
        "Position": "OF",
        "Age": "27",
        "Hits": "L",
        "Throws": "L",
        "Image": "Ap_Creative_Stock_Header.jpg"
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
    return render_template(index.html, playerName=name, playerNumber=number, playerPosition=position, playerAge=age,
                           playerHits=hits, playerThrows=throws, playerImage=image)


if __name__ == "__main__":
    app.run(debug=True)



