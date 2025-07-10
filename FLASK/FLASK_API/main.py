from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def json():
    marks = {
        "Pratik" :78,
        "rounak" : 66,
        "ritik": 88,
        "Shivam": 100,
        "vishal": 69
    }
    values = [1,marks,69]
    return jsonify(values)

app.run(debug=True)