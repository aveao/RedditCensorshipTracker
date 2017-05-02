import urllib.request
import urllib.error
import traceback
import json
import re

global counter
counter = 1

#http://redditlist.com/nsfw?page=2

while counter != 7:
	try:
		output = urllib.request.urlopen("http://redditlist.com/nsfw?page="+str(counter)).read().decode()
		counter = counter + 1
		matches = re.findall(r"\/r\/[a-zA-Z0-9]*'", output)
		nsfwtexts = ''
		for match in matches:
			nsfwtexts = nsfwtexts +str(match).replace("/r/","").replace("'","")+"\n"
		with open("nsfwsublisttemp", "a") as myfile:
			myfile.write(nsfwtexts)
	except urllib.error.HTTPError as e:
		print("HTTP Error: " + str(e.code))

lines_seen = set() # holds lines already seen
outfile = open("nsfwsublist", "w")
for line in open("nsfwsublisttemp", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()