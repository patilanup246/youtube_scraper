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

def id_finder(s):
    try:
        return s.split('{')[1].split('}')[0]
    except:
        return None

async def main():

    print() # just for style

    ch = 0
    ch_max = len(channels)
    videos = []

    vids_downloaded = 0
    vids_deleted = 0

    requests = [None for channel in channels]

    start = time.time()
    loop = asyncio.get_event_loop()

    for i, channel in enumerate(channels):

        requests[i] = loop.run_in_executor(None, req.get, channel['url'])

    for i in range(ch_max):
        request = await requests[i]
        feed = feedparser.parse(request.text).entries

        videos += [{'channel': re.sub('[|,.:;#\'"$%/?\\*~]', '', feed[i].authors[0].name),
                    'title': re.sub('[|,.:;#\'"$%/?\\*~]', '', feed[i].title),
                    'link': feed[i].link,
                    'vid_id': feed[i].yt_videoid,
                    'date': feed[i].published} for i in range(len(feed))]
        ch += 1
        progress = int(ch/ch_max*100)
        prog_bar = progress//2
        bar = '█'*(prog_bar) + ' '*(50-prog_bar)
        print(f"Scanning: {bar} {progress/100:.0%}\t",end='\r')

    videos = sorted(videos, key=itemgetter('date'))[-num_videos:]

    offline_videos = [video for video in os.listdir(destination) if video.endswith(".mp4")]

    try:
        deletion_file = open(f"{destination}/deleted_vids.txt", "r")
        for video in deletion_file.readlines():
            try:
                os.remove(f"{destination}/{video.rstrip()}")
                vids_deleted += 1
                print(f"Deleting {video}")
            except Exception as e:
                print(e)
        deletion_file.close()
    except:
        pass
    finally:
        deletion_file = open(f"{destination}/deleted_vids.txt", "w")

    for offline_vid in offline_videos:
        video_id = id_finder(offline_vid)
        is_in_list = False

        for i, list_vid in enumerate(videos):
            if video_id == list_vid['vid_id']:
                is_in_list = True
                videos.pop(i)
                break
        if not is_in_list:
            print(f"Deleted on next run: \"{offline_vid}\"\n")
            deletion_file.write(f"{offline_vid}\n")

    deletion_file.close()

    for vid in videos:
        try:
            yt = YouTube(f"https://youtube.com{vid['link']}").streams.filter(subtype='mp4').first()
        except:
            continue

        vids_downloaded += 1
        print(f"[{vids_downloaded:2}] Downloading: \"{vid['title']}\" by {vid['channel']}\n")

        download_start = time.time()
        yt.download(destination)
        video_file = File(f"{destination}/{vid['title']}.mp4")
        video_file.rename(f"[{vid['channel']}] {vid['title']} {{{vid['vid_id']}}}.mp4")
        download_end = time.time()

        print(f"Download finished in {download_end-download_start:0.0f} seconds\n")

    end = time.time()
    print(f"Elapsed time: {end-start:.0f} seconds. {vids_downloaded} videos downloaded and {vids_deleted} videos deleted")

if __name__ == '__main__':
   loop = asyncio.get_event_loop()
   loop.run_until_complete(main())
