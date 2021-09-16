import youtube_dl
import os

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
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': song_path
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        filename = replace_shit(ydl.prepare_filename(info_dict)) #get it to be mp3, yes it's painting over a deeper problem.
        song_downloaded = os.path.isfile(song_path)
        if not song_downloaded:
            ydl.download([url])
        return filename