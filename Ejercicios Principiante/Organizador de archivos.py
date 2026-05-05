import os
import shutil

def organize_files():
    # 1. Prompt the user for the target directory path
    target_folder = input("Enter the exact path of the folder you want to organize: ").strip()
    
    # 2. Verify if the directory actually exists
    if not os.path.exists(target_folder):
        print("The specified path does not exist. Please check and try again.")
        return
        
    files_moved = 0
    
    # 3. Iterate through all items in the target directory
    for filename in os.listdir(target_folder):
        full_path = os.path.join(target_folder, filename)
        
        # 4. Ensure the current item is a file and not a subdirectory
        if os.path.isfile(full_path):
            # Split the filename and its extension (e.g., 'document', '.pdf')
            name, file_extension = os.path.splitext(filename)
            
            # Skip files with no extension
            if file_extension == "":
                continue
                
            # Remove the dot and convert to uppercase (e.g., '.pdf' -> 'PDF')
            folder_name = file_extension[1:].upper() 
            new_folder_path = os.path.join(target_folder, f"{folder_name}_Files")
            
            # 5. Create the destination folder if it doesn't exist
            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)
                
            # 6. Move the file to its new location
            destination_path = os.path.join(new_folder_path, filename)
            shutil.move(full_path, destination_path)
            files_moved += 1
            print(f"Moved: {filename} -> {folder_name}_Files/")
            
    print(f"\nDone! Successfully organized {files_moved} files.")

if __name__ == "__main__":
    organize_files()