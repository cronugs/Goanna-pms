import datetime

class PatientFile:
    def __init__(self):
        return;

    def create_new_file(patnum, fullname, fname, lname, patrecord):
        date = datetime.date.today()
        file = open(fname + lname + patnum + '.txt', 'a+')
        file.write('############################################################\n'
        + patrecord + '\n' +
        '############################################################\n\n' + '----------------------------\n'
        + str(date) + ' First Appointment''\n' +
        '----------------------------\n')

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
            

    '''def newFile(self, fname, lname, phone, pernum, patnum):
        fo = open(full_name + ".txt", "a+")
        fo.write(datetime.date + " " + 'full_name \n')

        append = input('Would you like to begin documenting this case now?: Y/n')
        if append == 'N' or 'n':
            fo.close()
            print('File saved and closed')
            main_menu()
        elif append == 'Y' or 'y':
            fo.write(input('Case notes: \n'))
        else:
            main_menu()

        fo.close()

    def openFile():'''
