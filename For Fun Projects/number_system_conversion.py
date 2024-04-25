# This program contains functions for converting numbers between different number systems (decimal, binary, octal, hexadecimal).
# Note: For negative numbers, the program does not use two's complement. 
# Instead, it simply prepends a "-" sign to the representation of the absolute value of the number in the target number system.

def decimal_to_binary(decimal_number):  
    binary_number = ''
    integer_part = int(decimal_number)
    decimal_part = decimal_number - integer_part

    if integer_part == 0 and decimal_part == 0:
        return '0'
    elif integer_part < 0:
        is_negative = True
        integer_part = abs(integer_part)
    else:
        is_negative = False
    
    while integer_part > 0:
        remainder = integer_part % 2
        integer_part = integer_part // 2
        binary_number = str(remainder) + binary_number
    
    if decimal_part > 0:
        binary_number += '.'
        fractional_part = ''
        while len(fractional_part) <= 10:
            decimal_part = decimal_part * 2
            integer_part = int(decimal_part)
            fractional_part += str(integer_part)
            decimal_part -= integer_part
        binary_number += fractional_part
    
    if is_negative:
        binary_number = '-' + binary_number
    
    return binary_number

def decimal_to_octal(decimal_number):
    octal_number = ''
    integer_part = int(decimal_number)
    decimal_part = decimal_number - integer_part

    if integer_part == 0 and decimal_part == 0:
        return '0'
    elif integer_part < 0:
        is_negative = True
        integer_part = abs(integer_part)
    else:
        is_negative = False

    while integer_part > 0:
        remainder = integer_part % 8
        integer_part = integer_part // 8
        octal_number = str(remainder) + octal_number

    if decimal_part > 0:
        octal_number += '.'
        fractional_part = ''
        while len(fractional_part) <= 10:
            decimal_part = decimal_part * 8
            integer_part = int(decimal_part)
            fractional_part += str(integer_part)
            decimal_part -= integer_part
        octal_number += fractional_part
    
    if is_negative:
        octal_number = '-' + octal_number

    return octal_number

def decimal_to_hexadecimal(decimal_number):
    hexadecimal_conversion = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    hexadecimal_number = ''
    integer_part = int(decimal_number)
    decimal_part = decimal_number - integer_part

    if integer_part == 0 and decimal_part == 0:
        return '0'
    elif integer_part < 0:
        is_negative = True
        integer_part = abs(integer_part)
    else:
        is_negative = False
    
    while integer_part > 0:
        remainder = integer_part % 16
        if remainder in hexadecimal_conversion:
            remainder = hexadecimal_conversion[remainder]

        integer_part = integer_part // 16
        hexadecimal_number = str(remainder) + hexadecimal_number
    
    if decimal_part > 0:
        hexadecimal_number += '.'
        fractional_part = ''
        while len(fractional_part) <= 10:
            decimal_part = decimal_part * 16
            integer_part = int(decimal_part)
            decimal_part -= integer_part
            if integer_part in hexadecimal_conversion:
                integer_part = hexadecimal_conversion[integer_part]
            fractional_part += str(integer_part)
        hexadecimal_number += fractional_part

    if is_negative:
        hexadecimal_number = '-' + hexadecimal_number
    
    return hexadecimal_number

def binary_to_decimal(binary_number):
    decimal_number = 0
    exponent = 0
    for digit in binary_number[::-1]:
        if digit == '0':
            exponent += 1
            continue
        value = 2 ** exponent
        exponent += 1
        decimal_number += value

    return decimal_number

def binary_to_octal(binary_number):
    ...

def binary_to_hexadecimal(binary_number):
    ...

def octal_to_decimal(octal_number):
    ...

def octal_to_binary(octal_number):
    ...

def octal_to_hexadecimal(octal_number):
    ...

def hexadecimal_to_decimal(hexadecimal_number):
    ...

def hexadecimal_to_binary(hexadecimal_number):
    ...

def hexadecimal_to_octal(hexadecimal_number):
    ...

def main():
    while True:
        print("\nChoose the type of number you are inputting:")
        print("[1] Decimal")
        print("[2] Binary")
        print("[3] Octal")
        print("[4] Hexadecimal")
        print("[5] Exit")

        choice1 = input("\nEnter your choice: ")

        if choice1 == '1':
            while True:
                try:
                    decimal_number = float(input("\nEnter a decimal number: "))
                    break
                except ValueError as e:
                    print(e)
                    continue

            while True:
                print("\nChoose the type of conversion you want to perform:")
                print("[1] Decimal to Binary")
                print("[2] Decimal to Octal")
                print("[3] Decimal to Hexadecimal")
                print("[4] Back to main menu")

                choice2 = input("\nEnter your choice: ")

                if choice2 == '1':
                    print(decimal_to_binary(decimal_number))
                    break
                elif choice2 == '2':
                    print(decimal_to_octal(decimal_number))
                    break
                elif choice2 == '3':
                    print(decimal_to_hexadecimal(decimal_number))
                    break
                elif choice2 == '4':
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")

        elif choice1 == '2':
            binary_number = input("\nEnter a binary number: ")
            while True:
                print("\nChoose the type of conversion you want to perform:")
                print("[1] Binary to Decimal")
                print("[2] Binary to Octal")
                print("[3] Binary to Hexadecimal")
                print("[4] Back to main menu")

                choice2 = input("\nEnter your choice: ")

                if choice2 == '1':
                    print(binary_to_decimal(binary_number))
                    break
                elif choice2 == '2':
                    print(binary_to_octal(binary_number))
                    break
                elif choice2 == '3':
                    print(binary_to_hexadecimal(binary_number))
                    break
                elif choice2 == '4':
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")

        elif choice1 == '3':
            octal_number = input("\nEnter an octal number: ")
            while True:
                print("\nChoose the type of conversion you want to perform:")
                print("[1] Octal to Decimal")
                print("[2] Octal to Binary")
                print("[3] Octal to Hexadecimal")
                print("[4] Back to main menu")

                choice2 = input("\nEnter your choice: ")

                if choice2 == '1':
                    print(octal_to_decimal(octal_number))
                    break
                elif choice2 == '2':
                    print(octal_to_binary(octal_number))
                    break
                elif choice2 == '3':
                    print(octal_to_hexadecimal(octal_number))
                    break
                elif choice2 == '4':
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")

        elif choice1 == '4':
            hexadecimal_number = input("\nEnter a hexadecimal number: ")
            while True:
                print("\nChoose the type of conversion you want to perform:")
                print("[1] Hexadecimal to Decimal")
                print("[2] Hexadecimal to Binary")
                print("[3] Hexadecimal to Octal")
                print("[4] Back to main menu")

                choice2 = input("\nEnter your choice: ")

                if choice2 == '1':
                    print(hexadecimal_to_decimal(hexadecimal_number))
                    break
                elif choice2 == '2':
                    print(hexadecimal_to_binary(hexadecimal_number))
                    break
                elif choice2 == '3':
                    print(hexadecimal_to_octal(hexadecimal_number))
                    break
                elif choice2 == '4':
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")

        elif choice1 == '5':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

        while True:
            try_again = input("\nDo you want to try again? (Y/N): ").lower()
            if try_again == 'n':
                return
            elif try_again == 'y':
                break
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")

if __name__ == "__main__":
    main()