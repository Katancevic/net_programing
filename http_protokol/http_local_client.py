import requests
req = requests.get("http://127.0.0.1:8080/", params={"name":'michael'.lower()})
print(f"Request method: GET Response status_code: {req.status_code} Response data: {req.text}")

req = requests.post("http://127.0.0.1:8080/", params = {"name":"Ivan".lower(), 'last_name':"Katancevic".lower()})
print(f"Request method: POST, Response status_code: {req.status_code} Response data: {req.text}")

req = requests.delete("http://127.0.0.1:8080/", params = {"name":"ivan".lower()})
print(f"Request method: DELETE, response status_code: {req.status_code}, Response data: {req.text}")

