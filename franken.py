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

base = "giph"
ending = ".gif"

# print("".join((url, params)))

# with urllib.request.urlopen(url.join(params)) as response:
#     data = json.loads(response.read())
# print(json.dumps(data, sort_keys=True, indent=4))

for i in range(5):
	with urllib.request.urlopen("".join((url, params))) as response:
	    data = json.loads(response.read())

	newurl = data["data"]["images"]["fixed_height_downsampled"]["url"]

	with urllib.request.urlopen(newurl) as response:
		theGif = response.read()

	f = base + str(i) + ending
	fileWriter = open(f,'wb')
	fileWriter.write(theGif)
	fileWriter.close()
