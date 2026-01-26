import os

def file_manager():
    # Ask user for folder path
    folder_path = input("Enter the folder path to display its files: ")

    # Check if folder exists
    if not os.path.exists(folder_path):
        print("Folder does not exist! Please check the path.")
        return

    # List files and folders
    files = os.listdir(folder_path)
    if not files:
        print("The folder is empty.")
    else:
        print(f"\nFiles and folders in: {folder_path}")
        for f in files:
            if os.path.isfile(os.path.join(folder_path, f)):
                print(f"File: {f}")
            else:
                print(f"Folder: {f}")

# Run the program
file_manager()