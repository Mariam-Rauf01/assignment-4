def get_user_info():
    """
    Prompts the user for their first name, last name, and email address,
    and returns these pieces of data as a tuple.
    """
    first_name: str = input("What is your first name?: ")  # Prompt for first name
    last_name: str = input("What is your last name?: ")    # Prompt for last name
    email_address: str = input("What is your email address?: ")  # Prompt for email address
    
    return first_name, last_name, email_address  # Return the data as a tuple

########## No need to edit code past this point :) ##########

def main():
    user_data = get_user_info()  # Call the function to get user data
    print("Received the following user data:", user_data)  # Print the received data

if __name__ == "__main__":
    main()  # Execute the main function