#Program that prints a specific pattern of stars
#January 14, 2023
#Christian Kristopher D. Dalayoan

#Prompts the user to enter the valid pattern to print
def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 3:
                return value
            else:
                print("Please enter a valid number between 1 and 3.")
        except ValueError:
            print("Please enter a valid integer.")

#Prompts the user to enter the number of rows to print
def get_valid_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a valid number greater than 0.")
        except ValueError:
            print("Please enter a valid integer.")

#Star Pattern 1
def pattern1():
    #Upper part of the pattern
    for row in range(n):
        for left_star in range(row+1):
            print ('*', end=' ')
        print()
    #lower part of the pattern
    for row in range(n):
        for left_star in range(row, n-1):
            print('*', end=' ')
        print()

#Star Pattern 2
def pattern2():
    #Upper part of the pattern
    for row in range(n):
        for left_space in range(row,n-1):
            print(' ', end=' ')
        for right_star in range(row+1):
            print('*', end=' ')
        print()
    #Lower part of the pattern
    for row in range(n):
        for left_space in range(row+1):
            print(' ', end=' ')
        for right_star in range(row,n-1):
            print('*', end=' ')
        print()

#Star Pattern 3
def pattern3():
    #Upper part of the pattern
    for row in range(n-1, -1, -1):
        for left_star in range(row, n-1):
            print('*', end=' ')
        for left_space in range(row):
            print(' ', end=' ')
        for right_space in range(row+1):
            print(' ', end=' ')
        for right_star in range(row, n-1):
            print('*', end=' ')
        print()
    #Middle part of the pattern
    for row in range(1):
        print('* ' * (2*n-1))
    #Lower part of the pattern
    for row in range(n):
        for left_star in range(row, n-1):
            print('*', end=' ')
        for left_space in range(row):
            print(' ', end=' ')
        for right_space in range(row+1):
            print(' ', end=' ')
        for right_star in range(row, n-1):
            print('*', end=' ')
        print()

#Asks the user if they want to change the number of rows to print
def row_num():
    global n
    while True:
        change = input("Would you like to change the number of rows to print? Y/N: ").upper()
        if change == 'Y':
            n = get_valid_integer("Enter the number of rows to print: ")
            break
        elif change == 'N':
            break
        else:
            print("Please enter Y or N.")

#Asks the user if they want to print another pattern
def try_again():
    while True:
        again = input("Would you like to print another pattern? Y/N: ").upper()
        if again == 'Y':
            row_num()
            main()
        elif again == 'N':
            break
        else:
            print("Please enter Y or N.")
    
#The main function
def main():
    selected_pattern = get_valid_input("Enter a pattern (1, 2, or 3): ")

    if selected_pattern == 1:
        pattern1()
    elif selected_pattern == 2:
        pattern2()
    elif selected_pattern == 3:
        pattern3()
    
# Default number of rows to print
n = 5  

#Runs the main function
main()

#Runs the try_again function
try_again()
