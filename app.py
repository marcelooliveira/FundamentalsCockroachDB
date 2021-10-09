from flask import Flask, render_template, current_app
from flask_bootstrap import Bootstrap
from leaderboard import Leaderboard
from os import environ 

app = Flask(__name__)
Bootstrap(app)

# Initialize the db connection
conn_string = environ.get('DB_URI')
# conn_string = app.config.get('DB_URI')

leaderboard = Leaderboard(conn_string)

@app.route("/")
def index():

    scores = leaderboard.get_scores()
    return render_template('index.html',
                            scores=scores)

@app.route("/player")
def player():

    return render_template('player.html')

if __name__ == '__main__':
    app.run(debug=True)
