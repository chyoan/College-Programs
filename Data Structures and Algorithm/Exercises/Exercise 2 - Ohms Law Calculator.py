print("Ohm's Law Calculator\n")

print("Select the quantity you want to calculate:")
print("1. Voltage")
print("2. Current")
print("3. Resistance")

while True:
    to_calculate = input("\nEnter the number corresponding to your choice [1, 2, or 3]: ")
    if to_calculate in ["1", "2", "3"]:
        break
    else:
        print("Invalid input. Please select a valid quantity to calculate.")

while True:
    try:
        if to_calculate == "1":
            current = float(input("Enter the current in amperes: "))
            resistance = float(input("Enter the resistance in ohms: "))
            voltage = current * resistance
            print(f"\nThe voltage with a current of {current} A and resistance of {resistance} Ω is {voltage} V.")
            break
        elif to_calculate == "2":
            voltage = float(input("Enter the voltage in volts: "))
            resistance = float(input("Enter the resistance in ohms: "))
            current = voltage / resistance
            print(f"\nThe current with a voltage of {voltage} V and resistance of {resistance} Ω is {current} A.")
            break
        else:
            voltage = float(input("Enter the voltage in volts: "))
            current = float(input("Enter the current in amperes: "))
            resistance = voltage / current
            print(f"\nThe resistance with a voltage of {voltage} V and current of {current} A is {resistance} Ω.")
            break
    except ZeroDivisionError as e:
        print(f"Error: {e}. You cannot divide by zero. Please enter a valid number.\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")
