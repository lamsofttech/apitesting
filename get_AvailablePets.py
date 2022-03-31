# Import request package
import requests
# Get a response by invoking a get request and passing url as the parameter
response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus?status=available")
# get a json response and assign it to a variable
json_response = response.json()
# get the status code and assign it to a variable
code = response.status_code
# Print the status code
print(code)
# Validate  the response code
assert code == 200, "code doesnt match"
# print the response in json format
print(json_response)






