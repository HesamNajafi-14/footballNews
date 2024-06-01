from django.shortcuts import render
from dotenv import load_dotenv
import os
import requests


load_dotenv()
FOOTBALL_API_KEY = os.getenv("FOOTBALL_API_KEY")


def get_api_response(request):
    url = f'https://apiv3.apifootball.com/?action=get_countries&APIkey={FOOTBALL_API_KEY}'
    
    response = requests.get(url)
    
    if response.status_code == 200: 
        countrydata = response.json()
        # Process the data as needed
        return render(request, 'api_response.html', {'countrydata': countrydata})



