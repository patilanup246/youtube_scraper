import asyncio
import feedparser
import os
import re
import requests as req
import sqlite3
import sys
import time

from files import File
from operator import itemgetter
from pytube import YouTube
from subscriptions import destination, num_videos, channels, delta

execution_path = sys.path[0]
connection = sqlite3.connect(f"{execution_path}/Videos.db")
cursor = connection.cursor()

current_time = time.time()
deletion_time = current_time + delta

ch = 0
ch_max = len(channels)
videos = []

vids_downloaded = 0
vids_deleted = 0

print() # just for style

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS videos (name TEXT, date REAL, id TEXT)")

def close_connection():
    connection.close()

def video_entry(name, date, vid_id):
    cursor.execute("INSERT INTO videos (name, date, id) VALUES (?, ?, ?)", (name, date, vid_id))
    connection.commit()

def delete_old_videos():
    cursor.execute(f"SELECT * FROM videos WHERE date < {current_time}")
    for row in cursor.fetchall():
        print(f"Deleting {row[0]}")
        try:
            os.remove(f"{destination}/{row[0]}")
        except Exception as e:
            print(e)
    cursor.execute(f"DELETE FROM videos WHERE date < {current_time}")
    connection.commit()

def already_downloaded():
    global videos
    cursor.execute("SELECT * FROM videos")
    data = cursor.fetchall()
    for row in data:
        videos = [vid for vid in videos if not vid.get('vid_id') == row[2]]

def download_vid(vid):
    global vids_downloaded
    try:
        yt = YouTube(f"https://youtube.com{vid['link']}").streams.filter(subtype='mp4').first()
    except Exception as e:
        print(e)
        return False

    vids_downloaded += 1
    print(f"[{vids_downloaded:2}] Downloading: \"{vid['title']}\" by {vid['channel']}\n")

    download_start = time.time()
    yt.download(destination)
    video_file = File(f"{destination}/{vid['title']}.mp4")
    video_file.rename(f"[{vid['channel']}] {vid['title']}.mp4")
    download_end = time.time()

    print(f"Download finished in {download_end-download_start:0.0f} seconds\n")
    return True

async def main():

    global ch, ch_max, videos, vids_deleted, vids_downloaded

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
    print(""*100,end='\r')

    videos = sorted(videos, key=itemgetter('date'))[-num_videos:]

    offline_videos = [video for video in os.listdir(destination) if video.endswith(".mp4")]

    delete_old_videos()

    already_downloaded()

    for vid in videos:

        if download_vid(vid):
            video_entry(f"[{vid['channel']}] {vid['title']}.mp4", deletion_time, vid['vid_id'])

    end = time.time()
    print(f"Elapsed time: {end-start:.0f} seconds. {vids_downloaded} videos downloaded and {vids_deleted} videos deleted")
    close_connection()

if __name__ == '__main__':
   loop = asyncio.get_event_loop()
   loop.run_until_complete(main())
