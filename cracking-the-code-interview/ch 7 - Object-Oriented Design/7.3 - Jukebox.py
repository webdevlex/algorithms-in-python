class Jukebox:
    def __init__(self, cdPlayer, user, cdCollection):
        self.cdPlayer = cdPlayer
        self.user = user
        self.cdCollection

    def setUser(self, user):
        self.user = user


class CDPlayer:
    def __init__(self, cd, playlist):
        self.cd = cd
        self.playlist = playlist

    def playSong(song):
        # ...
        return

    def getPlaylist(self):
        return self.playlist

    def setPlaylist(self, playlist):
        self.playlist = playlist

    def getCD(self):
        return self.cd

    def setCD(self, cd):
        self.cd = cd

class Playlist:
    def __init__(self, song, queue):
        self.song = song
        self.queue = queue

    def getNextSongToPlay(self):
        return self.queue[0]
    
    def queueUpSong(self, song):
        self.queue.push(song)

class CD:
    def __init__(self, artist, album, songs):
        self.artist = artist
        self.album = album
        self.songs = songs

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def setName(self, name);
        self.name = name
    
    def getName(self):
        return self.name
    
    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id
    