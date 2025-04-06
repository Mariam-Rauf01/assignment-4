# Define the conversion factor
INCHES_PER_FOOT = 12

# Function to convert feet to inches
def convert_feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

# Main program loop
while True:
    # Prompt the user for input
    feet_input = input("Enter the number of feet (or type 'exit' to quit): ")
    
    # Allow the user to exit the loop
    if feet_input.lower() == 'exit':
        print("Exiting the program.")
        break
    
    try:
        # Convert the input to a float
        feet = float(feet_input)
        
        # Perform the conversion
        inches = convert_feet_to_inches(feet)
        
        # Output the result
        print(f"{feet} foot{'s' if feet != 1 else ''} is equal to {inches} inches.\n")
    
    except ValueError:
        print("Please enter a valid number for feet.")