import PyPDF2
import os

def merge_pdfs(input_paths, output_path):
    pdf_writer = PyPDF2.PdfWriter()
    
    for path in input_paths:
        pdf_reader = PyPDF2.PdfReader(path)
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)
    
    with open(output_path, 'wb') as out_pdf:
        pdf_writer.write(out_pdf)

def split_pdf(input_path, output_folder):
    pdf_reader = PyPDF2.PdfReader(input_path)
    
    for i, page in enumerate(pdf_reader.pages):
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(page)
        
        output_path = os.path.join(output_folder, f'page_{i+1}.pdf')
        with open(output_path, 'wb') as out_pdf:
            pdf_writer.write(out_pdf)

# Example usage:
# Merge PDFs
input_files = ['file1.pdf', 'file2.pdf']
output_merged = 'merged.pdf'
merge_pdfs(input_files, output_merged)

# Split PDF
input_pdf = 'large_file.pdf'
output_folder = 'split_pages'
split_pdf(input_pdf, output_folder)
