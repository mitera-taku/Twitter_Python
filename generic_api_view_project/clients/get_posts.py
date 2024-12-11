import requests # type: ignore
import json

url = 'http://localhost:8000/api/posts/'

response = requests.get(url) # type: ignore

print(response.status_code)
print(response.text)
print(response.headers)

json_response = json.loads(response.text)
next_url = json_response.get('next')
if next_url:
    response = requests.get(next_url)
    print(response.text)


