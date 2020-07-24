# Conference call audio downloader for indian equities 
# Powered by the Youtube channel : Trendlyne
# Uses: git@github.com:jansenicus/vtt-to-srt.py.git
import os

import youtube_dl
from vtt_to_srt import vtts_to_srt

from dotenv import load_dotenv
load_dotenv()
DOWNLOAD_DIRECTORY =os.environ['DOWNLOAD_DIRECTORY_WIN'] 

playlists = [
    'https://www.youtube.com/playlist?list=PLE25ZovyAdMdOFj-eclPLvdeUvgkQZqhQ', # Q320
    'https://www.youtube.com/playlist?list=PLE25ZovyAdMeFDAIYJcCgECylMfJzORiI', # Q420
    'https://www.youtube.com/playlist?list=PLE25ZovyAdMexlZ3-aBidggbYO1J1kHb-'  #Q121
]


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        try:
            print(f'{d["filename"]} ({d["downloaded_bytes"]}) Done!')
        except:
            print(f'{d["filename"].split(os.path.sep)[-1]} already downloaded!')
    elif d['status'] == 'downloading':
        print(f'ETA: {d["eta"]} sec, {round(d["speed"]/1000,2)}kb/s    ', end="\r")
    
def download_video(url):
    '''
    Download m4a audio , write thumbnails and extract subtitles
    '''
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]',
        # 'postprocessors': [{
        #     'key': 'FFmpegExtractAudio',
        #     'preferredcodec': 'mp3',
        #     'preferredquality': '192',
        # }],
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
        'outtmpl': f'{DOWNLOAD_DIRECTORY}/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s',
        'ignoreerrors':True,
        'continuedl': True,
        'writethumbnail': True,
        'writeautomaticsub': True,
        'writeinfojson': True,
        # 'allsubtitles': True,
        'subtitleslang': ['en']
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__=='__main__':
    for playlist in playlists[1:2]:
        download_video(playlist)
    vtts_to_srt(DOWNLOAD_DIRECTORY, rec=True) # Recursive True
