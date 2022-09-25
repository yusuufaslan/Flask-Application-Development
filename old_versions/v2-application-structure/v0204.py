from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home_v5.html", day=day_name)


@app.route("/movies")
def movies_page():
    return render_template("movies_v3.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
