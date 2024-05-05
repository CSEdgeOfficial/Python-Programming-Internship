from PIL import Image 
import os

def convert_image(input_path, output_path, output_format):

    try:
        img = Image.open(input_path)
    except IOError:
        print("Unable to open image file:", input_path)
        return

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    try:
        img.save(output_path, format=output_format)
        print("Image converted successfully!")
    except Exception as e:
        print("Failed to convert image:", e)

if __name__ == "__main__":
    input_path = input("Enter the path to the input image: ")
    output_path = input("Enter the path for the output image: ")
    output_format = input("Enter the desired output format (JPEG, PNG, BMP, GIF): ").upper()

    if output_format not in ["JPEG", "PNG", "BMP", "GIF"]:
        print("Invalid output format!")
    else:
        convert_image(input_path, output_path, output_format)
