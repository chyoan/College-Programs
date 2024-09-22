print("Temperature Converter\n")

while True:
    try:
        temperature = float(input("Please input a temperature: "))
        break
    except ValueError:
        print("Invalid input. Please input a valid temperature.\n")

print("\nConversion Types:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

while True:
    conversion_type = input("\nSelect the conversion type [1 or 2]: ")
    if conversion_type in ["1", "2"]:
        break
    else:
        print("Please select a valid conversion type [1 or 2].")

if conversion_type == "1":
    converted_temp = f"{(9/5) * temperature + 32 :.2f} °F"
else:
    converted_temp = f"{(5/9) * (temperature - 32 ) :.2f} °C"

print(f"Your converted temperature is {converted_temp}")