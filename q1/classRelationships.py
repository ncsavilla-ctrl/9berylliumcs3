class DiskAlbum:
    def __init__(self, title, genre, artist, recordlabel, releaseyear):
        self.title = title
        self.genre = genre
        self.__artist = artist
        self.record_label = recordlabel
        self.release_year = releaseyear

    def displayTitle(self):
        print(f"Title: {self.title}")

    def displayGenre(self):
        print(f"Genre: {self.genre}")

    def displayArtist(self):
        print(f"Artist: {self.__artist}")

    def displayRecordLabel(self):
        print(f"Record Label: {self.record_label}")

    def displayReleaseYear(self):
        print(f"Release Year: {self.release_year}")



object1 = DiskAlbum("Buzz", "Indie-Pop", "NIKI", "88rising", 2024)
object2 = DiskAlbum("Eternal Sunshine", "R&B", "Ariana Grande", "Republic Records", 2024)
object3 = DiskAlbum("Capacities", "Synth-Pop", "Bob Johnson", "Terno Recordings", 2012)
object4 = DiskAlbum("You seem so sad for a girl so in love", "Pop, Indie-Pop", "Olivia Rodrigo", "Geffen Records", 2026)



object1.displayTitle()
object2.displayGenre()
object3.displayArtist()
object4.displayRecordLabel()
object4.displayReleaseYear()


albums = [object1, object2, object3, object4]



print("\nAll Titles:")
for item in albums:
    print(item.title)



print("\nAll Genres:")
for item in albums:
    print(item.genre)



print("\nAll Artists:")
for item in albums:
    print(item._DiskAlbum__artist)



print("\nAll Record Labels:")
for item in albums:
    print(item.record_label)


print("\nAll Release Years:")
for item in albums:
    print(item.release_year)
