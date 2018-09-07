import datetime
from classes.patient import Patient

class PatientFile:
    def __init__(self):
        return;

    def create_new_file(patnum, fullname, fname, lname, patrecord, phone, pernum):
        date = datetime.date.today()
        file = open(patnum + fname + lname + '.txt', 'a+')
        file.write('############################################################\n'
        + patrecord + '\n' +
        '############################################################\n\n' +
        'Phone: ' + phone + '\n' + 'Personnummer: ' + pernum + '\n' + '\n' + '----------------------------\n'
        + str(date) + ' First Appointment''\n' +
        '----------------------------' + '\n')

        file.write(input('\nNew Entry: '))
        file.close()

    def open_existing_file(id):
        date = datetime.date.today()
        with open(id + '.txt', 'a+') as myfile:
            myfile.write('\n\n----------------\n'
            + str(date) + '\n' +
            '----------------\n')
            myfile.write(input('\nNew Entry: '))
            myfile.close()
