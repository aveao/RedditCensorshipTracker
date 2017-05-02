import urllib.request
import urllib.error
import traceback

global count
count = 0

def get_subreddit_list():
    try:
        with open("nsfwsublist", "r") as sublist:
            sublistsplit = sublist.read().split("\n")
            return sublistsplit
    except FileNotFoundError:
        print("No sublist file found! Please create one and place a subreddit name on each line.")
    except Exception:
        print(traceback.format_exc())

while 1:
	subslist = get_subreddit_list()
	count = 0
	for val in subslist:
		count = count + 1
		try:
			req = urllib.request.Request(
    			"https://www.reddit.com/r/"+val+".json", 
    			data=None, 
    			headers={
        			'User-Agent': 'python3:turkey_block_scanner_part2:v1.1 (by /u/ardaozkal)'
    			}
			)
			output = urllib.request.urlopen(req)
			print("Not blocked ("+str(count)+"): " + val)
		except urllib.error.HTTPError as e:
			if int(e.code) == 451:
				print("Block found ("+str(count)+"): " + val)