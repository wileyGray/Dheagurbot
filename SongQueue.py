class Entry:
    def __init__(self, path, url, requester):
        self.path = path
        self.url = url
        self.requester = requester


class SongQueue:

    def __init__(self):
        self.songs = []

    def peek(self):
        return self.songs[0]

    def pop_song(self):
        if len(self.songs) == 1:
            self.clear()
            return
        self.songs = self.songs.pop(0)

    def enqueue(self, path, url, requester):
        entry = Entry(path, url, requester)
        self.songs.append(entry)

    def clear(self):
        self.songs = []

    def isEmpty(self):
        print(len(self.songs))
        return len(self.songs) == 0

    def has_one_song(self):
        return len(self.songs) == 1

    def remove_from_queue(self, path, url, requester): #kinda useless and will probably never be used
        dequeuedEntry = Entry(path, url, requester)
        if self.contains(path, url, requester):
            self.songs.remove(Entry(path, url, requester))
        else:
            raise UserWarning("the entry requested doesnt exist: " + str(dequeuedEntry))

    def contains(self, path, url, requester):
        containedEntry = Entry(path, url, requester)
        return self.songs.__contains__(containedEntry)

