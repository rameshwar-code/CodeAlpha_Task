import os
import shutil

def move_images():
    # You can change these paths to folders on your computer
    source_folder = "images_source"
    destination_folder = "images_destination"

    # Create destination if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    if os.path.exists(source_folder):
        files = os.listdir(source_folder)
        for file in files:
            if file.endswith(".jpg"):
                shutil.move(os.path.join(source_folder, file), destination_folder)
                print(f"Moved: {file}")
        print("Automation Complete.")
    else:
        print("Source folder not found. Please create 'images_source' folder.")

move_images()
