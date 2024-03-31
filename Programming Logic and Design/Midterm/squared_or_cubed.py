def get_valid_input(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Please enter a valid number.")
    
number = get_valid_input("Please enter a number: ")    

char = input("Enter a letter: ").upper()

if char == 'S':
    print(number**2)
elif char == 'C':
    print(number**3)
else:
    print("Invalid character.")
    
