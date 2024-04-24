# This program contains functions for converting numbers between different number systems (decimal, binary, octal, hexadecimal).
# Note: For negative numbers, the program does not use two's complement. 
# Instead, it simply prepends a "-" sign to the representation of the absolute value of the number in the target number system.

def decimal_to_binary(decimal_number):
    binary_number = ''
    
    if decimal_number == 0:
        return '0'
    elif decimal_number < 0:
        is_negative = True
        decimal_number = abs(decimal_number)
    else:
        is_negative = False

    while decimal_number > 0:
        remainder = decimal_number % 2
        decimal_number = decimal_number // 2 
        binary_number = str(remainder) + binary_number
    
    if is_negative:
        binary_number = '-' + binary_number
    
    return binary_number

def decimal_to_octal(decimal_number):
    octal_number = ''

    if decimal_number == 0:
        return '0'
    elif decimal_number < 0:
        is_negative = True
        decimal_number = abs(decimal_number)
    else:
        is_negative = False

    while decimal_number > 0:
        remainder = decimal_number % 8
        decimal_number = decimal_number // 8
        octal_number = str(remainder) + octal_number
    
    if is_negative:
        octal_number = '-' + octal_number

    return octal_number

def decimal_to_hexadecimal(decimal_number):
    hexadecimal_conversion = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    hexadecimal_number = ''

    if decimal_number == 0:
        return '0'
    elif decimal_number < 0:
        is_negative = True
        decimal_number = abs(decimal_number)
    else:
        is_negative = False
    
    while decimal_number > 0:
        remainder = decimal_number % 16
        if remainder in hexadecimal_conversion:
            remainder = hexadecimal_conversion[remainder]

        decimal_number = decimal_number // 16
        hexadecimal_number = str(remainder) + hexadecimal_number
    
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

print(binary_to_decimal("1010101"))

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

