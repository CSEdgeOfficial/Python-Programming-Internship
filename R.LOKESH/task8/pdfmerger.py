import PyPDF2

def merge_pdfs(input_files, output_file):
    merger = PyPDF2.PdfFileMerger()
    for input_file in input_files:
        merger.append(input_file)
    merger.write(output_file)
    merger.close()
    print(f"PDF files merged successfully into {output_file}")

def split_pdf(input_file, output_prefix):
    input_pdf = PyPDF2.PdfFileReader(input_file)
    for page_number in range(input_pdf.numPages):
        output_pdf = PyPDF2.PdfFileWriter()
        output_pdf.addPage(input_pdf.getPage(page_number))
        output_filename = f"{output_prefix}_{page_number + 1}.pdf"
        with open(output_filename, "wb") as output_file:
            output_pdf.write(output_file)
        print(f"Page {page_number + 1} split into {output_filename}")

def main():
    # Merge PDF files
    input_files = ["input1.pdf", "input2.pdf", "input3.pdf"]
    merge_output_file = "merged_output.pdf"
    merge_pdfs(input_files, merge_output_file)
    
    # Split PDF file
    input_file = "input.pdf"
    split_output_prefix = "split_output"
    split_pdf(input_file, split_output_prefix)

if __name__ == "__main__":
    main()
