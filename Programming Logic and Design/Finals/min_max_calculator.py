def main():
    num1, num2 = map(int,input("Enter two integers: ").split())
    
    choice  = int(input("Enter 1 for min, 2 for max: "))
    
    if choice == 1:
        result = min(num1, num2)
    elif choice == 2:
        result = max(num1, num2)
    else:
        result = 0
    
    print(f"Result = {result}")

def try_again():
    while True:
        again = input("Do you want to try again Y/N ").upper()
        if again == 'Y':
            main()
        elif again == 'N':
            break
        else:
            print("Please enter Y or N.")

main()
try_again()
