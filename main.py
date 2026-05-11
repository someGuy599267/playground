import yt_dlp
from yt_dlp import YoutubeDL

ydl_opts = {
    'extract_flat': True,
    'quiet': True,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    res = ydl.extract_info('ytsearch5:tjthings', download=False)
    for entry in res['entries']:
        print(str(entry))