# Lab Assignment #3: Problem No. 4
# Programmed by: Christian Kristopher D. Dalayoan
# Course, Year and Section: BSCpE 1-3
# Instructor: Engr. Julius S. Cansino
# Date Submitted: March 23, 2024

# Write a method in python will create two separate text files after reading the source text file named integers.txt that contains 20 integers. 
# The first output file will be named double.txt containing the square of all even integers found in integers.txt 
# and the second file will be named triple.txt containing the cube of all odd numbers found in the integers.txt.

# Initialize the numbers list
numbers = []

# Open the integers.txt file and append the numbers to the numbers list
with open('integers.txt') as f:
    for num in f:
        numbers.append(num)

# Initialize the squared and cubed lists
squared = [int(i)**2 for i in numbers if int(i) % 2 == 0]
cubed = [int(i)**3 for i in numbers if int(i) % 2 == 1]

# Write the squared numbers to the double.txt file
with open('double.txt', 'w') as double:
    for number in squared:
        double.write(f"{str(number)}\n")

# Write the cubed numbers to the triple.txt file
with open('triple.txt', 'w') as triple:
    for number in cubed:
        triple.write(f"{str(number)}\n")
       
