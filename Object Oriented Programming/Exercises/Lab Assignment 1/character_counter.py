# Lab Exercise #1: Problem No. 4
# Programmed by: Christian Kristopher D. Dalayoan
# Course, Year and Section: BSCpE 1-3
# Instructor: Engr. Julius S. Cansino
# Date Submitted: March 9, 2024

# Get user input
text = input("Enter a string: ")

# Initialize counters for vowels, consonants, digits, special characters, and total characters
num_vowels = 0
num_consonants = 0
num_digits = 0
num_special = 0
num_total = 0

# Loop over each character in the text
for char in text:
    if char.isalpha():  # Check if the character is a letter
        if char in 'aeiouAEIOU':  # If it's a vowel
            num_vowels += 1
        else:  # If it's a consonant
            num_consonants += 1
    elif char.isdigit():  # Check if the character is a digit
        num_digits += 1
    else:  # If it's a special character
        num_special += 1
    num_total += 1  # Count the total number of characters

# Print the results
print(f"Number of vowels: {num_vowels}")
print(f"Number of consonants: {num_consonants}")
print(f"Number of digits: {num_digits}")
print(f"Number of special characters (including the spaces): {num_special}")
print(f"Total number of characters found on the string: {num_total}")


