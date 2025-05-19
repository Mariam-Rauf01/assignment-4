import random
import string

print("Welcome to the Password Generator!")

# Get input from the user
num_passwords = int(input("How many passwords would you like to generate? "))
password_length = int(input("What should be the length of each password? "))

# Define the characters to use in the password
characters = string.ascii_letters + string.digits + string.punctuation

print("\nHere are your passwords:")

# Generate passwords
for i in range(num_passwords):
    password = ''.join(random.choice(characters) for _ in range(password_length))
    print(f"{i + 1}: {password}")
