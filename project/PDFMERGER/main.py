import os
from PyPDF2 import PdfWriter

os.chdir(os.path.dirname(__file__))
merger = PdfWriter()

pdfs=[]
n = int(input("How many pdf do you want to merge?\n"))

for i in range (0, n):
    name= input(f"Enter the name of pdf {i + 1}: ")
    pdfs.append(name)

for pdf in pdfs:
    try:
        merger.append(pdf)
    except FileNotFoundError:
        print(f"File {pdf} not found. Please check the filename and try again.")
        exit()

merger.write("merged-pdf.pdf")
merger.close()
