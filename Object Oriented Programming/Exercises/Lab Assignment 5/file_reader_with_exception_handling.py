# Write a program that reads the contents of a text file and implements error handling using try-except-finally block
# to handle exceptions such as "FileNotFoundError" and "IOError". 
# Print the contents of the file or display appropriate error messages 
# if any of these exceptions occur during file handling.

# Start error handling
try:
    # Attempt to open and read the file
    with open("sqrt_results.txt", 'r') as f:
        text = f.read()
# Handle FileNotFoundError
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")
# Handle IOError
except IOError as e:
    print(f"IOError: {e}")
# If there is no error, print the content of the file
else:
    print(text)