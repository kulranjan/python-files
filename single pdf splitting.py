import os
from PyPDF2 import PdfFileReader, PdfFileWriter

#pdf_file_path = r"C:\Users\kulra\Downloads\Documents\35238 letters.pdf"


pdf_file_path = input("Input file path : ")

assert os.path.exists(pdf_file_path), "I did not find the file at, "+str(pdf_file_path)
f = open(pdf_file_path,'r+')
print("Hooray we found your file!")

file_base_name = pdf_file_path.replace('.pdf', '')
#output_folder_path = os.path.join(os.getcwd(), 'Output')
output_folder_path = input("Output file path : ")

print(output_folder_path)

pdf = PdfFileReader(pdf_file_path)

for page_num in range(pdf.numPages):
    pdfWriter = PdfFileWriter()
    a=pdfWriter.addPage(pdf.getPage(page_num))


    with open(os.path.join(output_folder_path, '{0}_Page{1}.pdf'.format(file_base_name, page_num+1)), 'wb') as f:
        pdfWriter.write(f)
        f.close()

print(output_folder_path)