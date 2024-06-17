# PDF Conversion Tool

## Overview

This Python program allows users to convert PDF files into either text files or individual image files. The program uses the `fitz` module from the PyMuPDF library to handle the PDF conversion.

## Features

- **PDF to Text Conversion**: Converts the entire content of a PDF file into a text file.
- **PDF to Images Conversion**: Converts each page of a PDF file into separate image files (PNG format).

## Requirements

- Python 3.x
- PyMuPDF library

You can install PyMuPDF using pip:

```sh
pip install pymupdf
```

## How to Use
1. Run the Program: Execute the script to start the program.
2. Provide PDF Path: Enter the path to the PDF file when prompted.
3. Choose Conversion Type: Enter either text or images to specify the type of conversion.

## Example Usage

1. **Convert PDF to Text:**
```
Enter the path to the PDF file: example.pdf
Enter the conversion type ('text' or 'images'): text
PDF file converted to text and saved as 'example.txt'
```
2. **Convert PDF to Images:**
```
Enter the path to the PDF file: example.pdf
Enter the conversion type ('text' or 'images'): images
PDF file converted to images and saved in 'example_images'
```
## Error Handling
The program includes basic error handling to manage common issues:

1. **Non-existent PDF File:**

If the specified PDF file does not exist, the program will display the message: The specified PDF file does not exist.
Invalid Conversion Type:

2. **Invalid Conversion Type:**

If the user enters a conversion type other than text or images, the program will display the message: Invalid conversion type. Please choose 'text' or 'images'.