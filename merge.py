import PyPDF2 
import os
from time import sleep
import os

class Merge():

    def merge_pdf(self, ):

        attachment = ''
        mergeFile = PyPDF2.PdfFileMerger()
        self.lista_file = []
        os.chdir(r"C:\Users\Warley Souza\Music\Submittal\File_PDF")
        os.listdir()
        
        for file in os.listdir():
            str_pdf = file[-3:]

            if str_pdf == "pdf":
                self.lista_file.append(file)

                while attachment != 'no':
                    print()
                    attachment =str(input("\033[2;36;40m Desejar anexar algum arquivo? (yes/no): \033[m"))
                    msg = attachment

                    if msg == 'yes':
                        for file in os.listdir():
                            str_pdf = file[-3:]

                            if str_pdf == "pdf":
                                try:
                                    self.lista_file.append(file)
                                except:
                                    print("Sem Arquivo para anexar")

                            # file = str(input("\033[1;34;40mNome do arquivo para unir: \033[m"))
                            # print()

                            
                                # self.lista_file.append(file)

                    for item in self.lista_file:
                        mergeFile.append(PyPDF2.PdfFileReader(f'{item}', 'rb'))
                        print()
                        sleep(2)    
                        print()
                        mergeFile.write(f'{name_submittal}.pdf')
                        print()
                        sleep(2)
                    else:
                        print("Sem arquivo para anexar!")

                name_submittal = str(input("\033[1;34;40mComo deseja salvar o arquivo: \033[m"))
                print("\033[1;32;40m  Arquivos anexado! \033[m")


test = Merge()
test.merge_pdf()

