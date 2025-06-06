import PyPDF2
import sys

inputs = sys.argv[1:] # Grab all arguments except the 1st one (the script name)

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write("combined.pdf")

pdf_combiner(inputs)
