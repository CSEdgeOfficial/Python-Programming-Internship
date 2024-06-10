import PyPDF2
from PIL import Image
import os

def convert_pdf_to_text(pdf_path, text_output_path):
    """Converts a PDF file to text.

    Args:
        pdf_path (str): Path to the input PDF file.
        text_output_path (str): Path to save the converted text file.
    """
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            with open(text_output_path, 'w', encoding='utf-8') as text_file:
                # Iterate through each page of the PDF
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    # Extract text from the page and write it to the text file
                    text_file.write(page.extract_text())
        print(f"PDF converted to text successfully. Text file saved at {text_output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


def extract_images_from_pdf(pdf_path, image_output_folder):
    """Extracts images from a PDF file.

    Args:
        pdf_path (str): Path to the input PDF file.
        image_output_folder (str): Folder to save the extracted images.
    """
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            # Iterate through each page of the PDF
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                xObject = page.resources['XObject'].resolve()
                for obj in xObject:
                    if xObject[obj]['/Subtype'] == '/Image':
                        size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                        data = xObject[obj].get_data()
                        mode = ''
                        if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                            mode = "RGB"
                        else:
                            mode = "P"
                        if xObject[obj]['/Filter'] == '/FlateDecode':
                            img = Image.frombytes(mode, size, data)
                            img.save(os.path.join(image_output_folder, f"page{page_num+1}_{obj[1:]}.png"))
                        elif xObject[obj]['/Filter'] == '/DCTDecode':
                            img = open(os.path.join(image_output_folder, f"page{page_num+1}_{obj[1:]}.jpg"), "wb")
                            img.write(data)
                            img.close()
                        elif xObject[obj]['/Filter'] == '/JPXDecode':
                            img = open(os.path.join(image_output_folder, f"page{page_num+1}_{obj[1:]}.jp2"), "wb")
                            img.write(data)
                            img.close()
        print(f"Images extracted successfully. Saved in {image_output_folder}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Get input paths and output folder from user
    pdf_path = input("Enter the path to the PDF file: ")
    output_folder = input("Enter the output folder path: ")

    # Create the output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Choose conversion option
    choice = input("Choose an option:\n1. Convert PDF to text\n2. Extract images from PDF\nEnter your choice: ")

    if choice == '1':
        # Convert PDF to text
        text_output_path = os.path.join(output_folder, "converted_text.txt")
        convert_pdf_to_text(pdf_path, text_output_path)
    elif choice == '2':
        # Extract images from PDF
        image_output_folder = os.path.join(output_folder, "extracted_images")
        if not os.path.exists(image_output_folder):
            os.makedirs(image_output_folder)
        extract_images_from_pdf(pdf_path, image_output_folder)
    else:
        print("Invalid choice. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
