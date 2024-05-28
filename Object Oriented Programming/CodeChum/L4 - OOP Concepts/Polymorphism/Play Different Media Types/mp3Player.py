from mediaPlayer import MediaPlayer

class MP3Player(MediaPlayer):
    def play_audio(self):
        print("MP3Player playing audio.")

    def play_video(self):
        print("MP3Player cannot play video.")