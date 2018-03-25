import os
import time
import re
import requests
from bs4 import BeautifulSoup
from pytube import YouTube
from operator import itemgetter

from subscriptions import channels

# needs to be modified for other languages
dates = {	"Sekunde": 1, "Sekunden": 1, "Minute": 60, "Minuten": 60, "Stunde": 3600, 
			"Stunden": 3600, "Tag": 86400, "Tagen": 86400, "Woche": 604800, "Wochen": 604800, 
			"Monat": 2592000, "Monaten": 2592000, "Jahr": 31104000, "Jahren": 31104000}

destination = "C:\\Users\\aaron\\Videos\\YouTube"

videos = []

start = time.time()

for channel in channels:
	channel_name = channel['channel']
	channel_id = channel['id']

	r = requests.get("https://www.youtube.com/channel/{}/videos".format(channel_id))

	soup = BeautifulSoup(r.text, 'html.parser')

	title = soup.select('h3.yt-lockup-title')
	meta = soup.select('div.yt-lockup-meta')

	# Title, (relative) link; location of strip needs to be modified for other languages
	video_attr = [[vid.a.attrs['title'],vid.a.attrs['href']] for vid in title]

	# Age; location of strip needs to be modified for other languages
	description = [m.ul.li.next_sibling.string[4:] for m in meta]
	
	age = [0 for i in range(len(description))]
	for i in range(len(description)):
		number, period = description[i].split()
		age[i] = int(number) * dates[period]

	videos += [{"channel": channel_name,
				"title": re.sub('[|,.:;#\'"$%/?\\*~]', '', video_attr[i][0]),
				"link": video_attr[i][1],
				"age": age[i]} for i in range(len(video_attr))]
				

sorted_videos = sorted(videos, key=itemgetter('age'))[:80]
sorted_videos = sorted_videos[::-1]

# delete videos that aren't in the list anymore
offline_videos = [video for video in os.listdir(destination) if os.path.isfile("{}\\{}".format(destination,video))]
vids_deleted = 0

for i in range(len(offline_videos)):
	vid, ext = os.path.splitext(offline_videos[i])
	is_in_list = False
	
	for list_vid in sorted_videos:
		if vid == list_vid['title']:
			is_in_list = True
			break
	if not is_in_list:
		vids_deleted += 1
		print("Deleting: \"{}{}\"\n".format(vid,ext))
		os.remove("{}\\{}{}".format(destination,vid,ext))		

vids_downloaded = 0
for vid in sorted_videos:
	if not os.path.isfile("{}/{}.mp4".format(destination,vid['title'])):
		try: # check if video is livestream
			yt = YouTube("https://youtube.com{}".format(vid['link']))
		except:
			continue
		vids_downloaded += 1
		print("[{:2}] Downloading: \"{}\" by {}\n".format(vids_downloaded, vid['title'], vid['channel']))
		download_start = time.time()
		yt.streams.filter(subtype='mp4').first().download(destination)
		download_end = time.time()
		print("Download finished in {:0.0f} seconds\n".format(download_end-download_start))
		
end = time.time()		
print("Elapsed time: {:0.0f} seconds. {} videos downloaded and {} videos deleted".format(end-start, vids_downloaded, vids_deleted))

