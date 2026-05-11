import argparse
import yt_dlp

parser = argparse.ArgumentParser(description='')
parser.add_argument('query', help='search query')
parser.add_argument('count', help='how many videos')
args = parser.parse_args()

ydl_opts = {
    # 'extract_flat': True,
    'quiet': True,
}
print(f'search for {args.query}')
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    res = ydl.extract_info(f'ytsearch30:{args.query}', download=False)
    for idx, entry in enumerate(res['entries']):
        print(f'{idx}.')
        print(f'title: {entry["title"]}')
        print(f'channel: {entry['channel']}')
        print(f'description: {entry["description"]}')
        print(f'duration: {entry["duration"]}')
        print(f'full response {str(entry)}')
        print('********')

