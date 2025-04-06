def main():
    # Dictionary of fruits and their prices
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }
    
    total_cost = 0  # Initialize total cost to zero
    
    # Loop through each fruit in the dictionary
    for fruit_name in fruits:
        price = fruits[fruit_name]  # Get the price of the current fruit
        amount_bought = int(input(f"How many ({fruit_name}) do you want to buy?: "))  # Prompt user for quantity
        total_cost += (price * amount_bought)  # Calculate total cost for this fruit and add to total
    
    # Print the total cost
    print(f"Your total is ${total_cost:.2f}")  # Format total cost to 2 decimal places

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()  # Execute the main function