import requests

r = requests.get("https://www.reddit.com/")

print(r.content)