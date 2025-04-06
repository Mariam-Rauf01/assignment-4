def get_first_element(lst):
    """
    Prints the first element of a provided list.
    """
    print(lst[0])  # Print the first element of the list

# There is no need to edit code beyond this point

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []  # Initialize an empty list
    elem: str = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":  # Continue until the user presses enter without input
        lst.append(elem)  # Add the element to the list
        elem = input("Please enter an element of the list or press enter to stop: ")  # Prompt for the next element
    return lst  # Return the populated list

def main():
    lst = get_lst()  # Get the list from user input
    get_first_element(lst)  # Print the first element of the list

if __name__ == '__main__':
    main()  # Execute the main function