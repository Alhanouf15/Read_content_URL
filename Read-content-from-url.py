import requests
link = "https://www.youtube.com/"
f= requests.get(link)
print(f.text)