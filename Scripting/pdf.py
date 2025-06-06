import PyPDF2
with open('./PDFs/dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)  # Print the number of pages in the PDF
    page = reader.getPage(0)  # Get the first page
    page.rotateCounterClockwise(90)
    writer =  PyPDF2.PdfFileWriter()
    writer.addPage(page)  # Add the rotated page to the writer
    with open('til.pdf', 'wb') as new_file:
        writer.write(new_file)
