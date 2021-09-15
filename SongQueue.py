class Entry:
    path = ""
    url = ""
    requester = ""
    def __init__(self, path, url, requester):
        self.path = path
        self.url = url
        self.requester = requester


class SongQueue:
    songs = []
    def __init__(self, path, url, requester):
        entry = Entry(path, url, requester)
        self.songs += [entry]

    def queue(self, path, url, requester):
        entry = Entry(path, url, requester)
        self.songs += [entry]

    def skip(self):
        self.songs = self.songs[1:]

    def clear(self):
        self.songs = []
