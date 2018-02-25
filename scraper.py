import time
import requests
from bs4 import BeautifulSoup
from subscriptions import channels

videos = []

start = time.time()

for channel in channels:
	channel_name = channel["channel"]
	channel_id = channel["id"]

	r = requests.get("https://www.youtube.com/channel/{}/videos".format(channel_id))

	soup = BeautifulSoup(r.text, 'html.parser')

	title = soup.select('h3.yt-lockup-title')
	meta = soup.select('div.yt-lockup-meta')
	thumbnail_span = soup.select('span.yt-thumb-clip')[6:]

	# Title, link, duration
	video_attr = [[vid.a.attrs['title'],vid.a.attrs['href'],vid.span.string[10:]] for vid in title]

	# views, age
	description = [[m.ul.li.string, m.ul.li.next_sibling.string[4:]] for m in meta]

	# complete link to thumbnail
	thumbnails = [thumb.img.attrs['src'] for thumb in thumbnail_span]

	videos += [{"channel": channel_name,
				"title": video_attr[i][0],
				"link": video_attr[i][1],
				"duration": video_attr[i][2],
				"views": description[i][0],
				"age": description[i][1],
				"thumbnail": thumbnails[i]} for i in range(len(video_attr))] # number of videos per channel


end = time.time()
			
for i in range(len(videos)):
	print("{}. Video: {}\n".format(i+1, videos[i]))
	
print("Elapsed time: {} seconds".format(end-start))

