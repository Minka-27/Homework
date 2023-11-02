
def is_isogram(input_string):
    # Remove spaces and convert the input string to lowercase to ensure case-insensitivity
    new_input_string = input_string.replace(" ","").lower()
    print(new_input_string)

    # Store the characters from the input string
    string_count = {}

    # Loop through the characters in the input string
    for char in new_input_string:
        # If a character is already in the set, it's not an isogram
        if char in string_count:
            print(False)
            return False
        # Increase counter
        string_count[char] = 1
    # If a character isn't already in the set, it's an isogram
    print(True)
    return True

is_isogram("isv GRA M")
