#Goanna PMS

from classes.patient import Patient
#from patientFile import PatientFile, newFile
from datetime import datetime

pat_dict = {}

def main_menu():

    print('\nGoanna PMS - Main menu \n')
    print('(N)ew patient')
    print('(O)pen patient file')
    print('(S)earch patient')
    print('(Q)uit \n')

    greeting = input('What would you like to do?: ')
    if greeting.lower() in ['n', 'new']:
        temp_pat = Patient()
        update_patient_dict(
            temp_pat.getPatnum(),
            temp_pat.getFullName(),
            temp_pat.getFName(),
            temp_pat.getLName(),
            temp_pat.getPatRecord()
            )
    elif greeting.lower() in ['o', 'open']:
        print('Nothing to do, yet')
    elif greeting.lower() in ['s', 'search']:
        print('There is no search implemented yet')
        main_menu()
    else:
        print('Enter N to start a new patient file \nPress O to open an existing patient file')
    #return;

def update_patient_dict(patnum, fullname, fname, lname, patrecord):

    file = open(fname + lname + patnum + '.txt', 'a+')
    file.write('############################################################\n'
    + patrecord + '\n' +
    '############################################################\n')
    file.write(input('\nNew Entry:'))
    file.close()

    #pat_dict['full_name'] = patnum

    #temp_pat = Patient(fname, lname, phone, pernum, patnum)

    #print('New patient entry recorded: ' + temp_pat.get_pat_record())

    #print('{}'.format(temp_pat.fname))
    #PatientFile().newFile()
    return;

main_menu()
