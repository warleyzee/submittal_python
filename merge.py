import PyPDF2 
import os

# from PyPDF2 import PdfFileMerger

# pdfs = ['Rawlplug.pdf', 'Rawlplug_r.pdf']

# merger = PdfFileManager()

# for pdf in pdfs:
#     merger.append(pdf)

# merger.write("Submittal #138 - Fixing Bolt.pdf")
# merger.close()


class Merge():

    def merge_pdf(self, ):

        file = str(input("Nome do arquivo para unir: "))
        file2 = str(input("Nome do arquivo para unir: "))

        mergeFile = PyPDF2.PdfFileMerger()

        mergeFile.append(PyPDF2.PdfFileReader('Submittal.pdf', 'rb'))

        mergeFile.append(PyPDF2.PdfFileReader(f'{file}.pdf', 'rb'))

        mergeFile.append(PyPDF2.PdfFileReader(f'{file2}.pdf', 'rb'))

        mergeFile.write("Submittal #138.pdf")

test = Merge()
test.merge_pdf()

