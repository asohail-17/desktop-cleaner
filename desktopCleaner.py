import os
import shutil

def organize_desktop():
    # Define the path to the desktop
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    
    # Check if the desktop path exists
    if not os.path.isdir(desktop_path):
        print(f"The desktop path '{desktop_path}' does not exist.")
        return

    # Iterate over all files and directories on the desktop
    for item in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, item)
        
        # Skip directories
        if os.path.isdir(item_path):
            continue
        
        # Get the file extension
        file_extension = os.path.splitext(item)[1].lower()
        
        # If there's no extension, skip the file
        if not file_extension:
            continue
        
        # Define the target directory based on file extension
        target_dir = os.path.join(desktop_path, file_extension.lstrip('.').upper())
        
        # Create the target directory if it doesn't exist
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        
        # Define the target path
        target_path = os.path.join(target_dir, item)
        
        # Move the file
        shutil.move(item_path, target_path)
        print(f"Moved '{item}' to '{target_dir}'")

if __name__ == "__main__":
    organize_desktop()
