# python

import urllib
import urllib.parse
import urllib.request
import json

# url = "http://api.giphy.com/v1/gifs/search"
url = "https://api.giphy.com/v1/gifs/random?"

# params = urllib.parse.urlencode({
#     "q": "ryan gosling",
#     "api_key": "YOUR_API_KEY",
#     "limit": "5"
# })

# random request
# https://api.giphy.com/v1/gifs/random?api_key=1WzVd7NaYaqYzWqA4d6SgDBhcUa7QflA&tag=&rating=g

# search request for 'gosling'
# https://api.giphy.com/v1/gifs/search?api_key=1WzVd7NaYaqYzWqA4d6SgDBhcUa7QflA&q=gosling&limit=25&offset=0&rating=g&lang=en

params = urllib.parse.urlencode({
    "api_key": "1WzVd7NaYaqYzWqA4d6SgDBhcUa7QflA",
    "tag": "",
    "rating": "g"
})

print("".join((url, params)))

with urllib.request.urlopen("".join((url, params))) as response:
    data = json.loads(response.read())

# with urllib.request.urlopen(url.join(params)) as response:
#     data = json.loads(response.read())
# print(json.dumps(data, sort_keys=True, indent=4))

newurl = data["data"]["images"]["fixed_height"]["url"]

with urllib.request.urlopen(newurl) as response:
	theGif = response.read()

fileWriter = open('200.gif','wb')
fileWriter.write(theGif)
fileWriter.close()
