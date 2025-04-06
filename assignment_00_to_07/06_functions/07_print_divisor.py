def print_divisors(num: int):
    print("Here are the divisors of", num)
    for i in range(1, num + 1):  # Loop from 1 to num inclusive
        if num % i == 0:  # Check if i is a divisor of num
            print(i)  # Print the divisor

def main():
    num = int(input("Enter a number: "))  # Prompt the user for a number
    print_divisors(num)  # Call the function to print divisors

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()  # Execute the main function