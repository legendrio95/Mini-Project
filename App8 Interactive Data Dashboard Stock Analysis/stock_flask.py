from flask import Flask, render_template
from Stock_analysis import stock_main

app = Flask(__name__)


@app.route('/plot/')
def plot():
    return stock_main()


@app.route('/')
def home():
    return render_template("Home.html")


@app.route('/about/')
def about():
    return render_template("About.html")


if __name__ == "__main__":
    app.run(debug=False)
