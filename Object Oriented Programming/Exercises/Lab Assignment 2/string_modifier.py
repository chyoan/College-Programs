# Lab Exercise #2: Problem No. 11
# Programmed by: Christian Kristopher D. Dalayoan
# Course, Year and Section: BSCpE 1-3
# Instructor: Engr. Julius S. Cansino
# Date Submitted: March 16, 2024

# Get user input
data = input("Enter a string of data: ")

# Make the first character uppercase
data = data[0].upper() + data[1:]

# Replace vowels with the next one
vowel_map = {'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a',
             'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'}
new_data = ""
for i in data:
    new_data += vowel_map.get(i, i)
data = new_data

# Replace all occurrences of 'S' or 's' with '$'
data = data.replace('S', '$').replace('s', '$')

# Replace all numbers 1-4 with double the number
num_map = {'1': '2', '2': '4', '3': '6', '4': '8'}
new_data = ""
for i in data:
    new_data += num_map.get(i, i)
data = new_data

# Print the result
print(f"New data is: {data}")
