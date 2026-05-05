def convert_temperature():
    # Display the main options menu to the user
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    # Prompt the user to choose an option and remove any trailing or leading whitespaces
    choice = input("\nChoose an option (1 or 2): ").strip()
    
    # Validate that the entered choice is exactly "1" or "2"
    if choice not in ["1", "2"]:
        # Display an error message and exit the function early if the input is incorrect
        print("Invalid option. Please restart the program.")
        return

    # Start a try-except block to handle potential data conversion errors
    try:
        # Prompt the user for the temperature and convert the string to a floating-point number
        temperature = float(input("Enter the temperature value: "))
        
        # Check if the user chose option 1 (Celsius to Fahrenheit)
        if choice == "1":
            # Apply the mathematical conversion formula for Fahrenheit
            result = (temperature * 9/5) + 32
            # Print the final result formatted to display exactly two decimal places
            print(f"\n{temperature} degrees Celsius is equal to {result:.2f} degrees Fahrenheit.")
        
        # Check if the user chose option 2 (Fahrenheit to Celsius)
        elif choice == "2":
            # Apply the mathematical conversion formula for Celsius
            result = (temperature - 32) * 5/9
            # Print the final result formatted to display exactly two decimal places
            print(f"\n{temperature} degrees Fahrenheit is equal to {result:.2f} degrees Celsius.")
            
    # Catch the specific exception if the user types letters instead of a number
    except ValueError:
        print("Invalid input. You must enter a number.")

# Script entry point: ensures the function only runs if the file is executed directly
if __name__ == "__main__":
    convert_temperature()