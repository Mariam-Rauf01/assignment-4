# Define the speed of light in meters per second
C = 299792458  # m/s

while True:
    # Prompt the user for mass input
    try:
        mass_input = input("Enter kilos of mass (or type 'exit' to quit): ")
        
        # Allow the user to exit the loop
        if mass_input.lower() == 'exit':
            print("Exiting the program.")
            break
        
        # Convert the input to a float
        mass = float(mass_input)
        
        # Calculate energy using E = m * c^2
        energy = mass * (C ** 2)
        
        # Output the results
        print(f"\ne = m * C^2...")
        print(f"m = {mass} kg")
        print(f"C = {C} m/s")
        print(f"{energy} joules of energy!\n")
    
    except ValueError:
        print("Please enter a valid number for mass.")