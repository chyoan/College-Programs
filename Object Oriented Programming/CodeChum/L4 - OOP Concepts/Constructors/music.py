# Playlist - Python
# by CodeChum Admin

# Create a class called Music having the following details:
# Class - Music:
# Public Properties:
# duration (type: int): Represents the duration of the music track in minutes.
# genre (type: str): Specifies the genre of the music.
# Constructor:
# __init__(self, duration: int = 0, genre: str = "Unknown", duration_type: str = "m"):
# This constructor can be used in two ways:
# When called with no parameters, it initializes duration to 0 and genre to "Unknown". This provides a standard default state for the Music object when no specific details are given.
# When called with parameters, it sets the duration and genre properties based on the provided values. Additionally, it accepts a duration_type string to indicate whether the duration is in minutes ('m'), hours ('h'), or days ('d'). If duration_type is 'm' or not provided, the duration is assumed to be in minutes. If duration_type is 'h', it converts hours to minutes, and if duration_type is 'd', it converts days to minutes before setting the duration property.

class Music:
    def __init__(self, duration: int = 0, genre: str = "Unknown", duration_type: str = "m"):
        self.duration = duration
        self.genre = genre
        self.duration_type = duration_type
        if self.duration_type == 'm' or self.duration_type == '':
            self.duration = duration
        elif self.duration_type == 'h':
            self.duration = duration * 60
        elif self.duration_type == 'd':
            self.duration = duration * 1440