import requests
import json

def scoreboard():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Origin': 'http://www.espn.com',
            'Host': 'site.api.espn.com',
            'Referer': 'http://www.espn.com/nba/scoreboard/_/date/20181019'
        }

        r = requests.get('http://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?lang=en&region=us&calendartype=blacklist&limit=100&dates=20181020&tz=America%2FNew_York', headers=headers)
        data = json.loads(r.text)
        
        jsonData = '{"scoreboard": [#]}'
        jsonObjects = ""
        
        for event in data["events"]:
            name = event["name"]
            shortName = event["shortName"]
            status = event["status"]["type"]["description"]
            airTime = event["status"]["type"]["detail"]
            isCompleted = str(event["status"]["type"]["completed"])

            #TEAM-HOME
            displayNameHome = event["competitions"][0]["competitors"][0]["team"]["displayName"]
            abbreviationHome = event["competitions"][0]["competitors"][0]["team"]["abbreviation"]
            logoHome = event["competitions"][0]["competitors"][0]["team"]["logo"]
            scoreHome = event["competitions"][0]["competitors"][0]["score"]
            
            #TEAM-AWAY
            displayNameAway = event["competitions"][0]["competitors"][1]["team"]["displayName"]
            abbreviationAway = event["competitions"][0]["competitors"][1]["team"]["abbreviation"]
            logoAway = event["competitions"][0]["competitors"][1]["team"]["logo"]
            scoreAway = event["competitions"][0]["competitors"][1]["score"]
            
            jsonObject = '{"eventName": "' + name + '","eventShortName": "' + shortName + '","eventStatus": "' + status + '","eventAirTime": "' + airTime + '","eventIsCompleted": "' + isCompleted + '","displayNameHome": "' + displayNameHome + '","abbreviationHome": "' + abbreviationHome + '","logoHome": "' + logoHome + '","scoreHome": "' + scoreHome + '","displayNameAway": "' + displayNameAway + '","abbreviationAway": "' + abbreviationAway + '","logoAway": "' + logoAway + '","scoreAway": "' + scoreAway + '"}'
            jsonObjects = jsonObjects + jsonObject + ","

            print(name)
            print(shortName)
            print(status)
            print(airTime)
            print(isCompleted)
            print(displayNameHome)
            print(abbreviationHome)
            print(logoHome)
            print(scoreHome)
            print(displayNameAway)
            print(abbreviationAway)
            print(logoAway)
            print(scoreAway)

        jsonObjects = jsonObjects[:-1]
        jsonData = jsonData.replace("#", jsonObjects)
    except:
        print("Exception")
scoreboard()