import http.client
import traceback
from subprocess import call

global count

def get_subreddit_list():
    try:
        with open("sublist", "r") as sublist: # replace sublist with nsfwsublist to check NSFW blocks
            sublistsplit = sublist.read().split("\n")
            return sublistsplit
    except FileNotFoundError:
        print("No sublist file found! Please create one and place a subreddit name on each line.")
    except Exception:
        print(traceback.format_exc())

#subslist = ["twinks", "firstworldanarchists"]
subslist = get_subreddit_list()
count = 0
for val in subslist:
	count = count + 1
	try:
            conn = http.client.HTTPConnection("www.reddit.com")
            conn.putrequest("HEAD", "/r/"+val+".json")
            conn.putheader("User-Agent", "python3:turkey_block_scanner_part2:v1.2 (by /u/ardaozkal)")
            conn.endheaders()
            conn.send("")
            response = conn.getresponse()
            if response.status == 451:
                call(["notify-send", 'Found blocked SR', val])
                print("Blocked (" + str(count) + "): " + val)
            else:
                print("Not Blocked (" + str(count) + "): " + val)
	except Exception:
		print(traceback.format_exc())

print("Done.")