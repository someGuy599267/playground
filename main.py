import yt_dlp
from yt_dlp import YoutubeDL

ydl_opts = {
    'extract_flat': True,
    'quiet': True,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    res = ydl.extract_info('ytsearch5:rickroll', download=False)
    if 'entries' in res:
        for video in res['entries']:
            print(video['title'])
            print(video['description'])
            print(video['url'])
            print(video['duration'])
            print(video.keys())