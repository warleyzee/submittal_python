from docxtpl import DocxTemplate
import pandas as pd
import jinja2
import re 
from docx2pdf import convert
from information import Information

class Save_File():

    def data_information(self,):
        information = Information()
        data = information.write_information()
        
        submittal = data[0]    
        description = data[1]
        to_submittal = data[2]
        no_submittal = data[3]
        date_submittal = data[4]
        response = data[5]
        info = data[6]
        date_current = data[7]

        doc = DocxTemplate("Submittal.docx")
        context = { 'submittal': submittal,    
                    'description': description,
                    'to': to_submittal,
                    'no': no_submittal,
                    'date_sub': date_submittal,
                    'response': response,
                    'info': info, 
                    'date_current': date_current}
        doc.render(context)
        doc.save("Submittal #{} - {}.docx".format(no_submittal, submittal))

        convert(r"C:\Users\Warley Souza\Music\Submittal\Submittal #{} - {}.docx".format(no_submittal, submittal),
                r"C:\Users\Warley Souza\Music\Submittal\Submittal #{} - {}.pdf".format(no_submittal, submittal))  
            

# test = Save_File()
# print(test.data_information())


