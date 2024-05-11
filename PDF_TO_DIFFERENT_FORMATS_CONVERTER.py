import PyPDF2
from pdf2image import convert_from_path
from pdf2docx import parse
print("1.PDF-TO-TXT-FILE\n\n\n2.PDF-IMAGE\n\n\n3.PDF-DOCUMENT\n\n\n")
ch=int(input("ENTER YOUR CHOICE:"))
if ch==1:
    pdffileobj=open('filename.pdf','rb')
    pdfreader=PyPDF2.PdfFileReader(pdffileobj)
    x=pdfreader.numPages
    pageobj=pdfreader.getPage(x+1)
    text=pageobj.extractText()
    file1=open("file path","a")
    file1.writelines(text)
elif ch==2:
    pdf_images = convert_from_path('pdf_name.pdf')
    for idx in range(len(pdf_images)):
        pdf_images[idx].save('pdf_page_'+ str(idx+1) +'.png', 'PNG')
    print("Successfully converted PDF to images")
elif ch==3:
    pdf_file = r"pdf file_path name.pdf"
    docx_file = r"document_path_name.docx"
    parse(pdf_file, docx_file)
else:
    exit()