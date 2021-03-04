import requests
import csv

inputYear = input('Enter the starting year of a Season: ')
# Formating '####-##'
inputYear = inputYear + '-' + str(int(inputYear[2:]) + 1)

# Requesting JSON data
url = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=' + \
    inputYear + '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight='
headerArgs = {
    'User-Agent': 'Mozilla/5.0',
    'Referer': 'https://stats.nba.com/players/drives/',
    'x-nba-stats-origin': 'stats',
    'x-nba-stats-token': 'true',
}
r = requests.get(url, headers=headerArgs)
jsonData = r.json()

playerSets = jsonData['resultSets'][0]['rowSet']

# Writing to csv
with open(inputYear + '.csv', 'w', newline='') as file:
    writter = csv.writer(file)
    # Header
    headers = []
    for i in jsonData['resultSets'][0]['headers']:
        headers.append(i)
    writter.writerow(headers)
    # Body
    body = []
    for i in range(0, len(playerSets)):
        for j in range(0, len(playerSets[i])):
            body.append(playerSets[i][j])
        writter.writerow(body)
        body.clear()
