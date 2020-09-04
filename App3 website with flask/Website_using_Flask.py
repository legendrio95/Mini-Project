from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("Journey.html")


@app.route('/quotes/')
def quotes():
    return render_template("Quotes.html")


@app.route('/secret_message/')
def secret():
    return render_template("secret.html")


if __name__ == "__main__":
    app.run(debug=True)
