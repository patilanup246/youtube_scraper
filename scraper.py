import asyncio
import feedparser
import os
import re
import requests as req
import time
from files import File
from operator import itemgetter
from pytube import YouTube
from subscriptions import destination, num_videos, channels

async def main():

    start = time.time()
    loop = asyncio.get_event_loop()

    ch = 0
    ch_max = len(channels)
    videos = []

    vids_downloaded = 0
    vids_deleted = 0

    requests = [None for channel in channels]

    for i, channel in enumerate(channels):

        requests[i] = loop.run_in_executor(None, req.get, channel['url'])

    for i in range(ch_max):
        request = await requests[i]
        feed = feedparser.parse(request.text).entries

        videos += [{'channel': re.sub('[|,.:;#\'"$%/?\\*~]', '', feed[i].authors[0].name),
                    'title': re.sub('[|,.:;#\'"$%/?\\*~]', '', feed[i].title),
                    'link': feed[i].link,
                    'date': feed[i].published} for i in range(len(feed))]
        ch += 1
        progress = int(ch/ch_max*100)
        bar = '█'*(progress//5) + ' '*(20-progress//5)
        print(f"Scanning: {bar} {progress/100:.0%}",end='\r')

    videos = sorted(videos, key=itemgetter('date'))[-num_videos:]

    offline_videos = [video for video in os.listdir(destination) if os.path.isfile(f"{destination}\\{video}")]

    for offline_vid in offline_videos:
        vid, ext = os.path.splitext(offline_vid)
        is_in_list = False

        for list_vid in videos:
            if vid == f"[{list_vid['channel']}] " + list_vid['title']:
                is_in_list = True
                break
        if not is_in_list:
            vids_deleted += 1
            print(f"Deleting: \"{vid}{ext}\"\n")
            os.remove(f"{destination}\\{vid}{ext}")

    for vid in videos:
        if not os.path.isfile(f"{destination}/[{vid['channel']}] {vid['title']}.mp4"):
            try:
                yt = YouTube(f"https://youtube.com{vid['link']}").streams.filter(subtype='mp4').first()
            except:
                continue

            vids_downloaded += 1
            print(f"[{vids_downloaded:2}] Downloading: \"{vid['title']}\" by {vid['channel']} ({round(yt.filesize/(2**20),1)} MB)\n")

            download_start = time.time()
            yt.download(destination)
            video_file = File(f"{destination}\\{vid['title']}.mp4")
            video_file.rename(f"[{vid['channel']}] {vid['title']}.mp4")
            download_end = time.time()

            print(f"Download finished in {download_end-download_start:0.0f} seconds\n")

    end = time.time()
    print(f"Elapsed time: {end-start:.0f} seconds. {vids_downloaded} videos downloaded and {vids_deleted} videos deleted")

if __name__ == '__main__':
   loop = asyncio.get_event_loop()
   loop.run_until_complete(main())
