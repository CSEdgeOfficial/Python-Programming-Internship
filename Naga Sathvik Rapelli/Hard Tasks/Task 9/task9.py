from PIL import Image
import os

def convert_image(input_path, output_path, output_format):
    try:
        with Image.open(input_path) as img:
            img.save(output_path, format=output_format)
        print(f"Image converted successfully: {input_path} -> {output_path}")
    except Exception as e:
        print(f"Error converting image: {e}")

def main(input_folder, output_folder, output_format):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        if os.path.isfile(input_path) and any(filename.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.bmp', '.gif']):
            output_filename = os.path.splitext(filename)[0] + '.' + output_format.lower()
            output_path = os.path.join(output_folder, output_filename)

            convert_image(input_path, output_path, output_format)

input_folder = 'C:/Users/SATHVIK/OneDrive/Desktop'
output_folder = 'output_images'
output_format = 'PNG'
main(input_folder, output_folder, output_format)
