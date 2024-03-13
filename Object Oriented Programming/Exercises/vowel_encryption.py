# Lab Exercise #1: Problem No. 1
# Programmed by: Christian Kristopher D. Dalayoan
# Course, Year and Section: BSCpE 1-3
# Instructor: Engr. Julius S. Cansino
# Date Submitted: March 9, 2024

# Define encryption key
encryption_key = {'a':'*', 'e':'&', 'i':'#', 'o':'+', 'u':'!'}

# Get user input
text = input("Enter a string to encrypt: ")

# Replace vowels with special characters
for key, value in encryption_key.items():
    text = text.replace(key, value)

# Print encrypted string
print(f"Encrypted string: {text}")


