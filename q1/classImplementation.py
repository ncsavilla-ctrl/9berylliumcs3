class MusicGenre:
    def __init__(self, title, genre, artist, streams):
        self.title = title
        self.genre = genre
        self.__artist = artist
        self._streams = streams

    def displayInfo(self, selected_artist):
        if self.__artist == selected_artist:
        print(f"Title: {self.title}, Genre: {self.genre}, Artist: {self.__artist}, Streams: {self._streams}")

    def updateStreams(self, amount):
        self._streams += amount
        print(f"Updated streams for {self.title}: {self._streams}")

    def displayGenre(self, selected_song):
        print(f"Genre of {selected_song.title}: {selected_song.genre}")

    def displayTitle(self, selected_song):
        print(f"Title of the song: {selected_song.title}")

object1 = MusicGenre("La La Lost You", "indie pop", "NIKI", "585,000,000")
object2 = MusicGenre("Mahika", "OPM", "Adie", "446,000,000")
object3 = MusicGenre("Fortnight", "synth-pop", "Taylor Swift", "1,239,082,552")

object1.displayInfo(object1.MusicGenre)
object2.displayInfo(object2.MusicGenre)
object3.displayInfo(object3.MusicGenre)

print("--- BEFORE ---")
print("Object 1: displayInfo")
print("Object 2: displayInfo")
print("Object 3: displayInfo")

print("Changing streams of object 1...")
print("--- AFTER ---")
print("Object 1: displayInfo")
print("Object 2: DisplayInfo")
print("Object 3: DisplayInfo")
