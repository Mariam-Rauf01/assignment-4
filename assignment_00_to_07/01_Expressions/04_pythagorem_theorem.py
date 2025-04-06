import math

# Function to calculate the hypotenuse using the Pythagorean theorem
def calculate_hypotenuse(ab, ac):
    return math.sqrt(ab**2 + ac**2)

# Main program
while True:
    try:
        # Prompt the user for the lengths of the two sides
        ab_input = input("Enter the length of AB (or type 'exit' to quit): ")
        
        # Allow the user to exit the loop
        if ab_input.lower() == 'exit':
            print("Exiting the program.")
            break
        
        ac_input = input("Enter the length of AC: ")
        
        # Convert inputs to floats
        ab = float(ab_input)
        ac = float(ac_input)
        
        # Calculate the hypotenuse
        hypotenuse = calculate_hypotenuse(ab, ac)
        
        # Output the result
        print(f"The length of BC (the hypotenuse) is: {hypotenuse}\n")
    
    except ValueError:
        print("Please enter valid numbers for the lengths.")