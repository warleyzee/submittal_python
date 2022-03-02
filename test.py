
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


import PyPDF2 
import os
from time import sleep

attachment = ''
mergeFile = PyPDF2.PdfFileMerger()
lista_file = []


while attachment != 'no':
    print()
    attachment =str(input("\033[2;36;40m Desejar anexar algum arquivo? (yes/no): \033[m"))
    msg = attachment

    if msg == 'yes':
        file = str(input("\033[1;34;40mNome do arquivo para unir: \033[m"))
        print()

        try:
           lista_file.append(file)

        except:
            print("Arquivo nao encontrado")

for item in lista_file:
    mergeFile.append(PyPDF2.PdfFileReader(f'{item}.pdf', 'rb'))

print("\033[1;32;40m  Anexando arquivos \033[m")
sleep(2)    
name_submittal = str(input("\033[1;34;40mComo deseja salvar o arquivo: \033[m"))

mergeFile.write(f'{name_submittal}.pdf')
print()
sleep(2)
print("\033[1;32;40m  Arquivos anexado! \033[m")























































