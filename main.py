from information import Information
from salve_file import Save_File
from move_file import Move_file
from send_email import Send_Email

print()
print("\033[4;36;40m### CRIANDO SUBMITTAL ###\033[m")


save = Save_File()
get_save = save.data_information()

# move = Move_file()
# move.move_file()


send = Send_Email()
send.send_email()


# question = str(input("Deseja deletar o arquivo Word? (Yes or No)"))

# if question == 'Yes' or 'yes':
#     test.delete_file()
# else:
#     print("Nenhum arquivo deletado")