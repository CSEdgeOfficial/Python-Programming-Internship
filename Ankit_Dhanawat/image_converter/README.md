# Image Converter Documentation

## Overview

This Python script is designed to convert images from one format to another using the PIL (Python Imaging Library) module.

## Usage

To use this script, follow these steps:

1. Ensure you have Python installed on your system.
2. Install the required Python modules using pip:
   ```
   pip install pillow
   ```
3. Run the script using Python:
   ```
   python image_converter.py
   ```

## Functions

### `convert_image(input_path, output_path, output_format)`

This function converts an input image to the specified output format and saves it to the output path.

- `input_path` (string): The file path of the input image.
- `output_path` (string): The file path where the converted image will be saved.
- `output_format` (string): The desired output format for the image (e.g., JPEG, PNG, BMP, GIF).

## Error Handling

- If the input image file cannot be opened, an IOError is raised, and an error message is displayed.
- If the conversion process fails, an exception is caught, and an error message is displayed.

## Example

```python
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
```

## Dependencies

- **PIL (Python Imaging Library)**: This script requires the PIL module to manipulate images. You can install it using pip:

   ```
   pip install pillow
   ```