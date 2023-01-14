class Music:
    def __init__(self,performer,song,album,year):
        self.performer = performer
        self.song = song
        self.album = album
        self.year = year
    def __str__(self):
        print(f"{self.performer},{self.song},{self.album},{self.year}")
ed = Music(1,2,3,4)
ed.__str__()