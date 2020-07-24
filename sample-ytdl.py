import youtube_dl
# git@github.com:jansenicus/vtt-to-srt.py.git

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
        'outtmpl': '~/ytvideos/%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s',
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
    download_video('https://www.youtube.com/playlist?list=PLE25ZovyAdMdOFj-eclPLvdeUvgkQZqhQ')
    #Q121
