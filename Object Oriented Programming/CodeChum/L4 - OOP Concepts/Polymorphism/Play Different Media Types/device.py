from mp4Player import MP4Player
from mp3Player import MP3Player

class Device:
    def __init__(self, media_player):
        self.media_player = media_player

    def play_audio(self):
        self.media_player.play_audio()

    def play_video(self):
        self.media_player.play_video()