# RedditCensorshipTracker
A Reddit Censorship Tracker to track subdomains blocked in Turkey (and potentially other countries, however, seeing the Transparency Reports, only Germany has opted to block a sub, which is `/r/watchpeopledie` (which involves people actually dying. NSFW and NSFL. You have been warned.)).

### How to set up

- Install python3. I have only used it on python3.6, but earlier versions should work too.
- Clone or download the project (duh).
- If you want to update the scrapes (you should!), run `python3 redditsubscraper.py` (it goes on forever! don't forget to stop it by hand) and `python3 nsfwscraper.py`.
- If you're on linux (you should be if you care about privacy a bit), it'll also notify you on blocked subreddits using `libnotify`'s `notify-send`. It should be installed on most Distros or should come with most WMs, but try installing `libnotify` anyways.
- If you want to test non-nsfw subs: just run `python3 rct.py`
- If you want to test nsfw subs: change `"sublist"` on line 9 to `"nsfwsublist"` and run `python3 rct.py`.
- If you just want to see if it is running fine, comment out line 18 and uncomment line 17, and run `python3 rct.py`.

### Blocked subs

There are 6 blocked subreddits according to [The 2016 Reddit Transparency Report](https://www.reddit.com/wiki/transparency/2016):
> Turkey – We received 6 requests for the removal of one post and 6 subreddits which contained material that fell under the scope of “obscenity” in the Turkish Criminal Code which, in turn, constitutes grounds for a website to be blocked under the Turkish Internet Law. The post and subreddits were blocked from Turkish IPs. 

Non-NSFW scan is still going on, but we suspect that the other 3 is in this list.

From NSFW Sublist scan, the following subs seem to be blocked:
- /r/twinks
- /r/gayporn
- /r/gaypornhunters