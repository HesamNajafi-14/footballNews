from django.shortcuts import render
from dotenv import load_dotenv
import os
import requests


load_dotenv()
FOOTBALL_API_KEY = os.getenv("FOOTBALL_API_KEY")


def get_api_response(request):
    #url = f'https://apiv3.apifootball.com/?action=get_countries&APIkey={FOOTBALL_API_KEY}'
    #url = f'https://apiv3.apifootball.com/?action=get_events&from=2024-06-01&to=2024-06-01&league_id=152&APIkey={FOOTBALL_API_KEY}'
    #url = f'https://heisenbug-champions-league-live-scores-v1.p.rapidapi.com/api/championsleague/match/events?team1=Borussia%20Dortmund&team2=Real%20Madrid'
    #url = 'https://www.chelseafc.com/en/api/fixtures/league-table?entryId=30EGwHPO9uwBCc75RQY6kg'
    url = 'https://web-api.varzesh3.com/v1.0/livescore/today'
    response = requests.get(url)
    
    if response.status_code == 200: 
        data = response.json()
        # Process the data as needed
        return render(request, 'api_response.html', {'data': data})



