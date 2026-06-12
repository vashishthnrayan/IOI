class Playlist:
    def __init__(self,name,genre,song_num):
        self.name = name
        self.genre = genre
        self.song_num = song_num
        self.song = []

        print(f"Playlist '{self.name}' of genre '{self.genre}' with {self.song_num} songs created successfully and song are {song}")

    def __del__(self):
        print(f"Playlist '{self.name}' deleted successfully.")
        print(f"Playlist '{self.name}' had {self.song_num} songs.")

ch1 = Playlist("Chill Vibes", "Lo-fi", 20,1)
del ch1
work_Hit = Playlist("Workout Hits", "Pop", 30,4)
del work_Hit