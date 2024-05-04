# Test Driver Program

# import TV class
from TV import TV

# Create two TV instances
tv1 = TV()
tv2 = TV()

# Turn on the TVs
tv1.turnOn()
tv2.turnOn()

# Set channels and volumes
tv1.setChannel(3)
tv2.setChannel(11)
tv1.setVolume(6)
tv2.setVolume(5)

# Increase the channel and volume
tv1.channelUp()
tv2.channelUp()
tv1.volumeUp()
tv2.volumeUp()

# Print the results
print(f"tv1's channel is {tv1.getChannel()} and volume level is {tv1.getVolume()}")
print(f"tv2's channel is {tv2.getChannel()} and volume level is {tv2.getVolume()}")

# Decrease the channel and volume
tv1.channelDown()
tv1.volumeDown()
tv2.channelDown()
tv2.volumeDown()

# Print the results
print(f"\ntv1's channel is {tv1.getChannel()} and volume level is {tv1.getVolume()}")
print(f"tv2's channel is {tv2.getChannel()} and volume level is {tv2.getVolume()}")

# Set new channels and volumes
tv1.setChannel(2)
tv2.setChannel(69)
tv1.setVolume(3)
tv2.setVolume(2)

# Print the results
print(f"\ntv1's channel is {tv1.getChannel()} and volume level is {tv1.getVolume()}")
print(f"tv2's channel is {tv2.getChannel()} and volume level is {tv2.getVolume()}")

# Increase the channel and volume
tv1.channelUp()
tv1.volumeUp()
tv2.channelUp()
tv2.volumeUp()

# Print the results
print(f"\ntv1's channel is {tv1.getChannel()} and volume level is {tv1.getVolume()}")
print(f"tv2's channel is {tv2.getChannel()} and volume level is {tv2.getVolume()}")

# Turn off the TVs
tv1.turnOff()
tv2.turnOff()