# Import the time module to use the sleep function and pause execution
import time

def pomodoro_timer():
    # Start a try-except block to handle errors if the user enters text
    try:
        # Prompt the user for minutes and convert the input to an integer
        minutes = int(input("Enter the minutes for the Pomodoro timer (e.g., 25): "))
        
        # Convert the total minutes into seconds by multiplying by 60
        total_seconds = minutes * 60
        
        # Display a message indicating that the timer has started
        print("\nStarting timer...")
        
        # Start a loop that will run as long as there are seconds left in the countdown
        while total_seconds > 0:
            # Use divmod to get the remaining minutes and seconds (quotient and remainder of dividing by 60)
            mins, secs = divmod(total_seconds, 60)
            
            # Format the time to always display two digits (e.g., 05:09) using :02d
            time_format = f"{mins:02d}:{secs:02d}"
            
            # Print the time, overwriting the current line in the console thanks to end="\r"
            print(time_format, end="\r")
            
            # Pause the execution of the program for exactly 1 second
            time.sleep(1)
            
            # Subtract one second from the total before the next loop iteration
            total_seconds -= 1
            
        # Once the loop ends (reaches 0), print the final message with an initial newline
        print("\nTime is up! It is time to take a break.")
        
    # Catch the error if the user does not enter a valid integer
    except ValueError:
        print("Please enter a valid integer.")

# Script entry point
if __name__ == "__main__":
    pomodoro_timer()