def add_three_copies(my_list, data):
    """Adds three copies of the given data to the provided list."""
    for i in range(3):
        my_list.append(data)  # Append the data to the list three times

########## No need to edit code past this point

def main():
    message = input("Enter a message to copy: ")  # Get user input
    my_list = []  # Initialize an empty list
    print("List before:", my_list)  # Print the list before modification
    add_three_copies(my_list, message)  # Call the function to add copies
    print("List after:", my_list)  # Print the list after modification

if __name__ == "__main__":
    main()  # Execute the main function