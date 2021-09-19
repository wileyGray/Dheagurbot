import youtube_dl
import os
from youtubesearchpython import VideosSearch

#helpful links:
#   youtubesearchpython: https://pypi.org/project/youtube-search-python/
#   https://manpages.ubuntu.com/manpages/xenial/man1/youtube-dl.1.html
#   https://github.com/ytdl-org/youtube-dl/issues/4309 - Example: bot searches for "bangTrippieRedd" the url it finds is a playlist, not a video, so the no_playlist option doesn't work given there is no video id in the url"


def replace_shit(path : str):
    length = len(path)
    for char_index in range(length):
        if path[char_index] == '.':
            index = char_index
    return path[:index] + ".mp3"

def download_song(url : str):

    print("downloading " + url)

    song_path = 'songs/%(title)s.%(ext)s'

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': song_path,
        'default_search': 'ytsearch',
        'no_playlist': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],

    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        filename = replace_shit(ydl.prepare_filename(info_dict)) #get it to be mp3, yes it's painting over a deeper problem.
        song_downloaded = os.path.isfile(filename)
        print("DEBUG: before download song path is: " + filename)
        if not song_downloaded:
            ydl.download([url])
            print("DEBUG: after download song path is: " + filename)
        else:
            print("file found, skipped download for " + filename)
        return filename