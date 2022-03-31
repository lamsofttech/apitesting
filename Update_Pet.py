# Import json and requests packages
import requests
import json
# API URL
url = "https://petstore.swagger.io/v2/pet"
# read input from json file
file = open("UpdatePet.json", "r")
# call the read method and assign the result to a variable
json_input = file.read()
# call the load method
request_json = json.loads(json_input)
# Print the results read from the json file
print(request_json)
# make a put request with json input body
response = requests.put(url, request_json)
# Validating response code
assert response.status_code != 200
