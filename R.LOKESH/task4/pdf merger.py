import PyPDF2

def split_pdf(input_pdf, output_path, page_ranges):
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        for i, page_range in enumerate(page_ranges):
            start_page, end_page = page_range
            pdf_writer = PyPDF2.PdfFileWriter()
            for page_num in range(start_page - 1, end_page):
                pdf_writer.addPage(pdf_reader.getPage(page_num))
            output_pdf = f"{output_path}/split_{i + 1}.pdf"
            with open(output_pdf, 'wb') as output_file:
                pdf_writer.write(output_file)

def merge_pdfs(input_pdfs, output_pdf):
    pdf_writer = PyPDF2.PdfFileWriter()
    for pdf in input_pdfs:
        with open(pdf, 'rb') as file:
            pdf_reader = PyPDF2.PdfFileReader(file)
            for page_num in range(pdf_reader.numPages):
                pdf_writer.addPage(pdf_reader.getPage(page_num))
    with open(output_pdf, 'wb') as output_file:
        pdf_writer.write(output_file)

# Example usage for splitting
input_pdf = 'input.pdf'
output_path = 'output'
page_ranges = [(1, 3), (4, 6)]  # List of tuples representing page ranges
split_pdf(input_pdf, output_path, page_ranges)

# Example usage for merging
input_pdfs = ['input1.pdf', 'input2.pdf']
output_pdf = 'merged_output.pdf'
merge_pdfs(input_pdfs, output_pdf)
