# Import the random module to be able to generate random numbers
import random

def simulate_dice_roll():
    # Start an infinite loop to keep the program running continuously
    while True:
        # Prompt the user to press Enter to roll or type exit
        action = input("\nPress Enter to roll a die (or type 'exit'): ").strip().lower()

        # Check if the user typed the word to terminate the program
        if action == "exit":
            # Print a message indicating that the program has ended
            print("Ending the simulator.")
            # Break the infinite loop to exit the function
            break

        # Generate a random integer between 1 and 6 (both inclusive)
        die = random.randint(1, 6)

        # Display the result of the roll to the user formatted with an f-string
        print(f"Roll result: {die}")

# Script entry point that ensures it is only executed directly
if __name__ == "__main__":
    simulate_dice_roll()