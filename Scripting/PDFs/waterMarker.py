import PyPDF2

template = PyPDF2.PdfFileReader(open('dummy.pdf','rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf','rb'))
output = PyPDF2.PdfFileWriter()