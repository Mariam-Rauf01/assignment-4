MINIMUM_HEIGHT: int = 50  # Minimum height requirement in arbitrary units

def main():
    # Ask the user for their height
    height = float(input("How tall are you? "))
    
    # Check if the user meets the height requirement
    if height >= MINIMUM_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

def tall_enough_extension():
    """Repeatedly ask the user for their height until they enter nothing."""
    while True:
        user_input = input("How tall are you? ")
        if user_input == "":  # Stop if the user enters nothing
            break
        height = float(user_input)  # Convert input to float
        if height >= MINIMUM_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    # Uncomment the line below to use the basic version
    # main()
    
    # Uncomment the line below to use the extended version
    tall_enough_extension()  # Execute the extended function