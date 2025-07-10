from flask import Flask, render_template , flash

app = Flask(__name__)

app.secret_key= "29dsjh9238jhrjhw8787uhu8"

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/logout")
def logout():
    flash("You have been logged out!", "Success")
    return render_template('index.html')

app.run(debug=True)