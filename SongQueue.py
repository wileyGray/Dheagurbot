class Entry:
    def __init__(self, path, url, requester, runtime):
        self.path = path
        self.url = url
        self.requester = requester
        self.runtime = runtime

    def get_runtime(self):
        return self.runtime

    def set_runtime(self, subtracted):
        self.runtime -= subtracted

class SongQueue:

    def __init__(self):
        self.songs = []
        self.paused = False

    def peek(self):
        return self.songs[0]

    def pop_song(self):
        if len(self.songs) == 1:
            entry = self.songs[0]
            self.clear()
            return entry
        return self.songs.pop(0)

    def enqueue(self, entry):
        self.songs.append(entry)

    def clear(self):
        self.songs = []
        self.paused = False

    def isEmpty(self):
        print(len(self.songs))
        return len(self.songs) == 0

    def has_one_song(self):
        return len(self.songs) == 1

    def remove_from_queue(self, entry): #kinda useless and will probably never be used
        if self.contains(entry):
            self.songs.remove(entry)
        else:
            raise UserWarning("the entry requested doesnt exist: " + str(entry))

    def contains(self, entry):
        return self.songs.__contains__(entry)

    def pause(self):
        self.paused = True

    def unpause(self):
        self.paused = False

    def is_paused(self):
        return self.paused

