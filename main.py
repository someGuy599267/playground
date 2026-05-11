import argparse

import yt_dlp
import sys

parser = argparse.ArgumentParser(description='')
parser.add_argument('arg1', help='search query')
args = parser.parse_args()



ydl_opts = {
    'extract_flat': True,
    'quiet': True,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    res = ydl.extract_info(f'ytsearch20:{args}', download=False)
    for idx ,entry in enumerate(res['entries']):
        print(f'{idx}.')
        print(f'title: {entry["title"]}')
        print(f'channel: {entry['channel']}')
        print(f'description: {entry["description"]}')
        print(f'duration: {entry["duration"]}')
        print(f'full response {str(entry)}')
        print('********')
