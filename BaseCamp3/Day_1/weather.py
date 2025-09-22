import requests
import json
'''
https://rapidapi.com/worldapi/api/open-weather13/playground/apiendpoint_812ee767-435a-46b4-af3a-849301e54d3c
'''
url = "https://open-weather13.p.rapidapi.com/city"

querystring = {"city":"bangalore","lang":"EN"}

headers = {
	"x-rapidapi-key": "bd4ffe1ccdmshc135537bc11c012p1c8982jsnfb84e45d5a3e",
	"x-rapidapi-host": "open-weather13.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

print(json.dumps(response.json(), indent=4, sort_keys=True))
#print(response.json())