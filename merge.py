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


merge = ''

while merge != 'no':
    merge = input(('Deseja anexar algum arquivo? (Yes/No): '))
    teste = merge

    if teste == 'Yes' or teste == 'yes':
        test.merge_pdf()        
    else:
        print('Sem arquivo para anexar!')
print('Yes, the password is You may enter.')


# password = ''

# while password != 'password':
#     print('What is the password?')
#     password = input()

# print('Yes, the password is ' + password + '. You may enter.')

# test = Merge()
# test.merge_pdf()

