import os 

class Move_file():

    def move_file(self,):

        try:
             os.chdir(r"C:\Users\Warley Souza\Music\Submittal")

             os.listdir()

             for file in os.listdir():
                 if 'Submittal' in file:
                     os.rename(file, r"C:\Users\Warley Souza\Music\Submittal\Submitall" + "\\" + file)
        except:
            pass

# test = Move_file()
# test.move_file()