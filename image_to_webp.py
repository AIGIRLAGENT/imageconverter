from PIL import Image, UnidentifiedImageError # Added UnidentifiedImageError for specific exception
import os
from pathlib import Path

def convert_images_to_webp(source_folder_path, destination_folder_path):
    """
    Scans a source folder for PNG, JPG, JPEG images, converts them to WebP
    if a WebP version doesn't already exist in the destination,
    and saves them in the destination folder.
    """
    print(f"\nStarting image conversion process...")
    print(f"Source folder: {source_folder_path}")
    print(f"Destination folder: {destination_folder_path}")

    source_path_obj = Path(source_folder_path) # For easier path joining later
    destination_path_obj = Path(destination_folder_path)

    # Ensure the destination folder exists, create it if it doesn't
    if not destination_path_obj.exists():
        try:
            print(f"Destination folder '{destination_folder_path}' does not exist. Creating it...")
            destination_path_obj.mkdir(parents=True, exist_ok=True)
            print(f"Successfully created destination folder: {destination_folder_path}")
        except Exception as e:
            print(f"Error: Could not create destination folder '{destination_folder_path}'. {e}")
            return
    elif not destination_path_obj.is_dir():
        print(f"Error: The destination path '{destination_folder_path}' exists but is not a folder.")
        return

    supported_extensions = ('.png', '.jpg', '.jpeg')
    images_found = 0
    images_converted = 0
    images_skipped_exists = 0 # Counter for skipped images
    images_failed = 0

    print(f"\nScanning source folder '{source_folder_path}' for images ({', '.join(supported_extensions)})...")

    for filename in os.listdir(source_folder_path):
        # Construct full path for the source file
        current_source_file_path = source_path_obj / filename

        if current_source_file_path.is_file() and current_source_file_path.suffix.lower() in supported_extensions:
            images_found += 1
            base_filename = current_source_file_path.stem # Gets filename without extension
            webp_filename = base_filename + ".webp"
            destination_webp_file_path = destination_path_obj / webp_filename

            print(f"\nFound image: {filename}")

            # --- CHECK IF WEBP ALREADY EXISTS ---
            if destination_webp_file_path.exists():
                print(f"  Skipping '{filename}': WebP version '{webp_filename}' already exists in the destination folder.")
                images_skipped_exists += 1
                continue # Move to the next file
            # --- END CHECK ---

            try:
                print(f"  Attempting to convert '{filename}' to '{webp_filename}'...")
                img = Image.open(current_source_file_path)

                if current_source_file_path.suffix.lower() == '.png':
                    img.save(destination_webp_file_path, 'webp', lossless=True, quality=100)
                    print(f"  Successfully converted '{filename}' to '{webp_filename}' (lossless) in destination folder.")
                else: # For .jpg, .jpeg
                    img.save(destination_webp_file_path, 'webp', quality=85)
                    print(f"  Successfully converted '{filename}' to '{webp_filename}' (quality 85) in destination folder.")
                
                images_converted += 1

            except FileNotFoundError: # Should be rare if os.listdir works
                print(f"  Error: Source file '{filename}' not found during conversion attempt.")
                images_failed += 1
            except UnidentifiedImageError:
                 print(f"  Error: Cannot identify image file '{filename}'. It might be corrupted or not a valid image format recognized by Pillow.")
                 images_failed += 1
            except Exception as e:
                print(f"  Error converting '{filename}': {e}")
                images_failed += 1
        elif current_source_file_path.is_file(): # It's a file but not a supported image
            print(f"Skipping non-image file: {filename}")


    print("\n--- Conversion Summary ---")
    if images_found == 0:
        print("No images with supported extensions found in the source folder.")
    else:
        print(f"Total images with supported extensions found: {images_found}")
        print(f"Successfully converted: {images_converted}")
        print(f"Skipped (WebP already existed): {images_skipped_exists}") # New summary line
        print(f"Failed to convert: {images_failed}")
    print("--------------------------")

if __name__ == "__main__":
    print("--- WebP Image Converter ---")

    while True:
        source_folder_input = input("Enter the path to the SOURCE folder (e.g., C:\\Users\\YourName\\Pictures): ").strip()
        # Remove surrounding quotes if present (common when pasting paths)
        source_folder_input = source_folder_input.strip('"').strip("'")
        source_folder_path_obj = Path(source_folder_input)
        if source_folder_path_obj.exists() and source_folder_path_obj.is_dir():
            break
        else:
            print("Invalid source folder path. Please ensure the folder exists and try again.")

    while True:
        destination_folder_input = input("Enter the path to the DESTINATION folder (can be same as source): ").strip()
        # Remove surrounding quotes
        destination_folder_input = destination_folder_input.strip('"').strip("'")
        destination_folder_path_obj_check = Path(destination_folder_input)
        if destination_folder_path_obj_check.exists() and not destination_folder_path_obj_check.is_dir():
            print(f"Error: The destination path '{destination_folder_input}' exists but is not a directory. Please choose a different path or remove the file.")
        else:
            # Allow non-existent paths as they will be created, or existing directories
            break

    convert_images_to_webp(str(source_folder_path_obj), destination_folder_input)

    print("\nScript finished.")