# Program that asks the user how many numbers they want to enter, and then asks for those numbers and prints out the sum of even and odd numbers separately.
# January 5, 2024
# Christian Kristopher D. Dalayoan

# Function to get a valid integer input from the user
def get_valid_integer(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Not a valid number. Please enter an integer.")
       
# The main function or the program itself         
def main():            
    # Get the number of inputs from the user
    count = get_valid_integer("How many numbers do you want to enter? ")

    # Initialize sums for odd and even numbers
    sum_odd = 0
    sum_even = 0

    # Ask the user to enter the specified number of numbers
    for i in range(count):
        num = get_valid_integer(f"Enter number {i+1}: ")
        
        # Check if the number is even or odd and add it to the appropriate sum
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num

    print("The sum of all odd numbers is:", sum_odd)
    print("The sum of all even numbers is:", sum_even)

# Loop that continues the program as long as the user wants to try again
while True:
    main()
    repeat = ''
    while repeat not in ['y', 'n']:
        repeat = input("Do you want to try again? (Y/N): ").lower()
    if repeat == 'n':
        break