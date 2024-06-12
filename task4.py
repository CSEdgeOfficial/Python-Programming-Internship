from PyPDF2 import PdfFileReader, PdfFileWriter

def split_pdf(input_pdf, output_folder):
    pdf_reader = PdfFileReader(input_pdf)
    total_pages = pdf_reader.numPages

    for page_num in range(total_pages):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf_reader.getPage(page_num))

        output_file = f"{output_folder}/page_{page_num + 1}.pdf"
        with open(output_file, "wb") as output_pdf:
            pdf_writer.write(output_pdf)

        print(f"Page {page_num + 1} saved as {output_file}")


