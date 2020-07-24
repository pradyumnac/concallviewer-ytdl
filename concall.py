# Conference call audio downloader for indian equities 
# Powered by the Youtube channel : Trendlyne
# Uses: git@github.com:jansenicus/vtt-to-srt.py.git
import youtube_dl
from vtt_to_srt import vtts_to_srt

DOWNLOAD_DIRECTORY ='/home/pi/ytvideos/trendlyne' 


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done!')
        print(d.keys())
    # print(f'Status : {d["status"]}')

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
        # 'allsubtitles': True,
        'subtitleslang': ['en']
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__=='__main__':
    # download_video('https://www.youtube.com/playlist?list=PLE25ZovyAdMdOFj-eclPLvdeUvgkQZqhQ')
    # Q320
    # download_video('https://www.youtube.com/playlist?list=PLE25ZovyAdMdOFj-eclPLvdeUvgkQZqhQ')
    #Q420
    # download_video('https://www.youtube.com/playlist?list=PLE25ZovyAdMdOFj-eclPLvdeUvgkQZqhQ')
    #Q121
    vtts_to_srt(DOWNLOAD_DIRECTORY, rec=True) # Recursive True
