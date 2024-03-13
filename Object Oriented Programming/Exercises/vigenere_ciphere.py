# Lab Exercise #1: Problem No. 3
# Programmed by: Christian Kristopher D. Dalayoan
# Course, Year and Section: BSCpE 1-3
# Instructor: Engr. Julius S. Cansino
# Date Submitted: March 9, 2024

# Get user input
message = input("Message: ").replace(' ', '').upper()
key = input("Key: ").upper()

# Define the alphabet list
alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# Converts message to its corresponding values
message_values = []
for char in message:
    message_values.append(alphabet.index(char))

# Convert key to its corresponding values
key_values = []
for key_char in key:    
    key_values.append(alphabet.index(key_char))
while len(key_values) < len(message_values):
    key_values.append(key_values[len(key_values) % len(key)])
key_values = key_values[:len(message_values)]

# Add the message and key values
add_values = []
for i in range(len(message)):
    combine = message_values[i] + key_values[i]
    add_values.append(combine)

# Subtract 26 if the sum is greater than 26 to get the cipher text
mod_values = []
for j in range(len(add_values)):
    if add_values[j] >= 26:
        mod = add_values[j] - 26
    else:
        mod = add_values[j]
    mod_values.append(mod)

# Convert the mod values to its corresponding characters
encrypted_message = ''
for value in mod_values:
    encrypted_message += alphabet[value]

# Print the results
print(f"Add: {add_values}")
print(f"Mod: {mod_values}")
print(f"Ciphertext: {encrypted_message}")
