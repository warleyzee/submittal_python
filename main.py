from heapq import merge
from information import Information
from salve_file import Save_File
from move_file import Move_file
from send_email import Send_Email
from merge import Merge

print()
print("\033[4;36;40m### CRIANDO SUBMITTAL ###\033[m")

input("Enter pra comecar")
save = Save_File()
get_save = save.data_information()

input("Digite algo movere")
move = Move_file()
move.move_file()

input("Digite algo movere")
merge = Merge()
merge.merge_pdf()

send_to_email = input("Desejar enviar um e-mail?(yes/no): ")

if send_to_email == 'yes':
    send = Send_Email()
    send.send_email()
else:
    print("Fim")

input("Digite algo para fechar")

