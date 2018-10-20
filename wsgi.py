from flask import Flask
import requests

application = Flask(__name__)

@application.route('/')
def hello():
    return 'Hello World!'

@application.route('/version')
def version():
    return 'v1.0'

@application.route('/scoreboard')
def scoreboard():
    try:
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
    except:
        return "Exception."

if __name__ == "__main__":
    application.run()
