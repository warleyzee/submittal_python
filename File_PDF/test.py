
# print()


# print("\033[3;30;39m### CRIANDO SUBMITTAL ###\033[m")
# print("\033[3;35;40m### CRIANDO SUBMITTAL ###\033[m")
# print("\033[0;31;40m  Red0 \033[m")
# print("\033[1;32;40m  Red1 \033[m")
# print("\033[2;33;40m  Red2 \033[m")
# print("\033[2;34;40m  Red3 \033[m")
# print("\033[2;35;40m  Red4 \033[m")
# print("\033[2;36;40m  Red5 \033[m")
# print("\033[2;37;40m  Red6 \033[m")
# print("\033[2;38;40m  Red7 \033[m")
# print("\033[2;39;40m  Red8 \033[m")


# import PyPDF2 
# import os
# from time import sleep

# attachment = ''
# mergeFile = PyPDF2.PdfFileMerger()
# self.lista_file = []


# while attachment != 'no':
#     print()
#     attachment =str(input("\033[2;36;40m Desejar anexar algum arquivo? (yes/no): \033[m"))
#     msg = attachment

#     if msg == 'yes':
#         file = str(input("\033[1;34;40mNome do arquivo para unir: \033[m"))
#         print()

#         try:
#            self.lista_file.append(file)

#         except:
#             print("Arquivo nao encontrado")

# for item in self.lista_file:
#     mergeFile.append(PyPDF2.PdfFileReader(f'{item}.pdf', 'rb'))

# print("\033[1;32;40m  Anexando arquivos \033[m")
# sleep(2)    
# name_submittal = str(input("\033[1;34;40mComo deseja salvar o arquivo: \033[m"))

# mergeFile.write(f'{name_submittal}.pdf')
# print()
# sleep(2)
# print("\033[1;32;40m  Arquivos anexado! \033[m")



# import PyPDF2 
# import os
# from time import sleep
# import os

# class Merge():

#     def merge_pdf(self, ):

#         attachment = ''
#         mergeFile = PyPDF2.PdfFileMerger()
#         self.lista_file = []
#         os.chdir(r"C:\Users\Warley Souza\Music\Submittal\File_PDF")
#         os.listdir()
        
#         for file in os.listdir():
#             str_pdf = file[-3:]

#             if str_pdf == "pdf":
#                 self.lista_file.append(file)

#                 while attachment != 'no':
#                     print()
#                     attachment =str(input("\033[2;36;40m Desejar anexar algum arquivo? (yes/no): \033[m"))
#                     msg = attachment

#                     if msg == 'yes':
#                         for file in os.listdir():
#                             str_pdf = file[-3:]

#                             if str_pdf == "pdf":
#                                 try:
#                                     self.lista_file.append(file)
#                                 except:
#                                     print("Sem Arquivo para anexar")

#                             # file = str(input("\033[1;34;40mNome do arquivo para unir: \033[m"))
#                             # print()

                            
#                                 # self.lista_file.append(file)

#                             for item in self.lista_file:
#                                 mergeFile.append(PyPDF2.PdfFileReader(f'{item}', 'rb'))
#                                 print()
#                                 print("\033[1;32;40m  Anexando arquivos \033[m")
#                                 sleep(2)    
#                                 name_submittal = str(input("\033[1;34;40mComo deseja salvar o arquivo: \033[m"))
#                                 print()
#                                 mergeFile.write(f'{name_submittal}.pdf')
#                                 print()
#                                 sleep(2)
#                                 print("\033[1;32;40m  Arquivos anexado! \033[m")
        
#                             else:
#                                 print("Sem arquivo para anexar!")
        


            # attachment = ''
            # mergeFile = PyPDF2.PdfFileMerger()
            # self.lista_file = []


            # while attachment != 'no':
            #     print()
            #     attachment =str(input("\033[2;36;40m Desejar anexar algum arquivo? (yes/no): \033[m"))
            #     msg = attachment

            #     if msg == 'yes':
            #         file = str(input("\033[1;34;40mNome do arquivo para unir: \033[m"))
            #         print()

            #         try:
            #             self.lista_file.append(file)

            #             for item in self.lista_file:
            #                 mergeFile.append(PyPDF2.PdfFileReader(f'{item}.pdf', 'rb'))
            #                 print()
            #                 print("\033[1;32;40m  Anexando arquivos \033[m")
            #                 sleep(2)    
            #                 name_submittal = str(input("\033[1;34;40mComo deseja salvar o arquivo: \033[m"))
            #                 print()
            #                 mergeFile.write(f'{name_submittal}.pdf')
            #                 print()
            #                 sleep(2)
            #                 print("\033[1;32;40m  Arquivos anexado! \033[m")

            #         except:
            #             print("Arquivo nao encontrado")
            #     else:
            #         print("Sem arquivo para anexar!")

            # for item in self.lista_file:
            #     mergeFile.append(PyPDF2.PdfFileReader(f'{item}.pdf', 'rb'))
            # print()
            # print("\033[1;32;40m  Anexando arquivos \033[m")
            # sleep(2)    
            # name_submittal = str(input("\033[1;34;40mComo deseja salvar o arquivo: \033[m"))
            # print()
            # mergeFile.write(f'{name_submittal}.pdf')
            # print()
            # sleep(2)
            # print("\033[1;32;40m  Arquivos anexado! \033[m")

# test = Merge()
# test.merge_pdf()




















