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
  def __init__(self, id: str, title: str, duration: int, lyrics: str, bpm: int):
    super().__init__(id, title, duration)
    self.lyrics = lyrics
    self.bpm = bpm
    self.duration = duration
    self.title = title

  def get_song_details(self):
    return f"{self.display_info()} | BPM: {self.bpm}\nLyrics Snippet: 'self.lyrics[:30]}...'"
    
