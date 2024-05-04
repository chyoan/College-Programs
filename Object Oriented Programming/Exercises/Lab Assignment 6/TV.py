# Exercise: 
# Given: A UML Class Diagram below:
# Required: Create a Python Code for creating the Class named TV and a Test Driver program named TestTV that will create two objects from Class TV and will produce the following output:
# tv1's channel is 30 and volume level is 3
# tv2's channel is 3 and volume level is 2

# TV
# channel: int                                 # The current channel (1-120) of this TV.
# volumeLevel: int                             # The current volume (1-7) of this TV.                         
# on: boolean                                  # Indicates whether this TV is on/off.

# TV()                                         # Constructs a default TV object.
# turnOn(): None                               # Turns on this TV.
# turnOff(): None                              # Turns off this TV.
# getChannel(): int                            # Returns the channel for this TV.
# setChannel(newChannel: int): None            # Sets a new channel for this TV.
# getVolume(): int                             # Gets the volume level for this TV.
# setVolume(newVolumeLevel: int): None         # Sets a new volume level for this TV.
# channelUp(): None                            # Increases the channel number by 1.
# channelDown(): None                          # Decreases the channel number by 1.
# volumeUp(): None                             # Increases the volume level by 1.
# volumeDown(): None                           # Decreases the volume level by 1.

# Constructs a default TV object.
class TV:
    def __init__(self):
        self.channel: int = 1
        self.volumeLevel: int = 1
        self.on: bool = False

    # Turns on this TV.
    def turnOn(self) -> None:
        self.on = True

    # Turns off this TV.
    def turnOff(self) -> None:
        self.on = False
    
    # Returns the channel for this TV.
    def getChannel(self) -> int:
        return self.channel

    # Sets a new channel for this TV.
    def setChannel(self, channel: int) -> None:
        if self.on and 1 <= channel <= 120:
            self.channel = channel

    # Gets the volume level for this TV.
    def getVolume(self) -> int:
        return self.volumeLevel
    
    # Sets a new volume level for this TV.
    def setVolume(self, volumeLevel: int) -> None:
        if self.on and 1 <= volumeLevel <= 7:
            self.volumeLevel = volumeLevel

    # Increases the channel number by 1.
    def channelUp(self) -> None:
        if self.on and self.channel < 120:
            self.channel += 1

    # Decreases the channel number by 1.
    def channelDown(self) -> None:
        if self.on and self.channel > 1:
            self.channel -= 1

    # Increases the volume level by 1.
    def volumeUp(self) -> None:
        if self.on and self.volumeLevel < 7:
            self.volumeLevel += 1

    # Decreases the volume level by 1.
    def volumeDown(self) -> None:
        if self.on and self.volumeLevel > 1:
            self.volumeLevel -= 1