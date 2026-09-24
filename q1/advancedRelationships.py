class AudioTrack:
    def __init__(self, title: str, duration: int, id: str):
        self.id = id
        self.title = title
        self.duration = duration

    def display_info(self):
        mins = self.duration // 60
        secs = self.duration % 60
        return f"ID: {self.id} | Title: {self.title} | Duration: {mins}:{secs:02d}"


class Song(AudioTrack):
    def __init__(
        self,
        id: str,
        title: str,
        duration: int,
        lyrics: str,
        bpm: int
    ):
        super().__init__(title, duration, id)
        self.lyrics = lyrics
        self.bpm = bpm

    def get_song_details(self):
        return (
            f"{self.display_info()} | BPM: {self.bpm}\n"
            f"Lyrics Snippet: '{self.lyrics[:30]}...'"
        )


class AudioHeader:
    def __init__(self, sample_rate: int, bit_depth: int):
        self.sample_rate = sample_rate
        self.bit_depth = bit_depth

    def get_specs(self):
        return f"{self.sample_rate} Hz, {self.bit_depth}-bit"


class DigitalAlbum:
    def __init__(
        self,
        album_id: str,
        album_title: str,
        featured_song: Song,
        sample_rate: int,
        bit_depth: int
    ):
        self.album_id = album_id
        self.album_title = album_title
        self.featured_song = featured_song
        self.audio_header = AudioHeader(sample_rate, bit_depth)

    def get_album_summary(self):
        return (
            f"Album: {self.album_title} (ID: {self.album_id})\n"
            f"Audio Quality: {self.audio_header.get_specs()}\n"
            f"Featured Song Details:\n"
            f"{self.featured_song.get_song_details()}"
        )
    
