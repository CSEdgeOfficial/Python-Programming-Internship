import os
from PIL import Image

# Function to process the images
def process_images(input_folder, output_folder, files):
    images_details = []
    for file in files:
        file_path = os.path.join(input_folder, file)
        with Image.open(file_path) as img:
            # Details
            details = {
                'filename': file,
                'format': img.format,
                'mode': img.mode,
                'size': img.size
            }
        
        images_details.append(details)

        # Convert image format to PNG
        new_file_name = os.path.splitext(file)[0] + '.png'
        new_file_path = os.path.join(output_folder, new_file_name)
        img.save(new_file_path, 'PNG')
    
    return images_details

def main():
    # Path to the input folder
    input_folder = 'input'
    output_folder = 'output'

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # List all files in the input folder
    files = os.listdir(input_folder)

    # Process the images and get their details
    try:
        image_details = process_images(input_folder, output_folder, files)

        # Print the file details.
        for detail in image_details:
            print(detail)

        # Successful Conversion of Images
        print("Images Converted Successfully!")

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()