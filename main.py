from information import Information
from salve_file import Save_File
from move_file import Move_file
from send_email import Send_Email

print()
print("\033[1;36;40m\033[m \033[1;32;40m\033[m \033[1;36;40m### CRIANDO SUBMITTAL ###\033[m")
info = Information().write_information()

# Information = info.write_information()


save = Save_File()
get_save = save.data_information()

move = Save_File()
move.move_file()


send = Send_Email()
send.send_email()