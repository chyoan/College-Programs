# Create a Simple App Calculator
# 1. The application will ask the user to choose one of the four math operations (Addition, Subtraction, Multiplication and Division)
# 2. The application will ask the user for two numbers
# 3. Display the result
# 4. The application will ask if the user wants to try again or not.
# 5. If yes, repeat Step 1.
# 6. If no, Display “Thank you!” and the program will exit
# 7. Use Python Function and appropriate Exceptions to capture errors during runtime.

# Define the main function
def main():
    while True:
        print("Choose one of the four math operators:")
        print("1: Addition")
        print("2: Subtraction")
        print("3: Multiplication")
        print("4: Division")

        # Validate user input for operation choice
        while True:
            operation = input("Enter the number corresponding to your choice: ")
            
            if operation not in ['1', '2', '3', '4']:
                print("Invalid input. Please enter a number from 1 to 4 only.")
            else:
                break
        
        # Get user input for two numbers
        while True:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                # Perform the selected operation
                if operation == '1':
                    result = num1 + num2
                elif operation == '2':
                    result = num1 - num2
                elif operation == '3':
                    result = num1 * num2
                else:
                    result = num1 / num2
                print(f"The result is: {result}")
                break 
            
            except ValueError as e:
                print(f"{e}: Invalid syntax.")
            except ZeroDivisionError as e:
                print(f"{e}: You can not divide by zero.")
            except KeyboardInterrupt:
                print("\nProgram interrupted by the user. Exiting...")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        
        # Asks the user if they want to try again
        while True:
            choice = input("Do you want to try again? (Y/N) ").upper()
            if choice not in ['Y', 'N']:
                print("Please enter Y or N only.")
            else:
                break
        if choice == 'N':
            print("Thank you!")
            break
        print()

# Call the main function to start the program
main()