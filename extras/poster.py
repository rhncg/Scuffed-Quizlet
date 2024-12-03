import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')

with open('/Users/rohan/Developer/Scuffed-Quizlet/extras/terms.json', 'r') as file:
    data = json.load(file)
    print(data)
    headers = {
        "Authorization": f"Bearer {token}"
    }
    print(requests.post("https://scuffed-quizlet-api.vercel.app/data", json=data, headers=headers))