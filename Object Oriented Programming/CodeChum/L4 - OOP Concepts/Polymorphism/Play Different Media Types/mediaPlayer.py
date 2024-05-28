# Play Different Media Types - Python
# by CodeChum Admin
# 
# Create a program where different types of media players demonstrate polymorphism.
# 
# Class - MediaPlayer:
# Methods:
# def play_audio(self) -> None: An abstract method representing audio playback. It doesn't have a specific implementation in the base class MediaPlayer.
# def play_video(self) -> None: An abstract method representing video playback. It doesn't have a specific implementation in the base class MediaPlayer.
#  
# Class - MP3Player (extends MediaPlayer):
# Methods:
# def play_audio(self) -> None: Overrides the play_audio method from the base class MediaPlayer. It prints "MP3Player playing audio."
# def play_video(self) -> None: Overrides the play_video method from the base class MediaPlayer. It prints "MP3Player cannot play video."
#  
# Class - MP4Player (extends MediaPlayer):
# Methods:
# def play_audio(self) -> None: Overrides the play_audio method from the base class MediaPlayer. It prints "MP4Player playing audio."
# def play_video(self) -> None: Overrides the play_video method from the base class MediaPlayer. It prints "MP4Player playing video."
#  
# Class - Device:
# Methods:
# def __init__(self, media_player: MediaPlayer) -> None: Initializes the Device object with a media_player parameter, which should be an instance of a MediaPlayer or its subclasses.
# def play_audio(self) -> None: Calls the play_audio method on the media_player object provided during initialization.
# def play_video(self) -> None: Calls the play_video method on the media_player object provided during initialization.

class MediaPlayer:
    def play_audio(self):
        pass

    def play_video(self):
        pass