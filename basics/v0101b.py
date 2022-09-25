from flask import Flask


app = Flask(__name__)


@app.route("/")
def home_page():
    return """<!DOCTYPE html>
            <html lang="en">
              <head>
                <meta charset="utf-8"/>
                <title>My movies</title>
              </head>
              <body>
                <h1>My movie collection</h1>
              </body>
            </html>
            """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
