from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/Services")
def services():
    return render_template('services.html')

@app.route("/Contact")
def contact():
    return render_template('contact.html')

@app.route("/About")
def about():
    return render_template('about.html')

app.run(debug=True)