import urllib.request
import urllib.error
import traceback
import json

global after
after = ""

global count
count = 0

global subnames
subnames = ""

while 1:
	try:
		req = urllib.request.Request(
    		"https://www.reddit.com/reddits/.json?after="+after, 
    		data=None, 
    		headers={
        		'User-Agent': 'python3:turkey_block_scraper:v1.2 (by /u/ardaozkal)'
    		}
		)
		output = urllib.request.urlopen(req).read().decode()
		j = json.loads(output)
		after = j["data"]["after"]
		print("current after: " + str(after) + ", current count: " + str(count))
		for child in j["data"]["children"]:
			subnames = subnames + child["data"]["display_name"] + "\n"
			count = count + 1
		with open("sublist", "a") as myfile:
			myfile.write(subnames)
	except urllib.error.HTTPError as e:
		print("HTTP Error: " + str(e.code))