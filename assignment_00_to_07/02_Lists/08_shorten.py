MAX_LENGTH: int = 3  # Define the maximum length for the list

def shorten(lst):
    """Removes elements from the end of lst until it is MAX_LENGTH items long."""
    while len(lst) > MAX_LENGTH:  # While the list is longer than MAX_LENGTH
        last_elem = lst.pop()  # Remove the last element
        print(last_elem)  # Print the removed element

# There is no need to edit code beyond this point

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []  # Initialize an empty list
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":  # Continue until the user presses enter without input
        lst.append(elem)  # Add the element to the list
        elem = input("Please enter an element of the list or press enter to stop: ")  # Prompt for the next element
    return lst  # Return the populated list

def main():
    lst = get_lst()  # Get the list from user input
    shorten(lst)  # Shorten the list if necessary

if __name__ == '__main__':
    main()  # Execute the main function