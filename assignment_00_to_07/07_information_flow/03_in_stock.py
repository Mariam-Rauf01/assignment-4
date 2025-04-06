def num_in_stock(fruit: str) -> int:
    """
    This function returns the number of fruit Sophia has in stock.
    """
    if fruit == 'apple':
        return 2
    if fruit == 'durian':
        return 4
    if fruit == 'pear':
        return 1000
    else:
        # This fruit is not in stock.
        return 0

def main():
    fruit: str = input("Enter a fruit: ")  # Prompt the user for a fruit
    stock = num_in_stock(fruit)  # Get the number of that fruit in stock
    if stock == 0:
        print("This fruit is not in stock.")  # Print if the fruit is not in stock
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)  # Print the number of fruits in stock

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()  # Execute the main function