import requests
import os 
from dotenv import load_dotenv

load_dotenv()
url = "https://distance-calculator8.p.rapidapi.com/calc"

querystring = {"startLatitude":"-26.311960","startLongitude":"-48.880964","endLatitude":"-26.313662","endLongitude":"-48.881103"}

headers = {
	"X-RapidAPI-Key": os.getenv('RAPID_API_KEY'),
	"X-RapidAPI-Host": "distance-calculator8.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
print(response.json())