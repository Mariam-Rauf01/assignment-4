ADULT_AGE: int = 18  # U.S. age 

def is_adult(age: int) -> bool:
    """
    Returns True if age is greater than or equal to ADULT_AGE, otherwise returns False.
    """
    if age >= ADULT_AGE:
        return True
    return False

########## No need to edit code beyond this point :) ##########

def main():
    age: int = int(input("How old is this person?: "))  # Correctly convert input to int
    print(is_adult(age))  # Call the function and print the result

if __name__ == "__main__":
    main()  # Execute the main function