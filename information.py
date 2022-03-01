from datetime import date



class Information(): 
    def date_current(self,):
        
        data = date.today()
        month = data.month
        year = data.year

        if month == 1:
            month = 'Jan'
        elif month == 2:
            month = 'Fev'
        elif month == 3:
            month = 'Mar'
        elif month == 4:
            month = 'Apr'
        elif month == 5:
            month = 'May'
        elif month == 6:
            month = 'Jun'
        elif month == 7:
            month = 'Jul'
        elif month == 8:
            month = 'Aug'
        elif month == 9:
            month = 'Sep'
        elif month == 10:
            month = 'Oct'
        elif month == 11:
            month = 'Nov'
        elif month == 12:
            month = 'Dec'

        self.data_current = '{} {}'.format(month,year)
        return self. data_current

    def write_information(self,):
        
        data = Information()
        data.date_current()
        data_current = data.date_current()
        self.information = []

        print()
        submittal = str(input("Name Submittal: "))
        print()
        to_submittal = str(input("Submitall To: "))
        print()
        description = str(input("Discription: "))
        print()
        no_submittal = str(input("Submitall No: "))
        print()
        date_submittal = str(input("Date Submitall: "))
        print()
        response = str(input("Response Required By: "))
        print()
        info = str(input("Information: "))
        print()
        

        self.information = submittal, description, to_submittal, no_submittal, date_submittal, response,info, data_current

        return(self.information)


# test = Information()
# test.write_information()
# print(test.write_information())