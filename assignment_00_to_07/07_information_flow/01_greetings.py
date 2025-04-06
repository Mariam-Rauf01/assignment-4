def greet(name: str) -> str:
    """
    Returns a greeting string for the given name.
    """
    return "Greetings " + name + "!"  # Return the greeting

def main():
    name: str = input("What's your name? ")  # Prompt the user for their name
    print(greet(name))  # Call the greet function and print the greeting

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()  # Execute the main function