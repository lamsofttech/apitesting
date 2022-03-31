# Import requests package
import requests
# API URL
url = "https://petstore.swagger.io/v2/pet/600"
response = requests.delete(url)
# Fetch the response code
print(response.status_code)
# Assert response code
assert response.status_code == 200
