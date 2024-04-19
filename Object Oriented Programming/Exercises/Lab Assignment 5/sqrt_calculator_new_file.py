# Write a Python program that prompts the user to enter a number, calculates its square root, and handles the "ValueError" exception 
# by displaying an appropriate error message when the user enters a negative number. 
# The program should also write the results to a file named "sqrt_results.txt".

# Start error handling
try:
    number = float(input("Enter a number: ")) # Get user input
    if number < 0: # If the number is negative, raise an error
        raise ValueError("Please enter a valid positive number.")
    sqrt = number ** 0.5 # Calculate square root
# Handle ValueError
except ValueError as e:
    print(e)
# If there is no error, write to this file
else:
    with open("sqrt_results.txt", 'w') as f:
        f.write(f"The square root of {number} is {sqrt}")