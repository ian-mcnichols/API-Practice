import json
import requests


api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
print("response:", response.json())
print("headers:", [x for x in response.headers])

new_item = {
    "userId": 1,
    "title": "Buy milk",
    "completed": False
}
api_url = "https://jsonplaceholder.typicode.com/todos"
response = requests.post(api_url, json=new_item)
print(response.json())
print(response.status_code)

new_item = {
    "userId": 2,
    "title": "Buy milk",
    "completed": False,
}

new_item = json.dumps(new_item)
headers = {"Content-Type":"application/json"}
response = requests.post(api_url, new_item, headers=headers)
print(response.json())
print(response.status_code)

api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
print(response.json())

new_item = {"userId": 1, "title": "Wash car", "completed": True}
response = requests.put(api_url, json=new_item)
print(response.json())
print(response.status_code)

new_item = {"title": "Mow lawn"}
response = requests.patch(api_url, json=new_item)
print(response.json())
print(response.status_code)

response = requests.delete(api_url)
print(response.json())
print(response.status_code)

response = requests.get(api_url)
print(response.json())
print(response.status_code)
