def manage_tasks():
    # Create an empty list in memory to store the user's tasks
    tasks = []
    
    # Start an infinite loop to keep the main menu running
    while True:
        # Display the available options to the user
        print("\nTo-Do List Menu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")
        
        # Prompt the user for their choice and strip whitespace
        choice = input("Choose an option (1-4): ").strip()
        
        # Check if the user chose option 1 (View tasks)
        if choice == "1":
            # Verify if the length of the list is zero (it is empty)
            if len(tasks) == 0:
                print("The task list is empty.")
            else:
                print("\nYour tasks:")
                # Iterate through the list using enumerate to get both index and value
                for i, task in enumerate(tasks):
                    # Print the index (adding 1 so it doesn't start at 0) and the task name
                    print(f"{i + 1}. {task}")
                    
        # Check if the user chose option 2 (Add task)
        elif choice == "2":
            # Prompt for the text of the new task
            new_task = input("Enter the new task: ").strip()
            # Add the entered text to the end of the list using the append method
            tasks.append(new_task)
            print("Task added successfully.")
            
        # Check if the user chose option 3 (Delete task)
        elif choice == "3":
            # Prevent attempting to delete if the list is already empty
            if len(tasks) == 0:
                print("There are no tasks to delete.")
                # Use continue to skip the rest of the code and show the menu again
                continue
                
            # Use try-except in case the user types letters instead of numbers
            try:
                # Prompt for the number of the task to delete
                index = int(input("Enter the number of the task to delete: "))
                
                # Validate that the entered number actually exists in the list boundaries
                if 1 <= index <= len(tasks):
                    # Remove the task using pop() by adjusting the index (subtracting 1)
                    deleted_task = tasks.pop(index - 1)
                    print(f"Task '{deleted_task}' deleted.")
                else:
                    # Show error if the number is too high or negative
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
                
        # Check if the user chose option 4 (Exit)
        elif choice == "4":
            print("Exiting the program.")
            # Break the infinite loop to terminate the script execution
            break
            
        # Handle any input that is not 1, 2, 3, or 4
        else:
            print("Invalid option. Please try again.")

# Script entry point
if __name__ == "__main__":
    manage_tasks()