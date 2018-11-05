import PyPDF2
import os
import fnmatch
import sys

Files = os.listdir('.')
pdfs = []
for var in Files:
    if fnmatch.fnmatch(var,"*.pdf"):
        pdfs.append(var)

merger = PyPDF2.PdfFileMerger()

for pdf in pdfs:
    merger.append(open(pdf, 'rb'))

with open(sys.argv[1]+".pdf", 'wb') as fout:
    merger.write(fout)
