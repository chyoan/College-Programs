# You're going to write an interactive calculator! 
# User input is assumed to be a formula that consist of a number, an operator (at least + and -), 
# and another number, separated by white space (e.g. 1 + 1). 
# Split user input using str.split(), and check whether the resulting list is valid:
# If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception. 
# Try to convert the first and third input to a float (like so: float_value = float(str_value)). 
# Catch any ValueError that occurs, and instead raise a FormulaError.  
# If the second input is not '+' or '-', again raise a FormulaError. 
# If the input is valid, perform the calculation and print out the result. 
# The user is then prompted to provide new input, and so on, until the user enters quit.

# Custom exception
class FormulaError(Exception):
    pass

# Continuously prompt the user for input until they enter 'quit'
while True:
    try: 
        # Get user input
        user_input = input("Enter a number, an operator, and another number seperated by a space (e.g. 1 + 1): ")
        # Check if the user wants to quit
        if user_input.lower() == 'quit':
            break
        # Split the user input
        user_input = user_input.split()
        # Check if the user input is valid
        if len(user_input) != 3:
            raise FormulaError("FormulaError: Please enter a valid formula.")
        # Check if the first and third inputs are numbers
        try:
            first_float_value = float(user_input[0])
            third_float_value = float(user_input[2])
        except ValueError:
            raise FormulaError("FormulaError: The first and third inputs must be numbers.")
        # Check if the second input is a valid operator
        if user_input[1] not in ['+', '-', '*', '/']:
            raise FormulaError("FormulaError: Please enter a valid operator.")
        # Determine the operator
        operator = user_input[1]
    # Handle FormulaError
    except FormulaError as e:
        print(e)
    # If there is no error, calculate the result
    else:
        try:
            if operator == '+':
                result = first_float_value + third_float_value
            elif operator == '-':
                result = first_float_value - third_float_value
            elif operator == '*':
                result = first_float_value * third_float_value
            elif operator == '/':
                result = first_float_value / third_float_value
        except ZeroDivisionError as e:
            print(f"ZeroDivisionError: {e}")
        else:
            # Print the result
            print(f"The result of {first_float_value} {operator} {third_float_value} is {result}")