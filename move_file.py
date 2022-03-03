import os 

class Move_file():

    def move_file(self,):

        try:
            os.chdir(r"C:\Users\Warley Souza\Music\Submittal")

            os.listdir()

            for file in os.listdir():
                if 'Submittal' in file:
                    os.rename(file, r"C:\Users\Warley Souza\Music\Submittal\File_PDF" + "\\" + file )
                
        except:
            print()
            print("\033[0;31;40m  The File does not exist. \033[m")
            print()
            

    def delete_file(self, ):

        try:
            os.chdir(r"C:\Users\Warley Souza\Music\Submittal\File_PDF")
            os.listdir()

            for file in os.listdir():
                if '.docx' in file:    
                    os.remove(file)
                    print('File delete!')
        except:
            pass


# test = Move_file()
# test.move_file()

# test.delete_file()