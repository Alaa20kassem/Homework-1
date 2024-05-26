
def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        if digit not in ['0', '1']:
            return None
        decimal = decimal * 2 + int(digit)
    return decimal

try:
    binary_number = input("Enter a binary number: ")
    decimal_number = binary_to_decimal(binary_number)
    
    if decimal_number is not None:
        print(f"The decimal equivalent of {binary_number} is: {decimal_number}")
    else:
        print("Invalid binary number. Please enter a binary number containing only 0s and 1s.")
except ValueError:
    print("Invalid input. Please enter a valid binary number.")
