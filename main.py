#Goanna PMS

from classes.patient import Patient
from classes.patientFile import PatientFile
import datetime

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
        PatientFile.create_new_file(
            temp_pat.getPatnum(),
            temp_pat.getFullName(),
            temp_pat.getFName(),
            temp_pat.getLName(),
            temp_pat.getPatRecord()
            )
    elif greeting.lower() in ['o', 'open']:
        id = input('enter first name, last name and patient number as a single string: ')
        PatientFile.open_existing_file(id)
        main_menu()
    elif greeting.lower() in ['s', 'search']:
        print('There is no search implemented yet')
        main_menu()
    else:
        print('Enter N to start a new patient file \nPress O to open an existing patient file')

main_menu()
