import urllib.request
import urllib.error
import traceback
import json

global after
after = ""

while 1:
	try:
		req = urllib.request.Request(
    		"https://www.reddit.com/reddits/.json?after="+after, 
    		data=None, 
    		headers={
        		'User-Agent': 'python3:turkey_block_scanner:v1 (by /u/ardaozkal)'
    		}
		)
		output = urllib.request.urlopen(req).read().decode()
		j = json.loads(output)
		after = j["data"]["after"]
		with open("sublist", "a") as myfile:
			for child in j["data"]["children"]:
				subname = child["data"]["display_name"]
				myfile.write(subname+"\n")
	except urllib.error.HTTPError as e:
		print("HTTP Error: " + str(e.code))

#https://www.reddit.com/reddits/.json