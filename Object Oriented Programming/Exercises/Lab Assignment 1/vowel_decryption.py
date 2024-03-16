# Lab Exercise #1: Problem No. 2
# Programmed by: Christian Kristopher D. Dalayoan
# Course, Year and Section: BSCpE 1-3
# Instructor: Engr. Julius S. Cansino
# Date Submitted: March 9, 2024

# Define decryption key
decryption_key = {'*':'a', '&':'e', '#':'i', '+':'o', '!':'u'}

# Get user input
text = input("Enter a string to decrypt: ")

# Replace special characters with vowels
for key, value in decryption_key.items():
    text = text.replace(key, value)

# Print decrypted string
print(f"The Plain Text: {text}")

