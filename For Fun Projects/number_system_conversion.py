# This program contains functions for converting numbers between different number systems (decimal, binary, octal, hexadecimal).
# Note: For negative numbers, the program does not use two's complement. 
# Instead, it simply prepends a "-" sign to the representation of the absolute value of the number in the target number system.

def decimal_to_binary(decimal_number: float) -> str:
    binary_number = ''
    integer_part = int(decimal_number)
    decimal_part = abs(decimal_number) - abs(integer_part)

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

    if binary_number == '':
        binary_number = '0'
    
    if decimal_part > 0:
        binary_number += '.'
        fractional_part = ''
        while len(fractional_part) <= 10:
            decimal_part = decimal_part * 2
            integer_part = int(decimal_part)
            fractional_part += str(integer_part)
            decimal_part -= integer_part
        fractional_part = fractional_part.rstrip('0')    
        binary_number += fractional_part
    
    if is_negative:
        binary_number = '-' + binary_number
    
    return binary_number

def decimal_to_octal(decimal_number: float) -> str:
    octal_number = ''
    integer_part = int(decimal_number)
    decimal_part = abs(decimal_number) - abs(integer_part)

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

    if octal_number == '':
        octal_number = '0'

    if decimal_part > 0:
        octal_number += '.'
        fractional_part = ''
        while len(fractional_part) <= 10:
            decimal_part = decimal_part * 8
            integer_part = int(decimal_part)
            fractional_part += str(integer_part)
            decimal_part -= integer_part
        fractional_part = fractional_part.rstrip('0')
        octal_number += fractional_part
    
    if is_negative:
        octal_number = '-' + octal_number

    return octal_number

def decimal_to_hexadecimal(decimal_number: float) -> str:
    hexadecimal_conversion = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    hexadecimal_number = ''
    integer_part = int(decimal_number)
    decimal_part = abs(decimal_number) - abs(integer_part)

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
    
    if hexadecimal_number == '':
        hexadecimal_number = '0'
    
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
        fractional_part = fractional_part.rstrip('0')     
        hexadecimal_number += fractional_part

    if is_negative:
        hexadecimal_number = '-' + hexadecimal_number
    
    return hexadecimal_number

def binary_to_decimal(binary_number: str) -> float:
    decimal_number = 0
    binary_exponent = 0

    if '.' in binary_number:
        integer_binary, decimal_binary = binary_number.split('.')
    else:
        integer_binary = binary_number
        decimal_binary = ''
        
    if integer_binary[0] == '-':        
        is_negative = True
        integer_binary = integer_binary[1:]
    else:
        is_negative = False

    for digit in integer_binary[::-1]:
        if digit == '1':
            decimal_number += 2 ** binary_exponent
        binary_exponent += 1

    decimal_exponent = -1
    for digit in decimal_binary:
        if digit == '1':
            decimal_number += 2 ** decimal_exponent
        decimal_exponent -= 1
    
    if is_negative:
        decimal_number *= -1

    return decimal_number

def binary_to_octal(binary_number: str) -> str:
    octal_number = ''

    if '.' in binary_number:
        integer_binary, decimal_binary = binary_number.split('.')
    else:
        integer_binary = binary_number
        decimal_binary = ''

    if integer_binary[0] == '-':
        is_negative = True
        integer_binary = integer_binary[1:]
    else:
        is_negative = False

    while len(integer_binary) % 3 != 0:
        integer_binary = '0' + integer_binary
    while len(decimal_binary) % 3 != 0:
        decimal_binary += '0'

    integer_binary_group = [integer_binary[i:i+3] for i in range(0, len(integer_binary), 3)]
    decimal_binary_group = [decimal_binary[i:i+3] for i in range(0, len(decimal_binary), 3)]

    integer_octal = ''
    for group in integer_binary_group:
        integer_exponent = 0
        octal_digit = 0
        for digit in group[::-1]:
            if int(digit) == 1:
                octal_digit += 2 ** integer_exponent
            integer_exponent += 1
        integer_octal += str(octal_digit)
    
    decimal_octal = ''
    for group in decimal_binary_group:
        decimal_exponent = 0
        octal_digit = 0
        for digit in group[::-1]:
            if int(digit) == 1:
                octal_digit += 2 ** decimal_exponent
            decimal_exponent += 1
        decimal_octal += str(octal_digit)

    octal_number = integer_octal      
    if decimal_octal != '':
        octal_number += '.' + decimal_octal.rstrip('0')      

    if is_negative:
        octal_number = '-' + octal_number

    return octal_number

def binary_to_hexadecimal(binary_number: str) -> str:
    hexadecimal_number = ''
    hexadecimal_conversion = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    if '.' in binary_number:
        integer_binary, decimal_binary = binary_number.split('.')
    else:
        integer_binary = binary_number
        decimal_binary = ''

    if integer_binary[0] == '-':
        is_negative = True
        integer_binary = integer_binary[1:]
    else:
        is_negative = False

    while len(integer_binary) % 4 != 0:
        integer_binary = '0' + integer_binary
    while len(decimal_binary) % 4 != 0:
        decimal_binary += '0'
    
    integer_binary_group = [integer_binary[i:i+4] for i in range(0, len(integer_binary), 4)]
    decimal_binary_group = [decimal_binary[i:i+4] for i in range(0, len(decimal_binary), 4)]

    integer_hexadecimal = ''
    for group in integer_binary_group:
        integer_exponent = 0
        hexadecimal_digit = 0
        for digit in group[::-1]:
            if int(digit) == 1:
                hexadecimal_digit += 2 ** integer_exponent
            integer_exponent += 1
        if hexadecimal_digit in hexadecimal_conversion:
            hexadecimal_digit = hexadecimal_conversion[hexadecimal_digit]
        integer_hexadecimal += str(hexadecimal_digit)

    decimal_hexadecimal = ''
    for group in decimal_binary_group:
        decimal_exponent = 0
        hexadecimal_digit = 0
        for digit in group[::-1]:
            if int(digit) == 1:
                hexadecimal_digit += 2 ** decimal_exponent
            decimal_exponent += 1
        if hexadecimal_digit in hexadecimal_conversion:
            hexadecimal_digit = hexadecimal_conversion[hexadecimal_digit]
        decimal_hexadecimal += str(hexadecimal_digit)
    
    hexadecimal_number = integer_hexadecimal
    if decimal_hexadecimal != '':
        hexadecimal_number += '.' + decimal_hexadecimal
    if is_negative:
        hexadecimal_number = '-' + hexadecimal_number

    return hexadecimal_number

def octal_to_decimal(octal_number: float) -> float:
    decimal_number = 0
    integer_part, decimal_part = str(octal_number).split('.')

    if integer_part == '0' and decimal_part == '0':
        return 0
    elif integer_part[0] == '-':
        is_negative = True
        integer_part = integer_part[1:]
    else:
        is_negative = False
    
    integer_exponent = 0
    for digit in integer_part[::-1]:
        decimal_number += int(digit) * 8 ** integer_exponent
        integer_exponent += 1

    decimal_exponent = -1
    for digit in decimal_part:
        decimal_number += int(digit) * 8 ** decimal_exponent
        decimal_exponent -= 1

    if is_negative:
        decimal_number *= -1
    
    return decimal_number

def octal_to_binary(octal_number: float) -> str:
    binary_number = ''
    integer_part, decimal_part = str(octal_number).split('.')
    octal_representation_binary = {'0': '000',
                                   '1': '001',
                                   '2': '010',
                                   '3': '011',
                                   '4': '100',
                                   '5': '101',
                                   '6': '110',
                                   '7': '111'}

    if integer_part == '0' and decimal_part == '0':
        return '0'
    elif integer_part[0] == '-':
        is_negative = True
        integer_part = integer_part[1:]
    else:
        is_negative = False

    for octal, binary in octal_representation_binary.items():
        integer_part = integer_part.replace(octal, binary)
        decimal_part = decimal_part.replace(octal, binary)
    
    if '.' in str(octal_number) and decimal_part != '000':
        binary_number = integer_part.lstrip('0') + '.' + decimal_part.rstrip('0')
    else:
        binary_number = integer_part.lstrip('0')
    
    if is_negative:
        binary_number = '-' + binary_number

    return binary_number

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
            while True:
                binary_number = input("\nEnter a binary number: ")
                if (binary_number[0] == '-' and all(char in '01.' for char in binary_number[1:]) and binary_number.count('.') <= 1) \
                or (all(digit in '01.' for digit in binary_number) and binary_number.count('.') <= 1):
                    break
                else:
                    print("Invalid binary number.")

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
            while True:
                try:
                    octal_number = input("\nEnter an octal number: ")
                    if '8' in octal_number or '9' in octal_number:
                        raise ValueError("Octal numbers can only contain digits 0-7.")
                    octal_number = float(octal_number)
                    break
                except ValueError as e:
                    print(e)
                    continue

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