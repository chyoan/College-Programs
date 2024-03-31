# Lab Assignment #3: Problem No. 3
# Programmed by: Christian Kristopher D. Dalayoan
# Course, Year and Section: BSCpE 1-3
# Instructor: Engr. Julius S. Cansino
# Date Submitted: March 23, 2024

# Write a method in python to write multiple line of text contents into a text file mylife.txt. 

# Function to write lines to a text file
def write_line():
    with open('mylife.txt', 'a') as f:
        line = input("Enter line: ")
        f.write(f"{line}\n")

# Main function
def main():
    write_line()
    
    while True:
        again = input("Are there more lines y/n? ").lower()
        if again not in ['y', 'n']:
            print("Please input y/n only.")
        elif again == 'y':
            write_line()
        else:
            break

# Call the main function   
main()

