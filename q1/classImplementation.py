class MusicGenre:
    def __init__(self, title, genre, artist, streams):
        self.title = title
        self.genre = genre
        self.__artist = artist
        self._streams = streams

    def displayInfo(self):
        print(f"Title: {self.title}, Genre: {self.genre}, "
              f"Artist: {self.__artist}, Streams: {self._streams:,}")

    def updateStreams(self, amount):
        self._streams += amount
        print(f"Updated streams for {self.title}: {self._streams:,}")

    def displayGenre(self, selected_song):
        print(f"Genre of {selected_song.title}: {selected_song.genre}")

    def displayTitle(self, selected_song):
        print(f"Title of the song: {selected_song.title}")


object1 = MusicGenre("La La Lost You", "indie pop", "NIKI", 585000000)
object2 = MusicGenre("Mahika", "OPM", "Adie", 446000000)
object3 = MusicGenre("Fortnight", "synth-pop", "Taylor Swift", 1239082552)

print("--- BEFORE ---")

print("Object 1: displayInfo")
object1.displayInfo()

print("Object 2: displayTitle")
object2.displayTitle(object2)

print("Object 3: updateStreams")
object3.updateStreams(1000000)

print("\nChanging streams of object 1...")
object1.updateStreams(1000000)

print("\n--- AFTER ---")

print("Object 1: displayInfo")
object1.displayInfo()

print("Object 2: displayTitle")
object2.displayTitle(object2)

print("Object 3: updateStreams")
object3.updateStreams(1000000)
