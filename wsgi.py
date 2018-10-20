from flask import Flask
import requests
import subprocess

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
            'Origin': 'http://www.espn.com',
            'Host': 'site.api.espn.com',
            'Referer': 'http://www.espn.com/nba/scoreboard/_/date/20181019'
        }

        r = requests.get('http://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?lang=en&region=us&calendartype=blacklist&limit=100&dates=20181020&tz=America%2FNew_York', headers=headers)
        return r.text
    except:
        return "Exception."

if __name__ == "__main__":
    application.run()
