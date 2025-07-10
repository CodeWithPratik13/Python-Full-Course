from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
        "john": 45,
        "pratik": 68,
        "rounak": 58,
        "gopal": 60,
        "ritik":100
    }
    return render_template('index.html', marks=marks)

app.run(debug=True)