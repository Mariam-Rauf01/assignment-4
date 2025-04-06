def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}  # Create an empty phonebook

    while True:
        name = input("Name: ")
        if name == "":  # Break the loop if the user enters a blank name
            break
        number = input("Number: ")
        phonebook[name] = number  # Store the name and number in the phonebook

    return phonebook  # Return the populated phonebook


def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    for name in phonebook:
        print(f"{name} -> {phonebook[name]}")  # Print each name and its associated number


def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input("Enter name to lookup: ")
        if name == "":  # Break the loop if the user enters a blank name
            break
        if name not in phonebook:  # Check if the name is in the phonebook
            print(f"{name} is not in the phonebook")
        else:
            print(phonebook[name])  # Print the associated number


def main():
    phonebook = read_phone_numbers()  # Read phone numbers from user input
    print_phonebook(phonebook)  # Print the entire phonebook
    lookup_numbers(phonebook)  # Allow the user to lookup numbers


# Python boilerplate.
if __name__ == '__main__':
    main()  # Execute the main function