from flask import Flask, render_template




app = Flask(__name__)


@app.route('/')
def index():
    return render_template('compare.html')


@app.route('/rate')
def calculateRate():
    return render_template('calcRate.html')


@app.route("/time")
def calculateTime():
    return render_template('calcTime.html')



@app.route("/annuity")
def annuity():
    return render_template("annuity.html")

if __name__ == "__main__":
    app.run(debug=True)
