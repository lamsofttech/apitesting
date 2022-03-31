# Import json and requests package
import requests
import json
# API URL
url = "https://petstore.swagger.io/v2/pet"
# read input from json file
file = open("CreatePet.json", "r")
json_input = file.read()
request_json = json.loads(json_input)
print(request_json)
# make a post request with json input body
response = requests.post(url, request_json)
# Validating response code
assert response.status_code != 200
