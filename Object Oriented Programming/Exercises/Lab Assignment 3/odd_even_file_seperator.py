# Lab Assignment #3: Problem No. 1
# Programmed by: Christian Kristopher D. Dalayoan
# Course, Year and Section: BSCpE 1-3
# Instructor: Engr. Julius S. Cansino
# Date Submitted: March 16, 2024

# Write a Python program that reads a text file named numbers.txt that contains 20 integers. 
# The program will create two other text files; 
# the first text file will be named even.txt that will contain all even numbers extracted from the numbers.txt.  
# The second text file will be named odd.txt  
# that will contain all odd numbers extracted from the numbers.txt.

# Initialize odd and even lists
evens = []
odds = []

# Initialize total of odd and even variables
even_total = 0
odd_total = 0

# Open the numbers.txt file and append the even and odd numbers to their respective lists
numbers = open("numbers.txt", "r")
for number in numbers:
    if int(number) % 2 == 0:
        evens.append(number)
        even_total += 1
    else:
        odds.append(number)
        odd_total += 1
        
# Write the even numbers to the even.txt file
even_file = open("even.txt", "w")
for number in evens:
    even_file.write(f"{str(number)}")
even_file.write(f"The total of all even numbers is: {even_total}")
even_file.close()

# Write the odd numbers to the odd.txt file
odd_file = open("odd.txt", "w")
for number in odds:
    odd_file.write(f"{str(number)}")
odd_file.write(f"The total of all odd numbers is: {odd_total}")
odd_file.close()
