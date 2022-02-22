import PyPDF2 
import os

# from PyPDF2 import PdfFileMerger

# pdfs = ['Rawlplug.pdf', 'Rawlplug_r.pdf']

# merger = PdfFileManager()

# for pdf in pdfs:
#     merger.append(pdf)

# merger.write("Submittal #138 - Fixing Bolt.pdf")
# merger.close()



# mergeFile = PyPDF2.PdfFileMerger()


# mergeFile.append(PyPDF2.PdfFileReader('Submittal.pdf', 'rb'))

# mergeFile.append(PyPDF2.PdfFileReader('Rawlplug.pdf', 'rb'))

# mergeFile.append(PyPDF2.PdfFileReader('Rawlplug_r.pdf', 'rb'))

# mergeFile.write("Submittal #138.pdf")

pdfs_dir = r"C:"
bg_filename = pdfs_dir + '\Submittal.pdf'
fg_filename = pdfs_dir + '\Submittal.pdf'

with open(bg_filename, 'rb') as bg_file, open(fg_filename, 'rb') as fg_file:
	bg_page = PyPDF2.PdfFileReader(bg_file).getPage(0)
	pdf_out = PyPDF2.PdfFileWriter()
	for page in PyPDF2.PdfFileReader(fg_file).pages:
		if page.extractText():  # Do not copy pages that have no text
			page.mergePage(bg_page)
			pdf_out.addPage(page)
	if pdf_out.getNumPages():
		with open('New.pdf', 'wb') as out_file:
			# Caution: All three files MUST be open when write() is called
			pdf_out.write(out_file)


