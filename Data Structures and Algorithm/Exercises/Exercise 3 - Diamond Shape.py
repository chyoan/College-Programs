print("Diamond Shape\n")

def print_diamond(n):
    if n % 2 == 0:
        print("Please provide an odd integer.")
        return
    
    for i in range(1, n+1, 2):
        print(' ' * ((n-i) // 2) + '*' * i)
    for i in range(n-2, 0, -2):
        print(' ' * ((n-i) // 2) + '*' * i)

while True:
    try:
        n = int(input("Enter the width of the diamond: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")

print_diamond(n)