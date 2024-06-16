
import os
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

def merge_pdfs(pdf_list, output_path):
    merger = PdfMerger()

    for pdf in pdf_list:
        if os.path.exists(pdf):
            merger.append(pdf)
        else:
            print(f"File not found: {pdf}")

    with open(output_path, 'wb') as output_file:
        merger.write(output_file)

    print(f'Merged PDF saved as {output_path}')

def split_pdf(input_path, output_folder):
    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        return

    with open(input_path, 'rb') as input_file:
        reader = PdfReader(input_file)
        num_pages = len(reader.pages)

        for page_num in range(num_pages):
            writer = PdfWriter()
            writer.add_page(reader.pages[page_num])

            output_path = os.path.join(output_folder, f'page_{page_num + 1}.pdf')
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)

            print(f'Saved {output_path}')

def main():
    print("PDF Merger/Splitter")
    print("1. Merge PDFs")
    print("2. Split PDF")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        pdf_files = input("Enter the PDF files to merge (separated by commas): ").split(',')
        pdf_files = [pdf.strip() for pdf in pdf_files]  # Strip whitespace
        output_path = input("Enter the output path for the merged PDF: ")
        merge_pdfs(pdf_files, output_path)
    elif choice == '2':
        input_path = input("Enter the PDF file to split: ")
        output_folder = input("Enter the output folder for the split PDFs: ")
        os.makedirs(output_folder, exist_ok=True)
        split_pdf(input_path, output_folder)
    elif choice == '3':
        print("Exiting.")
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
