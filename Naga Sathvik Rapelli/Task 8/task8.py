import PyPDF2
import os

def merge_pdfs(input_folder, output_path):
    pdf_merger = PyPDF2.PdfWriter()

    input_paths = [os.path.join(input_folder, filename) for filename in os.listdir(input_folder) if filename.endswith('.pdf')]

    for path in input_paths:
        pdf_reader = PyPDF2.PdfReader(path)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_merger.add_page(page)

    with open(output_path, 'wb') as output_pdf:
        pdf_merger.write(output_pdf)

input_folder = 'C:/Users/SATHVIK/OneDrive/Desktop/DESKTOP/APP_POINTS'
output_path = 'C:/Users/SATHVIK/OneDrive/Desktop/merged_pdf.pdf'

merge_pdfs(input_folder, output_path)
print("PDF files merged successfully and saved as 'merged_pdf.pdf' on your desktop.")
