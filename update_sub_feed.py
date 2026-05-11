import argparse
import datetime
from time import sleep

import yt_dlp

parser = argparse.ArgumentParser(description='')
parser.add_argument('count', help='how many videos')
args = parser.parse_args()



ydl_opts = {
    'extract_flat': True,
    'quiet': True,
    'playlistend': int(args.count),
}


print(f'sub feed updated ({str(datetime.datetime.now())})')
print(f'count: {args.count}')
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    with open('subs.txt', 'r') as f:
        for line in f:
            channel_id = line.strip().split(':::')[1]
            res = ydl.extract_info(f'https://www.youtube.com/channel/{channel_id}/videos', download=False)
            for idx, entry in enumerate(res['entries']):
                print(f'{idx}.')
                print(f'full response {str(entry)}')
                print('********')
                sleep(3)
