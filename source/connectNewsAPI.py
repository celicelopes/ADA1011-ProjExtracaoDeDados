import requests
from dotenv import load_dotenv
import os 
import json

load_dotenv("../.env")

newsAPIurl = "https://newsapi.org/v2/everything"

def connectNewsApi():
    headers = {
        'X-Api-Key': os.getenv('NEWS_API_KEY')
    }

    params= {
        'q': 'bitcoin'
    }

    response = requests.get(newsAPIurl, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        #with open("./middleware/data.json", "w") as outfile:
        #   outfile.write(json.dumps(data))
        return data
    else:
        print("Erro ao obter dados:", response.status_code)