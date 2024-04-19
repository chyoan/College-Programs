# Define a function capitalize_last_name() that accepts as argument a string with a (single) first and a (single) last name, 
# and returns a string in which only the first letter of the first name is uppercase, whereas all letters of the last name are uppercase; 
# in otherwords, 'marisa tomei' becomes 'Marisa TOMEI'. 
# (Tip: use str.split() to split a str into separate words.)
# If something other than a str object is passed as an argument, the function should raise a TypeError. 
# (Tip: you can use isistance() to check whether an object is of a particular type.) 
# If the str does not consist of exactly two words, the function should raise a ValueError.

def capitalize_last_name(name):
    try:
        # Check if input is a string
        if not isinstance(name, str):
            raise TypeError("Not a string object.")
        # Split the name into words
        name_list = name.split()
        # Check if there are exactly two words
        if len(name_list) != 2:
            raise ValueError("String does not consist of exactly two words.") 
        # Capitalize the first name and make the last name uppercase
        first_name = name_list[0].capitalize()
        last_name = name_list[1].upper()
        # Combine the names
        new_name = f"{first_name} {last_name}"
        return new_name
    # Handle TypeError
    except TypeError as e:
        return f"TypeError: {e}"
    # Handle ValueError
    except ValueError as e:
        return f"ValueError: {e}"
    
# Print the results
print(capitalize_last_name(23))