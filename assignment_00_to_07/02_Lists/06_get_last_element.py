def get_last_element(lst):
    """ Prints the last element of the provided list. """
    # Print the last element using negative indexing
    print(lst[-1])  # This is a concise way to access the last element

# There is no need to edit code beyond this point

def get_lst():
    """ Prompts the user to enter one element of the list at a time and returns the resulting list. """
    lst = []  # Initialize an empty list
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":  # Continue until the user presses enter without input
        lst.append(elem)  # Add the element to the list
        elem = input("Please enter an element of the list or press enter to stop: ")  # Prompt for the next element
    return lst  # Return the populated list

def main():
    lst = get_lst()  # Get the list from user input
    get_last_element(lst)  # Print the last element of the list

if __name__ == '__main__':
    main()  # Execute the main function