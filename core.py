# [START app]
import logging
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/scoreboard')
def scoreboard():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Origin': 'stats.nba.com',
        'Host': 'stats.nba.com',
        'Referer': 'https://stats.nba.com/scores/10/19/2018',
        'x-nba-stats-origin': 'stats',
        'X-NewRelic-ID': 'VQECWF5UChAHUlNTBwgBVw==',
        'x-nba-stats-token': 'true',
    }

    r = requests.get('https://stats.nba.com/stats/scoreboardV2?DayOffset=0&LeagueID=00&gameDate=10%2F19%2F2018', headers=headers)
    return r.text

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]