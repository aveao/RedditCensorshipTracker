import http.client
import traceback

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

subslist = get_subreddit_list()
count = 0
for val in subslist:
	count = count + 1
	try:
            conn = http.client.HTTPConnection("www.reddit.com")
            conn.putrequest("HEAD", "/r/"+val+".json")
            conn.putheader("User-Agent", "python3:turkey_block_scanner_part2:v1.1 (by /u/ardaozkal)")
            conn.endheaders()
            conn.send("")
            response = conn.getresponse()
            if str(response.status) == "451":
                print(val + ": Blocked")
            else:
                print(val + ": Not blocked")
	except Exception:
		print(traceback.format_exc())

print("Done.")