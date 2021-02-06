#!/usr/bin/env python3

# Thanks you to Giphy sample code and API explorer for this:
# https://developers.giphy.com/docs/resource/
# https://developers.giphy.com/explorer

import urllib
import urllib.parse
import urllib.request
import json
import time
import os

key = "1WzVd7NaYaqYzWqA4d6SgDBhcUa7QflA"
base = "giph"
ending = ".gif"

def search(prefix, schString, limit):
	url = "http://api.giphy.com/v1/gifs/search?"

	params = urllib.parse.urlencode({
	    "q": schString,
	    "api_key": key,
	    "limit": str(limit)
	})

	with urllib.request.urlopen("".join((url, params))) as response:
		data = json.loads(response.read())

	for i in range(limit):
		newurl = data["data"][i]["images"]["fixed_height_downsampled"]["url"]

		with urllib.request.urlopen(newurl) as response:
			theGif = response.read()

		f = prefix + base + str(i) + ending
		fileWriter = open(f,'wb')
		fileWriter.write(theGif)
		fileWriter.close()

	# print(json.dumps(data, sort_keys=True, indent=4))
	# print("".join((url, params)))
	# search request for 'gosling'
	# https://api.giphy.com/v1/gifs/search?api_key=1WzVd7NaYaqYzWqA4d6SgDBhcUa7QflA&q=gosling&limit=25&offset=0&rating=g&lang=en

def trending(prefix, limit):
	url = "https://api.giphy.com/v1/gifs/trending?"

	params = urllib.parse.urlencode({
	    "api_key": key,
	    "limit": str(limit),
	    "rating": "g"
	})

	with urllib.request.urlopen("".join((url, params))) as response:
		data = json.loads(response.read())

	for i in range(limit):
		newurl = data["data"][i]["images"]["fixed_height_downsampled"]["url"]

		with urllib.request.urlopen(newurl) as response:
			theGif = response.read()

		f = prefix + base + str(i) + ending

		# print("Saving gif #",i,"\n") # for testing

		fileWriter = open(f,'w')
		fileWriter.write(theGif)
		fileWriter.close()

	# example request:
	# https://api.giphy.com/v1/gifs/trending?api_key=1WzVd7NaYaqYzWqA4d6SgDBhcUa7QflA&limit=25&rating=g

def random(prefix, limit):
	url = "https://api.giphy.com/v1/gifs/random?"

	# random request
	# https://api.giphy.com/v1/gifs/random?api_key=1WzVd7NaYaqYzWqA4d6SgDBhcUa7QflA&tag=&rating=g

	params = urllib.parse.urlencode({
	    "api_key": key,
	    "tag": "",
	    "rating": "g"
	})

	for i in range(limit):
		with urllib.request.urlopen("".join((url, params))) as response:
		    data = json.loads(response.read())

		newurl = data["data"]["images"]["fixed_height_downsampled"]["url"]

		with urllib.request.urlopen(newurl) as response:
			theGif = response.read()

		f = prefix + base + str(i) + ending

		# print("Saving gif #",i,"\n") # for testing

		fileWriter = open(f,'wb')
		fileWriter.write(theGif)
		fileWriter.close()

def main():
	searchString = "happy"
	limit = 10

	if os.getcwd() == '/':
		fileTop = "/home/pi/Activities/TotalDisplay/"
	else:
		fileTop = ""

	time.sleep(60)

	# search(fileTop, searchString, limit)
	trending(fileTop, limit)
	#random(fileTop, limit)


if __name__ == '__main__':
	main()
