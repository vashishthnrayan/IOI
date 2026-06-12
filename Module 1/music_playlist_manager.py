class Playlist:
    def __init__(self,name,genre):
        self.name = name
        self.genre = genre
        self.song = []

        print(f"Playlist '{self.name}' of genre '{self.genre}' created successfully.")
    def add_song(self,song):
        self.song.append(song)
        print(f"Song '{song}' added to playlist '{self.name}' successfully.")


    def remove_song(self,song):
        if song in self.song:
            self.song.remove(song)
            print(f"Song '{song}' removed from playlist '{self.name}' successfully.")
        else:
            print(f"Song '{song}' not found in playlist '{self.name}'.")

    def display_songs(self):
        print(f"\n--- {self.name} ({self.genre}) ---")
        if self.song:
           for i ,song in enumerate(self.song,1):
               print(f"{i}. {song}")
        else:
            print("No songs in the playlist.")
    def __del__(self):
        print(f"Playlist '{self.name}' deleted successfully.")

my_playlist = Playlist("Chill Vibes", "Lo-fi")

while True:

    print("\n1. Add Song 2. Remove Song 3. View Playlist 4. Delete Playlist 5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        song= input("Enter the song name to add: ")
        my_playlist.add_song(song)
    elif choice == '2':
        song = input("Enter the song name to remove: ")
        my_playlist.remove_song(song)
    elif choice == '3':
        my_playlist.display_songs()
    elif choice == '4':
        del my_playlist
        break
    elif choice == '5':
        print("Exiting the program.....")
        break
    
    else:
        print("\nInvalid choice. Please try again.")
        
