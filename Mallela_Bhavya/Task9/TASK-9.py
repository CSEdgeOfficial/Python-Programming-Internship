from PIL import Image
import os

def convert_image(input_path, output_path, output_format):
    try:
        # Open the image
        with Image.open(input_path) as img:
            # Check if the image has an alpha channel and convert it to RGB if necessary
            if output_format == 'JPEG' and img.mode == 'RGBA':
                img = img.convert('RGB')
            
            # Convert and save the image to the desired format
            img.save(output_path, format=output_format)
            print(f"Image converted successfully to {output_format} format.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    input_path = input("Enter the path to the input image: ")
    output_format = input("Enter the desired output format (e.g., JPEG, PNG, BMP, GIF): ").upper()

    # Validate output format
    if output_format not in ['JPEG', 'PNG', 'BMP', 'GIF']:
        print("Invalid output format. Please choose from JPEG, PNG, BMP, or GIF.")
        return

    # Extract the file name and extension
    file_name, file_extension = os.path.splitext(input_path)

    # Set the output path
    output_path = f"{file_name}_converted.{output_format.lower()}"

    # Convert the image
    convert_image(input_path, output_path, output_format)

if __name__ == "__main__":
    main()
