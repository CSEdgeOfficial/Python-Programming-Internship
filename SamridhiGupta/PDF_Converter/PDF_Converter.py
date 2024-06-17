import fitz  
import os

def convert_pdf_to_text(pdf_path, output_path):
    """
    Convert a PDF file to a text file.
    """
    with fitz.open(pdf_path) as pdf_file:
        text = ""
        for page_index in range(len(pdf_file)):
            page = pdf_file[page_index]
            text += page.get_text()

    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(text)

    print(f"PDF file converted to text and saved as '{output_path}'")

def convert_pdf_to_images(pdf_path, output_folder):
    """
    Convert a PDF file to individual image files.
    """
    with fitz.open(pdf_path) as pdf_file:
        for page_index in range(len(pdf_file)):
            page = pdf_file[page_index]
            image = page.get_pixmap()
            image_path = os.path.join(output_folder, f"page_{page_index + 1}.png")
            image.save(image_path)

    print(f"PDF file converted to images and saved in '{output_folder}'")

def main():
    pdf_path = input("Enter the path to the PDF file: ")
    conversion_type = input("Enter the conversion type ('text' or 'images'): ")

    if not os.path.exists(pdf_path):
        print("The specified PDF file does not exist.")
        return

    if conversion_type == "text":
        output_path = os.path.splitext(pdf_path)[0] + ".txt"
        convert_pdf_to_text(pdf_path, output_path)
    elif conversion_type == "images":
        output_folder = os.path.splitext(pdf_path)[0] + "_images"
        os.makedirs(output_folder, exist_ok=True)
        convert_pdf_to_images(pdf_path, output_folder)
    else:
        print("Invalid conversion type. Please choose 'text' or 'images'.")

if __name__ == "__main__":
    main()

    